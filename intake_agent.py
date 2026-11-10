"""
Intake agent for the AI legal assistant (v1).

Scope: INTAKE ONLY. The agent gives no legal advice, cites no law, and drafts nothing.
It only EXTRACTS information (via the LLM) and PHRASES clarifying questions. All
decisions — missing slots, next questions, escalation, readiness verdict — are plain
deterministic code in case_schema.py.

State persists as JSON (CaseFile.model_dump_json / CaseFile.model_validate_json).
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

from case_schema import (
    CaseFile,
    Slot,
    Party,
    Event,
    Amount,
    Evidence,
    Risk,
    Issue,
    Goal,
    SlotDef,
    SLOT_REGISTRY,
    IssueType,
    compute_readiness,
    check_escalation,
    escalation_severity,
    next_questions,
    derive_flags,
    MAX_ASKS_PER_SLOT,
    _d,
    _val,
)

# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------
MAX_QUESTIONS_PER_TURN = 3

ESCALATION_MESSAGE_EN = (
    "I'm not able to continue with intake for this situation. "
    "It sounds like you may need urgent help from a qualified lawyer. "
    "You can contact a lawyer directly, or reach NALSA free legal aid at 15100. "
    "Please stop here and speak with a legal professional."
)

REFERRAL_MESSAGE_EN = (
    "I can't help with this type of legal issue yet. "
    "It falls outside the areas I currently support "
    "(security deposits and unpaid salary in Delhi, Maharashtra, Karnataka, and Tamil Nadu). "
    "You can contact a lawyer directly, or reach NALSA free legal aid at 15100."
)

NOT_READY_INTRO_EN = (
    "To help you understand your position, I need a little more information. "
    "Please answer the following (you can say 'I don't know' for anything):\n"
)

READY_MESSAGE_EN = (
    "Thank you — I have enough information to understand your situation. "
    "I have not given any legal advice or cited any law. "
    "Your case file is now ready to be handed to the appropriate specialist, "
    "who can explain your legal position and next steps."
)


# ==========================================================================
# LLM client interface (swappable provider)
# ==========================================================================
class LLMClient(ABC):
    @abstractmethod
    def complete(self, prompt: str, schema: type[BaseModel]) -> BaseModel:
        """Return a validated instance of `schema` extracted from `prompt`."""
        raise NotImplementedError


# ==========================================================================
# Extraction schema (what the LLM returns)
# ==========================================================================
class SlotFill(BaseModel):
    key: str
    value: Any
    confidence: float = Field(1.0, ge=0, le=1)


class RiskIndicators(BaseModel):
    police_or_arrest: Optional[bool] = None
    criminal_allegation_against_user: Optional[bool] = None
    threats_or_violence: Optional[bool] = None
    domestic_violence: Optional[bool] = None
    court_summons_or_hearing_date: Optional[str] = None   # ISO date
    notice_reply_deadline: Optional[str] = None           # ISO date


class Extraction(BaseModel):
    primary_issue: Optional[IssueType] = None
    issue_confidence: float = Field(0.0, ge=0, le=1)
    secondary_issues: list[str] = []
    state: Optional[str] = None
    city: Optional[str] = None
    user_role: Optional[Literal["tenant", "landlord", "employee", "employer", "other"]] = None
    slot_fills: list[SlotFill] = []
    parties: list[dict] = []
    timeline: list[dict] = []
    amounts: list[dict] = []
    evidence: list[dict] = []
    risk: RiskIndicators = Field(default_factory=RiskIndicators)
    notice_received: bool = False
    notice_sender: Optional[str] = None
    notice_claims: Optional[str] = None
    notice_demanded_amount: Optional[float] = None
    notice_reply_deadline: Optional[str] = None
    detected_language: str = "en"
    summary: Optional[str] = None


def normalize_primary_issue(issue_str: Optional[str], user_text: str = "") -> str:
    """Normalize and guard against LLM issue classification drift."""
    norm = str(issue_str or "").lower().replace(" ", "_").replace("-", "_").strip()

    if norm in ("security_deposit", "unpaid_salary"):
        return norm

    deposit_kw = ("deposit", "rent", "landlord", "tenant", "lease", "tenancy")
    salary_kw = ("salary", "wage", "employer", "employee", "severance", "resignation", "gratuity")

    if any(k in norm for k in deposit_kw):
        return "security_deposit"
    if any(k in norm for k in salary_kw):
        return "unpaid_salary"

    # Heuristic safety net on raw user text
    low_text = user_text.lower()
    is_deposit = "security" in low_text and any(k in low_text for k in ("deposit", "landlord", "rent", "tenant"))
    is_salary = any(k in low_text for k in ("salary", "wage", "wages")) and any(
        k in low_text for k in ("unpaid", "not paid", "employer", "pending", "settlement")
    )

    if is_deposit and not is_salary:
        return "security_deposit"
    if is_salary and not is_deposit:
        return "unpaid_salary"

    return norm if norm in ("other", "unclassified") else "other"


# ==========================================================================
# Real LLM client — OpenAI-compatible endpoint (e.g. Gemini via aionlabs)
# ==========================================================================
class GeminiLLMClient(LLMClient):
    """Real LLM client backed by an OpenAI-compatible chat completions endpoint.

    Usage:
        client = GeminiLLMClient(api_key="YOUR_GEMINI_API_KEY")
        result = process_turn(case, user_message, llm_client=client)

    Where to paste your key:
        Replace "YOUR_GEMINI_API_KEY" below with your actual Gemini API key string,
        or set the GEMINI_API_KEY environment variable and pass it in.
    """

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-3.5-flash-lite",
        base_url: str = "https://generativelanguage.googleapis.com/v1beta/openai/",
    ):
        from openai import OpenAI

        self._client = OpenAI(base_url=base_url, api_key=api_key)
        self._model = model

    def complete(self, prompt: str, schema: type[BaseModel]) -> BaseModel:
        import time
        max_attempts = 4
        last_err = None
        for attempt in range(max_attempts):
            try:
                completion = self._client.chat.completions.create(
                    model=self._model,
                    messages=[{"role": "user", "content": prompt}],
                    response_format={"type": "json_object"},
                )
                break
            except Exception as e:
                last_err = e
                if attempt < max_attempts - 1:
                    time.sleep(2 * (attempt + 1))
                else:
                    raise last_err

        content = completion.choices[0].message.content
        if not content:
            raise ValueError("LLM returned an empty response.")

        import json as _json

        cleaned_content = content.strip()
        if cleaned_content.startswith("```"):
            cleaned_content = re.sub(r"^```(?:json)?\s*", "", cleaned_content, flags=re.IGNORECASE)
            cleaned_content = re.sub(r"\s*```$", "", cleaned_content)
        data = _json.loads(cleaned_content)

        if isinstance(schema, type) and issubclass(schema, Extraction):
            data["primary_issue"] = normalize_primary_issue(data.get("primary_issue"), prompt)

            # Collect top-level slot keys into slot_fills
            all_known_keys = {sd.key for sds in SLOT_REGISTRY.values() for sd in sds}
            if "slot_fills" not in data or not isinstance(data["slot_fills"], list):
                data["slot_fills"] = []

            existing_fill_keys = {
                f.get("key") for f in data["slot_fills"] if isinstance(f, dict)
            }

            for k, v in list(data.items()):
                if k in all_known_keys and k not in existing_fill_keys and v is not None:
                    data["slot_fills"].append({"key": k, "value": v, "confidence": 1.0})
                    existing_fill_keys.add(k)

            # Ingest amounts into slot_fills if not already populated
            for amt in data.get("amounts", []):
                if isinstance(amt, dict):
                    lbl = str(amt.get("label", "")).lower()
                    val = amt.get("value_inr")
                    if "deposit" in lbl and "deposit_amount_inr" not in existing_fill_keys and val:
                        data["slot_fills"].append({"key": "deposit_amount_inr", "value": val, "confidence": 1.0})
                        existing_fill_keys.add("deposit_amount_inr")
                    elif any(w in lbl for w in ("salary", "wage", "unpaid")) and "amount_unpaid_inr" not in existing_fill_keys and val:
                        data["slot_fills"].append({"key": "amount_unpaid_inr", "value": val, "confidence": 1.0})
                        existing_fill_keys.add("amount_unpaid_inr")

        return schema.model_validate_json(_json.dumps(data))


# ==========================================================================
# Helpers
# ==========================================================================
_EN_KEYWORDS = {
    "police_or_arrest": [r"\bpolice\b", r"\barrest\b", r"\bfir\b", r"\bpolice station\b", r"\bcustody\b"],
    "criminal_allegation_against_user": [r"\bcriminal\b", r"\ballegation\b", r"\btheft\b", r"\bfraud\b", r"\bcheating\b"],
    "threats_or_violence": [r"\bthreat\b", r"\bthreaten\b", r"\bviolence\b", r"\bbeat\b", r"\bbeating\b", r"\bhurt\b", r"\bhit\b"],
    "domestic_violence": [r"\bdomestic violence\b", r"\bdowry\b", r"\bhusband\b", r"\bwife\b"],
}


def detect_language(text: str) -> str:
    """English only for now."""
    return "en"

def keyword_safety_net(text: str) -> dict[str, bool]:
    """English keyword scan of the RAW user text.

    Uses whole-word (\\b) regex matching to avoid false positives from
    substrings (e.g. 'hit' in 'whitefield', 'fir' in 'confirm').
    """
    import re
    hits: dict[str, bool] = {}
    low = text.lower()
    for field, patterns in _EN_KEYWORDS.items():
        if any(re.search(p, low) for p in patterns):
            hits[field] = True
    return hits


# Indian states and union territories for fallback state detection.
_INDIAN_STATES_UTS = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Delhi", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan",
    "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh",
    "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu",
    "Lakshadweep", "Puducherry",
]


def _detect_state_from_text(case: CaseFile, text: str) -> None:
    """Try to detect an Indian state/UT from raw user text as a fallback."""
    low = text.lower()
    for state in _INDIAN_STATES_UTS:
        if state.lower() in low:
            case.state = state
            return


def _apply_risk_hits(case: CaseFile, hits: dict[str, bool]) -> None:
    r = case.risk
    for flag, value in hits.items():
        if value is True and hasattr(r, flag):
            setattr(r, flag, True)


from datetime import date, timedelta


def _clean_amount(val: Any) -> Any:
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        cleaned = re.sub(r"[^\d.]", "", val)
        if cleaned:
            try:
                return float(cleaned)
            except ValueError:
                pass
    return val


def resolve_relative_date(val: Any, today: Optional[date] = None) -> Any:
    if not val or not isinstance(val, str):
        return val
    today = today or date.today()
    s = val.strip().lower()

    # Match '40 days ago', '40 days since i left', 'past 30 days', '30 days'
    m_days = re.search(r"(\d+)\s*days?", s)
    if m_days and any(w in s for w in ("ago", "since", "past", "left", "moved", "before", "days", "vacated")):
        days = int(m_days.group(1))
        return (today - timedelta(days=days)).isoformat()

    # Match '2 months ago', 'past 3 months'
    m_months = re.search(r"(\d+)\s*months?", s)
    if m_months and any(w in s for w in ("ago", "since", "past", "before", "months")):
        months = int(m_months.group(1))
        return (today - timedelta(days=months * 30)).isoformat()

    return val


def build_extraction_prompt(case: CaseFile, user_message: str, today: Optional[date] = None) -> str:
    today = today or date.today()

    active_issue = case.issue.primary
    if active_issue in ("unclassified", "other"):
        candidate = normalize_primary_issue(active_issue, user_message)
        if candidate in ("security_deposit", "unpaid_salary"):
            active_issue = candidate

    registry = SLOT_REGISTRY.get(active_issue, [])
    if not registry:
        slots_desc = "For security deposit:\n" + "\n".join(
            f"- {sd.key}: {sd.question}" for sd in SLOT_REGISTRY["security_deposit"]
        ) + "\n\nFor unpaid salary:\n" + "\n".join(
            f"- {sd.key}: {sd.question}" for sd in SLOT_REGISTRY["unpaid_salary"]
        )
    else:
        slots_desc = "\n".join(
            f"- {sd.key}: {sd.question} (required={sd.required})" for sd in registry
        )

    known = {
        k: (s.value if s else None) for k, s in case.slots.items() if s and s.status == "known"
    }

    return f"""You are an intake extraction assistant for an Indian legal assistant.

TASK: Extract information from the user's message into structured JSON.
TODAY'S REFERENCE DATE: {today.isoformat()} (Use this to resolve relative expressions like "40 days ago", "40 days since I left", "last month", "yesterday", "2 months ago" into approximate ISO dates YYYY-MM-DD or YYYY-MM).

PRIMARY ISSUE CLASSIFICATION:
Classify 'primary_issue' as exactly one of:
- "security_deposit": if the dispute involves a tenant/landlord security deposit, rental advance, deduction, or withholding of deposit.
- "unpaid_salary": if the dispute involves unpaid wages, salary delays, termination dues, or gratuity.
- "other": for any other legal problem outside these two.

TARGET SCHEMA JSON FORMAT:
Return a JSON object with this shape:
{{
  "primary_issue": "security_deposit" or "unpaid_salary" or "other",
  "issue_confidence": 0.9,
  "state": "State/UT name if stated (e.g. Karnataka, Delhi, Maharashtra, Tamil Nadu)",
  "city": "City name if stated",
  "user_role": "tenant" or "employee" or "landlord" or "employer",
  "slot_fills": [
    {{"key": "slot_key", "value": "extracted value", "confidence": 1.0}}
  ],
  "amounts": [{{"label": "security deposit", "value_inr": 30000}}],
  "summary": "Brief factual summary of user message"
}}

IMPORTANT RULES:
- When the user answers questions (e.g. "Karnataka 2) residential 3) 30000"), extract EVERY answer into 'state' and 'slot_fills':
    - state: "Karnataka"
    - key "property_type": "residential"
    - key "deposit_amount_inr": 30000
    - key "tenancy_end_date": compute approximate ISO date from relative phrases like "40 days since I left"
- For numeric amounts (e.g. 30000, 30,000, 20k), record the numeric number in value.
- Only extract what the user explicitly stated or confirmed. Do not guess or invent.

CONVERSATION SUMMARY SO FAR: {case.user_goal_text or "(none)"}
ALREADY KNOWN SLOTS (do not re-ask these): {known}
WORKING PRIMARY ISSUE: {active_issue}

SLOTS TO FILL FOR THIS ISSUE:
{slots_desc}

USER MESSAGE: {user_message}

Extract into the schema."""


def merge_extraction(case: CaseFile, extraction: Extraction, user_message: str, today: Optional[date] = None) -> None:
    today = today or date.today()
    if extraction.detected_language:
        case.language = extraction.detected_language
    if extraction.state:
        case.state = extraction.state
    if extraction.city:
        case.city = extraction.city
    if extraction.user_role:
        existing = [p for p in case.parties if p.is_user]
        if not existing:
            case.parties.append(Party(role=extraction.user_role, is_user=True, entity_type="unknown"))
        else:
            existing[0].role = extraction.user_role
    for fill in extraction.slot_fills:
        key = fill.key
        if key == "state":
            case.state = str(fill.value)
            continue  # state is a case-level field, not a slot
        slot = case.slots.get(key)
        if slot is None:
            slot = Slot()
            case.slots[key] = slot
        if slot.status == "unknown" and fill.value is not None:
            val = fill.value
            if key in ("tenancy_end_date", "deposit_paid_date", "employment_end_date", "unpaid_period_from", "unpaid_period_to"):
                val = resolve_relative_date(val, today)
            elif key in ("deposit_amount_inr", "monthly_wage_inr", "amount_unpaid_inr", "monthly_rent_inr"):
                val = _clean_amount(val)
            slot.status = "known"
            slot.value = val
            slot.source = "user"
            slot.raw_quote = user_message
    for t in extraction.timeline or []:
        case.timeline.append(Event(
            date=t.get("date"), precision=t.get("precision", "unknown"),
            event=t.get("event", ""), source=t.get("source", "user"),
            confidence=float(t.get("confidence", 1.0)),
        ))
    for a in extraction.amounts or []:
        case.amounts.append(Amount(
            label=a.get("label", ""), value_inr=float(a.get("value_inr", 0)),
            status=a.get("status", "claimed"),
        ))
    for e in extraction.evidence or []:
        case.evidence.append(Evidence(
            item=e.get("item", ""), have=e.get("have", "unsure"),
            can_obtain=e.get("can_obtain"), note=e.get("note"),
        ))
    r = case.risk
    ri = extraction.risk
    for flag in ("police_or_arrest", "criminal_allegation_against_user",
                 "threats_or_violence", "domestic_violence"):
        if getattr(ri, flag) is True:
            setattr(r, flag, True)
    if ri.court_summons_or_hearing_date:
        r.court_summons_or_hearing_date = ri.court_summons_or_hearing_date
    if ri.notice_reply_deadline:
        r.notice_reply_deadline = ri.notice_reply_deadline
    if extraction.notice_received:
        note = (
            f"received legal notice from {extraction.notice_sender or 'unknown'} "
            f"claiming {extraction.notice_claims or ''} "
            f"demanding ₹{extraction.notice_demanded_amount or ''} "
            f"by {extraction.notice_reply_deadline or ''}"
        )
        if note not in case.issue.secondary_notes:
            case.issue.secondary_notes.append(note)
        if extraction.notice_reply_deadline:
            case.risk.notice_reply_deadline = extraction.notice_reply_deadline
    if extraction.summary:
        case.user_goal_text = (
            (case.user_goal_text + " | ") if case.user_goal_text else ""
        ) + extraction.summary

    # Heuristic fallback for property_type
    pt_slot = case.slots.get("property_type")
    if not pt_slot or pt_slot.status == "unknown":
        low_msg = user_message.lower()
        if "residential" in low_msg:
            if not pt_slot:
                pt_slot = Slot()
                case.slots["property_type"] = pt_slot
            pt_slot.status = "known"
            pt_slot.value = "residential"
            pt_slot.source = "user"
        elif "commercial" in low_msg:
            if not pt_slot:
                pt_slot = Slot()
                case.slots["property_type"] = pt_slot
            pt_slot.status = "known"
            pt_slot.value = "commercial"
            pt_slot.source = "user"

    # Heuristic fallback for deposit amount
    dep_slot = case.slots.get("deposit_amount_inr")
    if not dep_slot or dep_slot.status == "unknown":
        for a in case.amounts:
            if "deposit" in a.label.lower() and a.value_inr > 0:
                if not dep_slot:
                    dep_slot = Slot()
                    case.slots["deposit_amount_inr"] = dep_slot
                dep_slot.status = "known"
                dep_slot.value = float(a.value_inr)
                dep_slot.source = "user"
                break
        if not dep_slot or dep_slot.status == "unknown":
            m_amt = re.search(r"\b(?:rs\.?|inr)?\s*(\d{1,3}(?:,\d{3})+|\d+)\b", user_message, re.IGNORECASE)
            if m_amt:
                amt_val = _clean_amount(m_amt.group(1))
                if amt_val and amt_val >= 1000:
                    if not dep_slot:
                        dep_slot = Slot()
                        case.slots["deposit_amount_inr"] = dep_slot
                    dep_slot.status = "known"
                    dep_slot.value = amt_val
                    dep_slot.source = "user"

    # Heuristic fallback for tenancy_end_date relative expressions
    ted_slot = case.slots.get("tenancy_end_date")
    if not ted_slot or ted_slot.status == "unknown":
        rel_date = resolve_relative_date(user_message, today)
        if rel_date != user_message:
            if not ted_slot:
                ted_slot = Slot()
                case.slots["tenancy_end_date"] = ted_slot
            ted_slot.status = "known"
            ted_slot.value = rel_date
            ted_slot.source = "user"


def pick_primary_issue(case: CaseFile, extraction: Extraction, user_message: str = "") -> None:
    norm = normalize_primary_issue(extraction.primary_issue, user_message)
    case.issue.primary = norm  # type: ignore[assignment]
    case.issue.confidence = float(extraction.issue_confidence or (1.0 if norm in ("security_deposit", "unpaid_salary") else 0.0))
    for s in extraction.secondary_issues or []:
        if s and s != norm and s not in case.issue.secondary_notes:
            case.issue.secondary_notes.append(s)


# Synthetic slot definition for asking the user's state/UT (not in any issue registry).
STATE_SLOT_DEF = SlotDef(
    "state",
    "Which state/UT is the property located in (e.g. Delhi, Maharashtra, Karnataka, Tamil Nadu)?",
    "Needed to determine which rent laws apply to your case.",
    required=True,
)


def select_questions(case: CaseFile, n: int = MAX_QUESTIONS_PER_TURN) -> list[SlotDef]:
    """Pick up to n unanswered required slots.
    State/UT is essential for jurisdictional gating; prioritize it when missing."""
    out: list[SlotDef] = []
    if not case.state:
        out.append(STATE_SLOT_DEF)
    for q in next_questions(case, n=n):
        if len(out) >= n:
            break
        if q.key not in [x.key for x in out]:
            out.append(q)
    return out[:n]


def phrase_questions(case: CaseFile, questions: list[SlotDef], lang: str) -> str:
    intro = NOT_READY_INTRO_EN
    outro = "\n(If you don't know an answer, just say so.)"
    lines = [intro]
    for i, q in enumerate(questions, 1):
        lines.append(f"{i}. {q.question}")
    lines.append(outro)
    return "\n".join(lines)


def ready_message(lang: str) -> str:
    return READY_MESSAGE_EN


def escalation_message(lang: str, severity: Optional[str] = None) -> str:
    if severity == "referral":
        return REFERRAL_MESSAGE_EN
    return ESCALATION_MESSAGE_EN


# ==========================================================================
# Turn result
# ==========================================================================
@dataclass
class TurnResult:
    case: CaseFile
    reply_text: str
    verdict: str
    escalation_reasons: list[str] = field(default_factory=list)
    missing_required: list[str] = field(default_factory=list)
    asked_questions: list[str] = field(default_factory=list)
    severity: Optional[str] = None


# ==========================================================================
# Main entry point
# ==========================================================================
def process_turn(
    case: CaseFile,
    user_message: str,
    today: Optional[date] = None,
    llm_client: Optional[LLMClient] = None,
) -> TurnResult:
    """Process one user turn. Returns updated case + reply + verdict.

    `llm_client` is required — pass a `GeminiLLMClient(api_key="YOUR_KEY")` instance.
    """
    today = today or date.today()
    if llm_client is None:
        raise ValueError(
            "llm_client is required. Create one with:\n"
            "    from intake_agent import GeminiLLMClient\n"
            "    client = GeminiLLMClient(api_key='YOUR_GEMINI_API_KEY')\n"
            "    process_turn(case, user_message, llm_client=client)"
        )

    lang = detect_language(user_message)
    case.language = lang

    _apply_risk_hits(case, keyword_safety_net(user_message))

    extraction = llm_client.complete(build_extraction_prompt(case, user_message, today=today), Extraction)

    merge_extraction(case, extraction, user_message, today=today)

    # Fallback: detect state/UT from raw user text if the LLM missed it.
    if not case.state:
        _detect_state_from_text(case, user_message)

    pick_primary_issue(case, extraction, user_message)

    esc = check_escalation(case, today)
    if esc:
        severity = escalation_severity(esc)
        return TurnResult(
            case=case,
            reply_text=escalation_message(lang, severity),
            verdict="escalate",
            escalation_reasons=esc,
            missing_required=[],
            asked_questions=[],
            severity=severity,
        )

    case.flags = derive_flags(case)
    readiness = compute_readiness(case, today)

    if readiness.verdict == "ready":
        return TurnResult(
            case=case,
            reply_text=ready_message(lang),
            verdict="ready",
            escalation_reasons=[],
            missing_required=readiness.missing_required,
            asked_questions=[],
        )

    questions = select_questions(case, MAX_QUESTIONS_PER_TURN)
    for q in questions:
        if q.key not in case.slots:
            case.slots[q.key] = Slot()
        slot = case.slots[q.key]
        slot.asked_count += 1

    return TurnResult(
        case=case,
        reply_text=phrase_questions(case, questions, lang),
        verdict="not_ready",
        escalation_reasons=[],
        missing_required=readiness.missing_required,
        asked_questions=[q.key for q in questions],
    )


def save_case(case: CaseFile, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(case.model_dump_json(indent=2, ensure_ascii=False))


def load_case(path: str) -> CaseFile:
    import json
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return CaseFile.model_validate(data)


if __name__ == "__main__":
    from case_schema import Slot
    case = CaseFile(case_id="smoke", language="en", state="Delhi")
    res = process_turn(
        case,
        "My landlord is not returning my security deposit of Rs 50000.",
        today=date(2026, 11, 10),
    )
    print("VERDICT:", res.verdict)
    print("REPLY:\n", res.reply_text)
    print("ASKED:", res.asked_questions)
