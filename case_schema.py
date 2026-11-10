"""
Case-file schema + deterministic readiness logic for the legal-assistant intake agent.

Division of labour:
  - The LLM (intake agent) only EXTRACTS: it fills slots / timeline / parties / etc.
  - This module decides everything else in plain code: which slots are missing,
    what to ask next, whether to escalate, and the final readiness verdict.

Requires: pydantic>=2
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Callable, Literal, Optional

from pydantic import BaseModel, Field

# --------------------------------------------------------------------------
# Config
# --------------------------------------------------------------------------
SUPPORTED_RENT_STATES = {"Delhi", "Maharashtra", "Karnataka", "Tamil Nadu"}
LABOUR_CODES_EFFECTIVE = date(2025, 11, 21)  # verify against the gazette notification
MAX_ASKS_PER_SLOT = 2          # stop nagging after this many unanswered asks
DEADLINE_ESCALATION_DAYS = 7   # court date / notice deadline closer than this -> escalate

IssueType = Literal["security_deposit", "unpaid_salary", "other", "unclassified"]
SlotStatus = Literal["known", "unknown", "not_applicable", "declined"]
Source = Literal["user", "document", "inferred"]
Goal = Literal[
    "get_money_back", "understand_position", "send_notice",
    "respond_to_notice", "prepare_for_dispute", "other",
]


# --------------------------------------------------------------------------
# Case-file building blocks
# --------------------------------------------------------------------------
class Slot(BaseModel):
    value: Any = None
    status: SlotStatus = "unknown"
    source: Optional[Source] = None
    asked_count: int = 0           # how many times we've asked; avoids question loops
    raw_quote: Optional[str] = None  # user's own words, for audit/debugging


class Party(BaseModel):
    role: Literal["tenant", "landlord", "employee", "employer", "other"]
    name: Optional[str] = None
    is_user: bool = False
    entity_type: Optional[Literal["individual", "proprietorship", "company", "government", "unknown"]] = None


class Event(BaseModel):
    date: Optional[str] = None     # ISO, partial allowed: "2025", "2025-03", "2025-03-14"
    precision: Literal["day", "month", "year", "unknown"] = "unknown"
    event: str
    source: Source = "user"
    confidence: float = Field(1.0, ge=0, le=1)


class Amount(BaseModel):
    label: str                     # e.g. "security deposit", "unpaid salary"
    value_inr: float
    status: Literal["claimed", "agreed", "disputed", "paid", "unknown"] = "unknown"


class Evidence(BaseModel):
    item: str                      # "rent agreement", "bank statement", "WhatsApp chat"
    have: Literal["yes", "no", "unsure"] = "unsure"
    can_obtain: Optional[bool] = None
    note: Optional[str] = None


class Risk(BaseModel):
    """Escalate-now triggers. Any truthy value => verdict 'escalate'."""
    police_or_arrest: Optional[bool] = None
    criminal_allegation_against_user: Optional[bool] = None
    threats_or_violence: Optional[bool] = None
    domestic_violence: Optional[bool] = None
    court_summons_or_hearing_date: Optional[str] = None   # ISO date
    notice_reply_deadline: Optional[str] = None           # ISO date


class Issue(BaseModel):
    primary: IssueType = "unclassified"
    secondary_notes: list[str] = []      # keep other issues as notes, don't route on them
    confidence: float = Field(0.0, ge=0, le=1)


class CaseFile(BaseModel):
    case_id: str
    language: str = "en"                 # user's language; case file itself is canonical English
    state: Optional[str] = None          # retrieval filters on this
    city: Optional[str] = None
    issue: Issue = Issue()
    user_goal: Optional[Goal] = None
    user_goal_text: Optional[str] = None
    parties: list[Party] = []
    timeline: list[Event] = []
    amounts: list[Amount] = []
    evidence: list[Evidence] = []
    slots: dict[str, Slot] = {}
    risk: Risk = Risk()
    flags: list[str] = []                # derived in code, see derive_flags()
    # Intermediate carrier for the domain (explain) agent's output, added by
    # eval/run_scenario.py so the transcript + scoring can inspect citations
    # and legalese. Not part of the public case schema contract.
    explanation_fields: dict[str, Any] = Field(default_factory=dict)


# --------------------------------------------------------------------------
# Slot registry: what each issue type needs
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class SlotDef:
    key: str
    question: str                         # the intake agent rephrases this in the user's language
    why: str                              # shown to the user if they ask "why do you need this?"
    required: bool = True
    required_when: Optional[Callable[[dict[str, Slot]], bool]] = None  # conditional requirement


def _val(slots: dict[str, Slot], key: str) -> Any:
    s = slots.get(key)
    return s.value if s and s.status == "known" else None


SECURITY_DEPOSIT_SLOTS: list[SlotDef] = [
    SlotDef("property_type", "Was the property residential (a home) or commercial (a shop/office)?",
            "Different rules apply to homes and commercial premises."),
    SlotDef("deposit_amount_inr", "How much security deposit did you pay?",
            "This is the amount you can claim back."),
    SlotDef("deposit_paid_date", "Roughly when did you pay the deposit (month and year is fine)?",
            "Needed for the timeline and the time limit to take action."),
    SlotDef("agreement_type", "Is there a written rent agreement? Was it registered or notarised, or only verbal?",
            "It determines what you can prove and which rules apply."),
    SlotDef("tenancy_end_date", "When did you move out / when did the tenancy end?",
            "The refund clock and the time limit usually start here."),
    SlotDef("possession_handed_over", "Did you hand back the keys and the property? Is there any proof (message, receipt, photos)?",
            "Landlords often delay refund until handover, so we need to know this is done."),
    SlotDef("landlord_reason_for_withholding", "What reason, if any, has the landlord given for not returning the deposit?",
            "We need to know what the other side will argue."),
    SlotDef("demand_made", "Have you asked for the deposit back? How (call, WhatsApp, letter) and when?",
            "A prior demand is usually a first step before a formal notice."),
    # optional but useful
    SlotDef("monthly_rent_inr", "What was the monthly rent?", "Used to check the deposit against usual limits.", required=False),
    SlotDef("deposit_payment_mode", "How did you pay the deposit (cash, bank transfer, UPI, cheque)?", "Affects the proof you have.", required=False),
    SlotDef("notice_given_by_tenant", "Did you give notice before leaving? How long before?", "Landlords often cite missed notice to deduct money.", required=False),
    SlotDef("amount_already_refunded_inr", "Has any part of the deposit been returned?", "Reduces the amount claimed.", required=False),
    SlotDef("deductions_claimed_inr", "Has the landlord claimed deductions (repairs, dues)? How much and for what?", "We need to check whether the deductions are reasonable.", required=False),
    SlotDef("handover_condition_documented", "Do you have photos/videos of the property condition at move-out?", "Helps against damage claims.", required=False),
]

UNPAID_SALARY_SLOTS: list[SlotDef] = [
    SlotDef("employer_type", "Is your employer a private company, a small business/shop, a contractor, or a government body?",
            "The rules and the right forum differ; government employees are out of scope."),
    SlotDef("employment_type", "Are you permanent, on contract, daily-wage, or through a contractor/agency?",
            "Different categories of workers have different protections."),
    SlotDef("monthly_wage_inr", "What is your monthly salary (or daily wage)?", "Needed to calculate what is owed."),
    SlotDef("unpaid_period_from", "From which month is your salary unpaid?", "Defines the claim period."),
    SlotDef("unpaid_period_to", "Up to which month is it unpaid (or is it still continuing)?", "Defines the claim period."),
    SlotDef("amount_unpaid_inr", "How much in total is unpaid, as far as you know?", "This is the amount you can claim."),
    SlotDef("still_employed", "Are you still working there, or have you resigned / been removed?",
            "Final-settlement rules apply after leaving."),
    SlotDef("employment_end_date", "When did your employment end?", "Final-settlement timelines start from this date.",
            required_when=lambda s: _val(s, "still_employed") is False),
    SlotDef("how_employment_ended", "Did you resign, were you terminated, or did you stop going?", "It affects what you are owed and what the employer may argue.",
            required_when=lambda s: _val(s, "still_employed") is False),
    SlotDef("employer_reason_for_nonpayment", "What reason has the employer given for not paying?", "We need to know what the other side will argue."),
    SlotDef("demand_made", "Have you asked for the salary? How (HR email, WhatsApp, in person) and when?", "A prior demand is usually a first step."),
    SlotDef("employment_proof_available", "Do you have an appointment letter, payslips, bank statements or chats showing you worked and your pay?",
            "Proof of employment and pay is the core evidence."),
    # optional but useful
    SlotDef("establishment_size", "Roughly how many people work there?", "Coverage of some benefits depends on size.", required=False),
    SlotDef("other_dues", "Besides salary, are bonus, leave pay, gratuity or PF also pending?", "These can be claimed together.", required=False),
    SlotDef("notice_period_served", "Did you serve your notice period?", "Employers often withhold pay citing this.", required=False),
    SlotDef("pf_deducted", "Was PF deducted from your salary?", "Shows formal employment.", required=False),
]

SLOT_REGISTRY: dict[str, list[SlotDef]] = {
    "security_deposit": SECURITY_DEPOSIT_SLOTS,
    "unpaid_salary": UNPAID_SALARY_SLOTS,
}


# --------------------------------------------------------------------------
# Deterministic logic (no LLM)
# --------------------------------------------------------------------------
def _d(v: Any) -> Optional[date]:
    """Parse ISO dates, partial allowed ('2025', '2025-03', '2025-03-14')."""
    if not v:
        return None
    try:
        p = str(v).split("-")
        return date(int(p[0]), int(p[1]) if len(p) > 1 else 1, int(p[2]) if len(p) > 2 else 1)
    except (ValueError, IndexError):
        return None


def _resolved(slot: Optional[Slot]) -> bool:
    if slot is None:
        return False
    return slot.status != "unknown" or slot.asked_count >= MAX_ASKS_PER_SLOT


def _is_required(sd: SlotDef, slots: dict[str, Slot]) -> bool:
    if sd.required_when is not None:
        return bool(sd.required_when(slots))
    return sd.required


class Readiness(BaseModel):
    verdict: Literal["ready", "not_ready", "escalate"]
    escalation_reasons: list[str] = []
    missing_required: list[str] = []
    missing_optional: list[str] = []
    severity: Optional[Literal["urgent", "referral"]] = None


def check_escalation(case: CaseFile, today: Optional[date] = None) -> list[str]:
    today = today or date.today()
    reasons: list[str] = []
    r = case.risk
    if r.police_or_arrest:
        reasons.append("police_or_arrest")
    if r.criminal_allegation_against_user:
        reasons.append("criminal_allegation_against_user")
    if r.threats_or_violence:
        reasons.append("threats_or_violence")
    if r.domestic_violence:
        reasons.append("domestic_violence")
    for label, raw in (("court_date", r.court_summons_or_hearing_date), ("notice_deadline", r.notice_reply_deadline)):
        d = _d(raw)
        if d and (d - today).days <= DEADLINE_ESCALATION_DAYS:
            reasons.append(f"{label}_within_{DEADLINE_ESCALATION_DAYS}_days_or_passed")
    if case.issue.primary == "other" and case.issue.confidence >= 0.6:
        reasons.append("out_of_scope_issue")
    if case.issue.primary == "security_deposit" and case.state and case.state not in SUPPORTED_RENT_STATES:
        reasons.append("unsupported_state_for_rent")
    return reasons


URGENT_REASONS = {
    "police_or_arrest",
    "criminal_allegation_against_user",
    "threats_or_violence",
    "domestic_violence",
}

REFERRAL_REASONS = {
    "out_of_scope_issue",
    "unsupported_state_for_rent",
}


def _is_deadline_reason(reason: str) -> bool:
    return reason.endswith("_within_7_days_or_passed")


def escalation_severity(reasons: list[str]) -> Optional[Literal["urgent", "referral"]]:
    """Classify escalation severity: urgent = time-critical, referral = out of scope / unsupported."""
    for r in reasons:
        if r in URGENT_REASONS or _is_deadline_reason(r):
            return "urgent"
    for r in reasons:
        if r in REFERRAL_REASONS:
            return "referral"
    return None


def compute_readiness(case: CaseFile, today: Optional[date] = None) -> Readiness:
    esc = check_escalation(case, today)
    if esc:
        return Readiness(
            verdict="escalate",
            escalation_reasons=esc,
            severity=escalation_severity(esc),
        )

    defs = SLOT_REGISTRY.get(case.issue.primary, [])
    missing_req: list[str] = []
    missing_opt: list[str] = []
    if not case.state:
        missing_req.append("state")
    for sd in defs:
        slot = case.slots.get(sd.key)
        if _is_required(sd, case.slots):
            if not _resolved(slot):
                missing_req.append(sd.key)
        elif not _resolved(slot):
            missing_opt.append(sd.key)

    return Readiness(
        verdict="not_ready" if missing_req else "ready",
        missing_required=missing_req,
        missing_optional=missing_opt,
    )


def next_questions(case: CaseFile, n: int = 3) -> list[SlotDef]:
    """Pick up to n unanswered required slots, in registry order (= priority order)."""
    defs = SLOT_REGISTRY.get(case.issue.primary, [])
    out = [sd for sd in defs
           if _is_required(sd, case.slots) and not _resolved(case.slots.get(sd.key))]
    return out[:n]


def derive_flags(case: CaseFile) -> list[str]:
    """Flags are computed from the case file, never trusted from the LLM."""
    flags: list[str] = []
    s = case.slots
    if case.issue.primary == "security_deposit" and _val(s, "tenancy_end_date"):
        flags.append("limitation_check_needed")
    if case.issue.primary == "unpaid_salary" and _val(s, "unpaid_period_from"):
        flags.append("limitation_check_needed")
        start = _d(_val(s, "unpaid_period_from"))
        if start and start < LABOUR_CODES_EFFECTIVE:
            # wages earned before the Codes came into force may fall under the repealed Acts
            flags.append("period_may_fall_under_repealed_acts")
    if case.issue.primary == "unpaid_salary" and _val(s, "employer_type") == "government":
        flags.append("government_employee_out_of_scope")
    if case.issue.secondary_notes:
        flags.append("secondary_issue_noted")
    return flags


if __name__ == "__main__":
    case = CaseFile(
        case_id="demo-1", language="hi", state="Karnataka",
        issue=Issue(primary="security_deposit", confidence=0.9,
                    secondary_notes=["may also involve unpaid maintenance dues"]),
        user_goal="get_money_back",
        slots={
            "property_type": Slot(value="residential", status="known", source="user"),
            "deposit_amount_inr": Slot(value=100000, status="known", source="user"),
            "deposit_paid_date": Slot(value="2024-03", status="known", source="user"),
            "tenancy_end_date": Slot(value="2025-12-31", status="known", source="user"),
        },
    )
    print("verdict:", compute_readiness(case, today=date(2026, 11, 10)).model_dump())
    print("ask next:", [q.key for q in next_questions(case)])
    print("flags:", derive_flags(case))