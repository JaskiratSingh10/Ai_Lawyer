"""
Domain (explain) agent — Phase 3.

ONE shared domain agent for both security_deposit and unpaid_salary, driven by
the per-issue config registry in domain_config.py.

Public entry point:
    explain(case, today=None, llm_client=None) -> Explanation

Design principles (per spec):
  - The LLM only composes an explanation from retrieved corpus chunks.
  - Every legal claim carries chunk_ids; no claim without a citation.
  - A plain-code citation validator (no LLM) drops / flags any claim whose
    chunk_id was not retrieved, any uncited legal claim, and any section
    number that does not appear in a retrieved chunk.
  - On weak retrieval, unsupported state, case-law requests, or too many
    failed validations -> abstain: "I'm not sure ... consult a lawyer"
    with NALSA free legal aid 15100.
  - Legal-status awareness: honour each chunk's effective_from / repealed_on /
    in_force_at_case_date; never tell the LLM to rely on law that isn't in
    the corpus. Stale "Pending Notification" / "not in force" labels are
    flagged (data_quality_flags), never silently fixed.
  - Never cite or invent case law; judgment requests are declined.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any

from pydantic import BaseModel, Field, field_validator

from case_schema import (
    CaseFile,
    Issue,
    Slot,
    _d,
    LABOUR_CODES_EFFECTIVE,
)
from corpus.corpus_rag_engine import LegalRAGEngine
from domain_config import (
    IssueConfig,
    IssueType,
    get_config,
)
from intake_agent import LLMClient
from limitation import (
    CLOSE_THRESHOLD_DAYS,
    LimitationResult,
    _parse_date,
    compute_limitation,
    consumer_protection_deadline_info,
)

# ---------------------------------------------------------------------------
# NALSA / abstain messaging
# ---------------------------------------------------------------------------

NALSA_MESSAGE = (
    "You can contact a lawyer directly, or reach NALSA free legal aid at 15100."
)

ABSTAIN_INTRO = "I'm not sure about this — please consult a qualified lawyer."


def _abstain_message(reason: str, detail: str | None = None) -> str:
    parts = [ABSTAIN_INTRO]
    if detail:
        parts.append(detail)
    parts.append(NALSA_MESSAGE)
    return " ".join(parts)

# ---------------------------------------------------------------------------
# LLM output schema (what the LLM returns)
# ---------------------------------------------------------------------------


class Option(BaseModel):
    title: str
    description: str
    next_steps: str
    chunk_ids: list[str] = Field(default_factory=list)
    supporting_quote: str = ""

    @field_validator("title", "description", "supporting_quote", mode="before")
    @classmethod
    def coerce_text(cls, v: Any) -> str:
        if isinstance(v, list):
            return " ".join(str(item).strip() for item in v if item)
        return str(v) if v is not None else ""

    @field_validator("next_steps", mode="before")
    @classmethod
    def coerce_next_steps(cls, v: Any) -> str:
        if isinstance(v, list):
            return "; ".join(str(item).strip() for item in v if item)
        return str(v) if v is not None else ""

    @field_validator("chunk_ids", mode="before")
    @classmethod
    def coerce_chunk_ids(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [c.strip() for c in re.split(r"[,;\s]+", v) if c.strip()]
        if isinstance(v, list):
            out = []
            for item in v:
                if isinstance(item, str):
                    out.append(item.strip())
                elif isinstance(item, dict):
                    cid = item.get("id") or item.get("chunk_id")
                    if cid:
                        out.append(str(cid).strip())
            return out
        return []


class OtherSideArg(BaseModel):
    argument: str
    chunk_ids: list[str] = Field(default_factory=list)
    supporting_quote: str = ""

    @field_validator("argument", "supporting_quote", mode="before")
    @classmethod
    def coerce_argument(cls, v: Any) -> str:
        if isinstance(v, list):
            return " ".join(str(item).strip() for item in v if item)
        return str(v) if v is not None else ""

    @field_validator("chunk_ids", mode="before")
    @classmethod
    def coerce_chunk_ids(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [c.strip() for c in re.split(r"[,;\s]+", v) if c.strip()]
        if isinstance(v, list):
            out = []
            for item in v:
                if isinstance(item, str):
                    out.append(item.strip())
                elif isinstance(item, dict):
                    cid = item.get("id") or item.get("chunk_id")
                    if cid:
                        out.append(str(cid).strip())
            return out
        return []


class LLMExplanation(BaseModel):
    summary: str
    summary_chunk_ids: list[str] = Field(default_factory=list)
    summary_supporting_quote: str = ""
    options: list[Option] = Field(default_factory=list)
    other_side: list[OtherSideArg] = Field(default_factory=list)
    evidence_gaps: list[str] = Field(default_factory=list)
    uncertainties: list[str] = Field(default_factory=list)

    @field_validator("summary", "summary_supporting_quote", mode="before")
    @classmethod
    def coerce_summary(cls, v: Any) -> str:
        if isinstance(v, list):
            return " ".join(str(item).strip() for item in v if item)
        return str(v) if v is not None else ""

    @field_validator("summary_chunk_ids", mode="before")
    @classmethod
    def coerce_summary_chunk_ids(cls, v: Any) -> list[str]:
        if isinstance(v, str):
            return [c.strip() for c in re.split(r"[,;\s]+", v) if c.strip()]
        if isinstance(v, list):
            out = []
            for item in v:
                if isinstance(item, str):
                    out.append(item.strip())
                elif isinstance(item, dict):
                    cid = item.get("id") or item.get("chunk_id")
                    if cid:
                        out.append(str(cid).strip())
            return out
        return []

    @field_validator("evidence_gaps", "uncertainties", mode="before")
    @classmethod
    def coerce_string_list(cls, v: Any) -> list[str]:
        if isinstance(v, list):
            out = []
            for item in v:
                if isinstance(item, dict):
                    out.append(" ".join(str(val) for val in item.values()))
                elif isinstance(item, list):
                    out.append(" ".join(str(val) for val in item))
                else:
                    out.append(str(item).strip())
            return [x for x in out if x]
        if isinstance(v, str):
            return [v.strip()] if v.strip() else []
        return []


# ---------------------------------------------------------------------------
# Final output schema
# ---------------------------------------------------------------------------


class Explanation(BaseModel):
    case_id: str
    issue_type: str
    state: str | None = None
    reply_text: str
    summary: str
    summary_chunk_ids: list[str] = Field(default_factory=list)
    options: list[Option] = Field(default_factory=list)
    other_side: list[OtherSideArg] = Field(default_factory=list)
    evidence_gaps: list[str] = Field(default_factory=list)
    uncertainties: list[str] = Field(default_factory=list)
    limitation: dict = Field(default_factory=dict)
    abstain: bool = False
    abstain_reason: str | None = None
    citations_used: list[str] = Field(default_factory=list)
    removed_claims: list[dict] = Field(default_factory=list)
    data_quality_flags: list[str] = Field(default_factory=list)
    case_law_declined: bool = False


# ---------------------------------------------------------------------------
# Retrieval
# ---------------------------------------------------------------------------


def _case_date(case: CaseFile, cfg: IssueConfig) -> date | None:
    """Pick the dispute/cause-of-action date for temporal evaluation."""
    start_value = None
    if case.slots and cfg.limitation.start_slot in case.slots:
        val = getattr(case.slots[cfg.limitation.start_slot], "value", None)
        if _parse_date(val) is not None:
            start_value = val
    if start_value is None and cfg.limitation.fallback_slot and case.slots:
        fb = case.slots.get(cfg.limitation.fallback_slot)
        if fb:
            val = getattr(fb, "value", None)
            if _parse_date(val) is not None:
                start_value = val
    if start_value is None and case.slots:
        for s in case.slots.values():
            val = getattr(s, "value", None)
            if _parse_date(val) is not None:
                start_value = val
                break
    return _parse_date(start_value) if start_value else None


def _jurisdiction(case: CaseFile, cfg: IssueConfig) -> str:
    if case.state and cfg.jurisdiction_by_state.get(case.state):
        return cfg.jurisdiction_by_state[case.state]
    return cfg.default_jurisdiction


def _build_queries(case: CaseFile, cfg: IssueConfig) -> list[str]:
    """Build retrieval queries from config hints + resolved key slot values."""
    queries = list(cfg.query_hints)
    s = case.slots or {}
    skip_vals = {"yes", "no", "true", "false", "none", "unknown", "null"}
    for key in cfg.relevant_slot_keys:
        slot = s.get(key)
        val = getattr(slot, "value", None) if slot else None
        if val is not None:
            s_val = str(val).strip()
            if s_val and s_val.lower() not in skip_vals and not _d(s_val):
                queries.append(f"{cfg.query_hints[0]} {s_val}")
    seen: set[str] = set()
    out: list[str] = []
    for q in queries:
        q = q.strip()
        if q and q not in seen:
            seen.add(q)
            out.append(q)
    return out


def _retrieve(
    engine: LegalRAGEngine,
    case: CaseFile,
    cfg: IssueConfig,
) -> tuple[list[dict], dict[str, Any]]:
    """Retrieve chunks filtered by state jurisdiction + scope BEFORE ranking."""
    case_date = _case_date(case, cfg)
    case_date_str = case_date.isoformat() if case_date else None
    jur = _jurisdiction(case, cfg)

    merged: dict[str, dict] = {}
    flags: dict[str, Any] = {
        "case_date": case_date_str,
        "period_may_fall_under_repealed_acts": False,
        "temporal_notes": [],
    }

    queries = _build_queries(case, cfg)

    for scope in cfg.scope_categories:
        if scope in ("Limitation", "Wage & Employment", "Consumer Protection"):
            scope_jurs = ["Central"]
        elif scope == "Rent Law":
            scope_jurs = [jur]
            if jur != "Central" and "Central" not in scope_jurs:
                scope_jurs.append("Central")
        else:
            scope_jurs = [jur]

        for s_jur in scope_jurs:
            for query in queries:
                out = engine.search(
                    query=query,
                    jurisdiction=s_jur,
                    scope_category=scope,
                    case_date=case_date_str,
                    limit=6,
                )
                for chunk in out.get("results", []):
                    merged[chunk["id"]] = chunk
                f = out.get("flags", {}) or {}
                if f.get("period_may_fall_under_repealed_acts"):
                    flags["period_may_fall_under_repealed_acts"] = True
                for note in f.get("temporal_notes", []):
                    if note not in flags["temporal_notes"]:
                        flags["temporal_notes"].append(note)

    return list(merged.values()), flags


# ---------------------------------------------------------------------------
# Legal-status awareness
# ---------------------------------------------------------------------------


def _status_notes(chunks: list[dict], case_date: date | None) -> list[str]:
    """Build uncertainty notes from each chunk's in-force status & dates.

    Never silently "fixes" a chunk; just reports what the corpus says.
    """
    notes: list[str] = []
    labour_effective = LABOUR_CODES_EFFECTIVE.isoformat()
    for c in chunks:
        cid = c["id"]
        status = c.get("legal_status")
        eff = c.get("effective_from")
        rep = c.get("repealed_on")
        temp = c.get("temporal_status") or status
        in_force = c.get("in_force_at_case_date")

        if in_force is False:
            notes.append(
                f"{cid} ({c.get('section_or_rule_number')}): {temp}. "
                "Not relied upon for this case date."
            )
            continue

        # Law effective after the case date -> cannot apply.
        if case_date and eff and eff > case_date.isoformat():
            notes.append(
                f"{cid} ({c.get('section_or_rule_number')}): effective from {eff}, "
                f"which is after the case date {case_date.isoformat()}; "
                "may not apply to your situation."
            )

        # Labour Codes specific: effective 21 Nov 2025.
        if "Code on Wages" in c.get("law_title", "") or "Code on Wages" in c.get(
            "short_title", ""
        ):
            if case_date and case_date < LABOUR_CODES_EFFECTIVE:
                notes.append(
                    f"{cid}: Code on Wages came into force on {labour_effective}; "
                    f"your case date {case_date.isoformat()} predates it, so "
                    "legacy wage laws may apply instead. Consult a lawyer."
                )

    return notes


def _audit_stale_labels(chunks: list[dict]) -> list[str]:
    """Flag chunks whose legal_status_notes suggest a stale label.

    Reported to the developer via data_quality_flags; never silently corrected.
    """
    flags: list[str] = []
    for c in chunks:
        notes = (c.get("legal_status_notes") or "") + " " + (
            c.get("legal_status") or ""
        )
        low = notes.lower()
        if "pending notification" in low or "not in force" in low:
            flags.append(
                f"STALE_LABEL: {c['id']} ({c.get('section_or_rule_number')}) "
                f"carries a 'pending/not-in-force' note while indexed as "
                f"{c.get('legal_status')}. Review corpus curation; "
                "not silently fixed."
            )
    return flags


# ---------------------------------------------------------------------------
# Prompt building for the LLM
# ---------------------------------------------------------------------------


def _format_chunks_for_prompt(chunks: list[dict]) -> str:
    """Format retrieved chunks into a citation-ready markdown block."""
    blocks = []
    for i, c in enumerate(chunks, 1):
        repeal = f" | Repealed: {c['repealed_on']}" if c.get("repealed_on") else ""
        blocks.append(
            f"### [Source {i}] [{c['id']}] {c.get('law_title')} — "
            f"{c.get('section_or_rule_number')}: {c.get('section_or_rule_title')}\n"
            f"- Jurisdiction: {c.get('jurisdiction')}\n"
            f"- Legal Status: `{c.get('legal_status')}` | Effective From: "
            f"`{c.get('effective_from')}`{repeal}\n"
            f"- In force at case date: {c.get('in_force_at_case_date')}\n"
            f"- Official URL: {c.get('official_source_url')}\n"
            f"```text\n{c.get('exact_text')}\n```\n"
        )
    return "\n".join(blocks) if blocks else "No statutory provisions found."


# ---------------------------------------------------------------------------
# Slot summary (context for the LLM, not law)
# ---------------------------------------------------------------------------


def _slot_summary(case: CaseFile, cfg: IssueConfig) -> str:
    user_roles = [p.role for p in case.parties if p.is_user and p.role]
    role_str = user_roles[0] if user_roles else ("tenant" if cfg.issue_type == "security_deposit" else "employee")
    lines: list[str] = [
        f"dispute_type: {cfg.display_name}",
        f"user_role: {role_str} (Use this exact role word '{role_str}'; do NOT use legal labels like 'licensee')",
    ]
    if case.state:
        lines.append(f"state: {case.state}")
    if case.city:
        lines.append(f"city: {case.city}")

    lines.append("\nFACTS ALREADY STATED AND CONFIRMED BY USER (Do NOT ask for these or list as missing gaps):")
    s = case.slots or {}
    for key in cfg.relevant_slot_keys:
        slot = s.get(key)
        if slot and getattr(slot, "status", None) == "known":
            lines.append(f"- {key}: {slot.value}")
    if case.amounts:
        for a in case.amounts:
            lines.append(f"- amount ({a.label}): ₹{a.value_inr:,.0f} ({a.status})")

    # Important note on user demand statements
    dem_val = getattr(s.get("demand_made"), "value", None)
    if dem_val and any(w in str(dem_val).lower() for w in ("call", "phone", "weekly", "spoke", "message")):
        lines.append(
            f"- Note on demand: The user already made demands: '{dem_val}'. "
            "Under limitation law, oral demands can already start the time clock; "
            "do NOT advise that sending a formal notice is needed to start the clock."
        )

    # Note on possession / keys
    pos_val = getattr(s.get("possession_handed_over"), "value", None)
    if pos_val:
        lines.append(
            f"- Note on possession: User stated '{pos_val}'. "
            "Do NOT list proof of handing over keys as a missing evidence gap if the user already confirmed they do not have a receipt."
        )

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Prompt building for the LLM
# ---------------------------------------------------------------------------


def _build_prompt(chunks: list[dict], case: CaseFile, cfg: IssueConfig) -> str:
    chunks_md = _format_chunks_for_prompt(chunks)
    slot_summary = _slot_summary(case, cfg)
    return f"""You are a legal-assistant domain agent for ordinary people in India (ENGLISH ONLY).
You explain the user's legal position in PLAIN LANGUAGE using ONLY the retrieved
statutory chunks below. Do not use outside knowledge. Do not cite or invent case law
(Supreme Court / High Court judgments). If asked for a judgment, say it is outside
scope and suggest a lawyer.

Retrieved corpus chunks (each has a chunk id like IND-FED-LIM-1963-ART-022):
{chunks_md}

Case summary (from intake, for context only — not law):
{slot_summary}

TASK: Return a JSON object matching the schema with these fields:
- summary: plain-language summary of the user's position.
- summary_chunk_ids: chunk ids backing the summary.
- summary_supporting_quote: exact verbatim phrase copied from one of the summary_chunk_ids that supports the summary.
- options: list of options, each with:
    - title: short option title
    - description: "What the law says" — grounded in the cited statutory chunk
    - next_steps: "Practical steps" — procedural steps for the user
    - chunk_ids: list of retrieved chunk ids
    - supporting_quote: exact verbatim phrase copied from one of the cited chunks supporting the legal statement
- other_side: list of arguments the other side may raise, each with:
    - argument: what the other side may argue under the law
    - chunk_ids: list of retrieved chunk ids
    - supporting_quote: exact verbatim phrase copied from one of the cited chunks
- evidence_gaps: list of genuinely missing evidence needed (plain strings)
- uncertainties: list of honest legal or factual uncertainties (plain strings)

STRICT RULES:
1. ONLY RELY ON RETRIEVED CHUNKS:
   - For every legal claim (in summary, options, or other_side), you MUST provide `chunk_ids` AND a `supporting_quote`.
   - `supporting_quote` MUST be an exact verbatim phrase copied from the cited chunk's text or title.
   - If you cannot quote verbatim support from a chunk, DO NOT make the claim.
2. NO INVENTED FACTS OR LEGAL LABELS:
   - Do NOT assert facts about the user that are not in the case file.
   - Use the user's own words for their role (e.g. "tenant", "room owner", "landlord"), NOT legal labels like "licensee", unless the case file explicitly says so.
3. ARGUABLE RULES & UNCERTAINTIES:
   - If a rule's applicability depends on something unknown or arguable (e.g. whether a deposit was "payable on demand", or whether oral calls already started the time limit), state it explicitly in `uncertainties` and recommend a lawyer.
   - Never present one reading as certain or settled law.
4. TIME LIMITS & NO DELAY:
   - Where a time limit or limitation is mentioned, state that the user should act early and that a lawyer should confirm the deadline.
   - NEVER advise delaying action or waiting.
   - Remember: prior oral calls or messages may already count as a demand.
5. PLAIN LANGUAGE (8TH-GRADE LEVEL):
   - Write for an ordinary person at an 8th-grade reading level.
   - Short, direct sentences. Avoid Latin or dense legal jargon.
   - If you mention a legal term, explain it in the same sentence (e.g. "limitation (the legal time limit to file in court)").
   - Separate "What the law says" (in description, cited) from "Practical steps" (in next_steps, procedural guidance).
   - Do NOT duplicate the same sentences between summary and options.

OUTPUT FORMAT (JSON only):
{{
  "summary": "Plain-language summary of user position citing relevant provisions",
  "summary_chunk_ids": ["CHUNK-ID-1"],
  "summary_supporting_quote": "exact phrase from chunk 1",
  "options": [
    {{
      "title": "Action title",
      "description": "What the law says: statutory explanation grounded in the chunk",
      "next_steps": "Practical steps: procedural steps the user should take",
      "chunk_ids": ["CHUNK-ID-1"],
      "supporting_quote": "exact phrase from chunk 1"
    }}
  ],
  "other_side": [
    {{
      "argument": "What the other side may argue under the law",
      "chunk_ids": ["CHUNK-ID-1"],
      "supporting_quote": "exact phrase from chunk 1"
    }}
  ],
  "evidence_gaps": ["Missing document or proof needed"],
  "uncertainties": ["Any factual or legal uncertainty"]
}}
"""


# ---------------------------------------------------------------------------
# Citation validator (plain code, no LLM)
# ---------------------------------------------------------------------------


_SECTION_RE = re.compile(
    r"\b(?:Section|Sec\.?|Article|Art\.?|Rule)\s+(\d+[a-z]?)\b",
    re.IGNORECASE,
)


def _norm_section(ref: str) -> str:
    """Normalize 'Section 22' / 'Article 7' / 'Rule 4' / '22' -> '22' / '7' / '4'."""
    m = re.search(r"(\d+[a-z]?)", ref, re.IGNORECASE)
    if m:
        return m.group(1).lower()
    return ref.strip().lower()


def _section_refs(text: str) -> list[str]:
    return [m.group(1) for m in _SECTION_RE.finditer(text)]


def _normalize_chunk_id(cid: str, valid_cids: set[str]) -> str | None:
    c = str(cid).strip().strip("[]'\"").strip()
    if c in valid_cids:
        return c
    if c.upper() in valid_cids:
        return c.upper()
    m = re.match(r"^(.*?-(?:SEC|ART|RULE)-)(\d+)(.*)$", c, re.IGNORECASE)
    if m:
        prefix, num, suffix = m.groups()
        for cand in valid_cids:
            mc = re.match(r"^(.*?-(?:SEC|ART|RULE)-)(\d+)(.*)$", cand, re.IGNORECASE)
            if mc:
                c_prefix, c_num, c_suffix = mc.groups()
                if (
                    c_prefix.upper() == prefix.upper()
                    and int(c_num) == int(num)
                    and c_suffix.upper() == suffix.upper()
                ):
                    return cand
    return None


def _normalize_text_for_matching(text: str) -> str:
    """Normalize text for substring matching: lowercase, alphanumeric and spaces only."""
    t = text.lower()
    t = re.sub(r"[^\w\s]", " ", t)
    return " ".join(t.split())


def _verify_quote_in_chunks(
    quote: str,
    norm_chunk_ids: list[str],
    retrieved_by_id: dict[str, dict],
) -> tuple[bool, str | None]:
    """Verify that quote is a non-trivial substring or closely matching phrase of at least one cited chunk.

    Returns (is_valid, matched_chunk_id).
    """
    clean_q = quote.strip()
    if not clean_q or len(clean_q) < 5:
        return False, None
    norm_q = _normalize_text_for_matching(clean_q)
    if not norm_q or len(norm_q) < 4:
        return False, None

    words = norm_q.split()

    for cid in norm_chunk_ids:
        chunk = retrieved_by_id.get(cid)
        if not chunk:
            continue
        c_text = _normalize_text_for_matching(chunk.get("exact_text") or "")
        c_title = _normalize_text_for_matching(chunk.get("section_or_rule_title") or "")
        target = f"{c_title} {c_text}"

        # 1. Exact normalized substring match
        if norm_q in target:
            return True, cid

        # 2. Robust match: at least one 4-word continuous sequence appears verbatim,
        # and at least 60% of quote words appear in the chunk text.
        if len(words) >= 4:
            has_subphrase = any(" ".join(words[j:j+4]) in target for j in range(len(words) - 3))
            if has_subphrase:
                target_words = set(target.split())
                overlap = sum(1 for w in words if w in target_words) / len(words)
                if overlap >= 0.6:
                    return True, cid

    return False, None


def _validate_claims(
    llm_expl: LLMExplanation,
    retrieved: list[dict],
) -> tuple[LLMExplanation, list[dict]]:
    """Drop / flag claims that fail citation rules.

    Checks:
      1. Every cited chunk must be in the retrieved set.
      2. supporting_quote must be an actual verbatim substring of at least one cited chunk.
      3. Any section number mentioned in the text must appear in the retrieved set.

    Returns (cleaned_explanation, removed_claims).
    """
    retrieved_by_id = {c["id"]: c for c in retrieved}
    retrieved_ids = set(retrieved_by_id.keys())
    retrieved_sections: set[str] = set()
    for c in retrieved:
        sec_num = c.get("section_or_rule_number") or ""
        if sec_num:
            retrieved_sections.add(_norm_section(sec_num))
        title = c.get("section_or_rule_title") or ""
        for sec in _section_refs(title):
            retrieved_sections.add(_norm_section(sec))
        for sec in _section_refs(c.get("exact_text") or ""):
            retrieved_sections.add(_norm_section(sec))

    removed: list[dict] = []

    def claim_reasons(
        text: str,
        chunk_ids: list[str],
        supporting_quote: str = "",
    ) -> tuple[list[str], list[str]]:
        reasons: list[str] = []
        norm_cids: list[str] = []
        bad_cids: list[str] = []
        for cid in chunk_ids:
            norm_cid = _normalize_chunk_id(cid, retrieved_ids)
            if norm_cid:
                norm_cids.append(norm_cid)
            else:
                bad_cids.append(cid)

        if not norm_cids and not bad_cids:
            reasons.append("uncited_claim")
        if bad_cids:
            reasons.append(f"uncited_chunk:{','.join(bad_cids)}")

        # Quote verification: must be a substring of at least one cited chunk
        if norm_cids:
            quote_ok, _ = _verify_quote_in_chunks(supporting_quote, norm_cids, retrieved_by_id)
            if not quote_ok:
                reasons.append(
                    f"unsupported_quote:quote '{supporting_quote[:40]}' not found in cited chunks"
                )

        for sec in _section_refs(text):
            if _norm_section(sec) not in retrieved_sections:
                reasons.append(f"uncited_section:{sec}")

        return norm_cids, reasons

    # Summary
    summary = llm_expl.summary
    summary_ids: list[str] = []
    bad_summary_chunks: list[str] = []
    for cid in llm_expl.summary_chunk_ids:
        norm_cid = _normalize_chunk_id(cid, retrieved_ids)
        if norm_cid:
            summary_ids.append(norm_cid)
        else:
            bad_summary_chunks.append(cid)

    s_reasons: list[str] = []
    if bad_summary_chunks:
        s_reasons.append(f"uncited_chunk:{','.join(bad_summary_chunks)}")
    if summary_ids:
        quote_ok, _ = _verify_quote_in_chunks(
            llm_expl.summary_supporting_quote, summary_ids, retrieved_by_id
        )
        if not quote_ok:
            s_reasons.append(
                f"unsupported_quote:quote '{llm_expl.summary_supporting_quote[:40]}' not found in cited chunks"
            )
    for sec in _section_refs(summary):
        if _norm_section(sec) not in retrieved_sections:
            s_reasons.append(f"uncited_section:{sec}")

    if s_reasons:
        removed.append(
            {"item": "summary", "text": summary[:120], "reasons": s_reasons}
        )
        summary = ""
        summary_ids = []

    # Options
    clean_options: list[Option] = []
    for opt in llm_expl.options:
        blob = f"{opt.title} {opt.description}"
        norm_cids, reasons = claim_reasons(blob, list(opt.chunk_ids), opt.supporting_quote)
        if reasons:
            removed.append(
                {
                    "item": f"option:{opt.title}",
                    "text": blob[:120],
                    "reasons": reasons,
                }
            )
        else:
            clean_options.append(
                Option(
                    title=opt.title,
                    description=opt.description,
                    next_steps=opt.next_steps,
                    chunk_ids=norm_cids,
                    supporting_quote=opt.supporting_quote,
                )
            )

    # Other side
    clean_other: list[OtherSideArg] = []
    for arg in llm_expl.other_side:
        norm_cids, reasons = claim_reasons(arg.argument, list(arg.chunk_ids), arg.supporting_quote)
        if reasons:
            removed.append(
                {
                    "item": f"other_side:{arg.argument[:40]}",
                    "text": arg.argument[:120],
                    "reasons": reasons,
                }
            )
        else:
            clean_other.append(
                OtherSideArg(
                    argument=arg.argument,
                    chunk_ids=norm_cids,
                    supporting_quote=arg.supporting_quote,
                )
            )

    # Evidence gaps / uncertainties: scan for uncited section numbers
    for entry in list(llm_expl.evidence_gaps) + list(llm_expl.uncertainties):
        for sec in _section_refs(entry):
            if _norm_section(sec) not in retrieved_sections:
                removed.append(
                    {
                        "item": "evidence_gap_or_uncertainty",
                        "text": entry[:120],
                        "reasons": [f"uncited_section:{sec}"],
                    }
                )

    cleaned = LLMExplanation(
        summary=summary,
        summary_chunk_ids=summary_ids,
        summary_supporting_quote=llm_expl.summary_supporting_quote if not s_reasons else "",
        options=clean_options,
        other_side=clean_other,
        evidence_gaps=list(llm_expl.evidence_gaps),
        uncertainties=list(llm_expl.uncertainties),
    )
    return cleaned, removed


# ---------------------------------------------------------------------------
# Case-law detection
# ---------------------------------------------------------------------------


_CASE_LAW_RE = re.compile(
    r"\b(supreme court|high court|judgment|judgement|case law|precedent|writ petition)\b",
    re.IGNORECASE,
)


def _looks_like_case_law_request(text: str) -> bool:
    return bool(_CASE_LAW_RE.search(text or ""))





# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def explain(
    case: CaseFile,
    today: date | None = None,
    llm_client: LLMClient | None = None,
    engine: LegalRAGEngine | None = None,
) -> Explanation:
    """Explain the user's legal position for their case.

    Returns a structured ``Explanation``. On abstain, ``reply_text`` carries
    the "not sure, consult a lawyer / NALSA 15100" message instead of an answer.
    """
    today = today or date.today()

    if llm_client is None:
        import os
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            from intake_agent import GeminiLLMClient
            llm_client = GeminiLLMClient(api_key=api_key)
        else:
            raise ValueError(
                "llm_client is required. Create one with:\n"
                "    from intake_agent import GeminiLLMClient\n"
                "    client = GeminiLLMClient(api_key='YOUR_GEMINI_API_KEY')\n"
                "    explain(case, today=today, llm_client=client)"
            )

    issue_type: IssueType = case.issue.primary  # type: ignore[assignment]
    cfg = get_config(issue_type)
    if cfg is None:
        return _make_abstain(
            case,
            issue_type,
            "unsupported_issue",
            today,
            detail=(
                f"I don't yet support the issue type '{issue_type}'. "
                f"Supported: security_deposit, unpaid_salary."
            ),
        )

    # --- State gating -------------------------------------------------------
    if cfg.supported_states and case.state not in cfg.supported_states:
        return _make_abstain(
            case,
            issue_type,
            "unsupported_state",
            today,
            detail=(
                f"I currently support {cfg.display_name} only in "
                f"{', '.join(cfg.supported_states)}. Your state ({case.state}) "
                "is not covered yet."
            ),
        )

    # --- Case-law request decline ------------------------------------------
    all_user_text = [
        case.user_goal_text or "",
        " ".join(case.issue.secondary_notes or []),
    ]
    if case.slots:
        for s in case.slots.values():
            if s.raw_quote:
                all_user_text.append(s.raw_quote)
            if isinstance(s.value, str):
                all_user_text.append(s.value)
    user_text = " ".join(filter(None, all_user_text))
    if _looks_like_case_law_request(user_text):
        return _make_abstain(
            case,
            issue_type,
            "case_law_request",
            today,
            detail=(
                "I can't cite or find Supreme Court / High Court judgments — "
                "that's outside what this tool covers. Please consult a lawyer."
            ),
            case_law_declined=True,
        )

    # --- Retrieve (filter by state + scope BEFORE ranking) -----------------
    engine = engine or LegalRAGEngine()
    retrieved, engine_flags = _retrieve(engine, case, cfg)

    if not retrieved:
        return _make_abstain(
            case,
            issue_type,
            "weak_retrieval",
            today,
            detail=(
                "I couldn't find any matching legal provisions in my corpus for "
                "your situation, so I can't give a grounded answer."
            ),
        )

    case_date = _case_date(case, cfg)

    # --- Legal-status awareness --------------------------------------------
    status_notes = _status_notes(retrieved, case_date)

    # --- Stale-label audit (report, never fix silently) --------------------
    data_quality_flags = _audit_stale_labels(retrieved)
    if issue_type == "unpaid_salary" and engine_flags.get("period_may_fall_under_repealed_acts"):
        data_quality_flags.append(
            "period_may_fall_under_repealed_acts: dispute date predates "
            "21-Nov-2025 Labour Codes commencement; legacy Acts may apply."
        )

    # --- Call the LLM with ONLY retrieved chunks ---------------------------
    prompt = _build_prompt(retrieved, case, cfg)
    llm_expl: LLMExplanation = llm_client.complete(prompt, LLMExplanation)  # type: ignore[assignment]

    # --- Citation validation (plain code, no LLM) --------------------------
    cleaned, removed_claims = _validate_claims(llm_expl, retrieved)

    # --- Abstain if too many claims fail validation ------------------------
    total_claims = (1 if llm_expl.summary else 0) + len(llm_expl.options) + len(llm_expl.other_side)
    valid_claims = (1 if cleaned.summary else 0) + len(cleaned.options) + len(cleaned.other_side)
    if removed_claims and valid_claims == 0:
        return _make_abstain(
            case,
            issue_type,
            "validation_failure",
            today,
            detail=(
                "The retrieved legal provisions did not support a reliable "
                "explanation, so I'd rather not guess."
            ),
            removed_claims=removed_claims,
            data_quality_flags=data_quality_flags,
        )
    if total_claims > 0 and (total_claims - valid_claims) / total_claims > 0.5:
        return _make_abstain(
            case,
            issue_type,
            "too_many_invalid_claims",
            today,
            detail=(
                "Too many legal claims could not be cited to the retrieved "
                "corpus, so I can't give a reliable answer."
            ),
            removed_claims=removed_claims,
            data_quality_flags=data_quality_flags,
        )

    # --- Limitation (deterministic, from corpus-backed config) -------------
    limitation_chunk_text = next(
        (c.get("exact_text", "") for c in retrieved if c["id"] == cfg.limitation.chunk_id),
        "",
    )
    limitation_result = compute_limitation(
        case, cfg, today=today, corpus_chunk_text=limitation_chunk_text
    )
    limitation_dict = limitation_result.model_dump()
    for k, v in list(limitation_dict.items()):
        if isinstance(v, date):
            limitation_dict[k] = v.isoformat()
    if "all_anchors" in limitation_dict:
        for item in limitation_dict["all_anchors"]:
            if isinstance(item, dict):
                for ak, av in list(item.items()):
                    if isinstance(av, date):
                        item[ak] = av.isoformat()

    # --- Assemble explanation ----------------------------------------------
    uncertainties = list(cleaned.uncertainties)
    uncertainties.extend(status_notes)

    if limitation_result.computable:
        if limitation_result.expired:
            uncertainties.append(
                f"Limitation: earliest deadline {limitation_result.deadline} appears to have "
                "passed. This may bar your claim — consult a lawyer immediately."
            )
        elif limitation_result.close:
            uncertainties.append(
                f"Limitation: earliest deadline {limitation_result.deadline} is close "
                f"({limitation_result.days_left} days left). Act promptly."
            )
        if limitation_result.is_arguable and limitation_result.assumption:
            uncertainties.append(f"Limitation: {limitation_result.assumption}")
        if not limitation_result.verified_against_corpus and limitation_result.corpus_note:
            uncertainties.append("Limitation: " + limitation_result.corpus_note)
    elif limitation_result.reason:
        uncertainties.append("Limitation: " + limitation_result.reason)

    if issue_type == "unpaid_salary" and engine_flags.get("period_may_fall_under_repealed_acts"):
        uncertainties.append(
            "Your dispute date predates 21 November 2025 (Labour Codes "
            "commencement). Legacy wage/employment laws may apply. "
            "Please consult a legal practitioner."
        )

    citations_used = sorted(
        {cid for c in cleaned.options for cid in c.chunk_ids}
        | set(cleaned.summary_chunk_ids)
        | {cid for a in cleaned.other_side for cid in a.chunk_ids}
    )

    raw_gaps = list(cleaned.evidence_gaps)
    evidence_gaps: list[str] = []
    s = case.slots or {}
    for gap in raw_gaps:
        low_g = gap.lower()
        # If user already explained key handover, don't repeat as gap
        if ("key" in low_g or "handover" in low_g) and s.get("possession_handed_over") and s["possession_handed_over"].status == "known":
            continue
        # If user already confirmed agreement type, don't repeat
        if ("agreement" in low_g or "contract" in low_g) and s.get("agreement_type") and s["agreement_type"].status == "known":
            continue
        evidence_gaps.append(gap)

    for key in ("employment_proof_available",):
        slot = s.get(key)
        if slot and getattr(slot, "status", None) in ("unknown", None):
            evidence_gaps.append(f"You have not confirmed: {key}.")

    reply_text = _assemble_reply(
        cleaned,
        uncertainty_list=uncertainties,
        limitation_result=limitation_result,
        abstain=False,
    )

    return Explanation(
        case_id=case.case_id,
        issue_type=issue_type,
        state=case.state,
        reply_text=reply_text,
        summary=cleaned.summary,
        summary_chunk_ids=cleaned.summary_chunk_ids,
        options=cleaned.options,
        other_side=cleaned.other_side,
        evidence_gaps=evidence_gaps,
        uncertainties=uncertainties,
        limitation=limitation_dict,
        abstain=False,
        citations_used=citations_used,
        removed_claims=removed_claims,
        data_quality_flags=data_quality_flags,
        case_law_declined=False,
    )


# ---------------------------------------------------------------------------
# Reply assembly & abstain constructor
# ---------------------------------------------------------------------------


def _assemble_reply(
    cleaned: LLMExplanation,
    uncertainty_list: list[str],
    limitation_result: LimitationResult,
    abstain: bool,
) -> str:
    parts: list[str] = []
    if abstain:
        parts.append(ABSTAIN_INTRO)

    # 1. Summary / Position
    if cleaned.summary:
        s = cleaned.summary.strip().rstrip(".") + "."
        parts.append(f"Your legal position: {s}")

    # 2. Options (with clear separation of law and practical steps)
    if cleaned.options:
        opt_lines = ["Your options:"]
        for i, opt in enumerate(cleaned.options, 1):
            desc = opt.description.strip().rstrip(".")
            steps = opt.next_steps.strip().rstrip(".")
            opt_lines.append(
                f"{i}. {opt.title} — What the law says: {desc}. Practical steps: {steps}."
            )
        parts.append(" ".join(opt_lines))

    # 3. Other side
    if cleaned.other_side:
        arg_lines = ["What the other side may argue:"]
        for i, arg in enumerate(cleaned.other_side, 1):
            a = arg.argument.strip().rstrip(".") + "."
            arg_lines.append(f"{i}. {a}")
        parts.append(" ".join(arg_lines))

    # 4. Evidence gaps
    if cleaned.evidence_gaps:
        parts.append("Documents you may need: " + "; ".join(cleaned.evidence_gaps).rstrip(".") + ".")

    # 5. Limitation breakdown
    if limitation_result.computable:
        lim_parts = []
        if limitation_result.warning:
            lim_parts.append(limitation_result.warning.rstrip(".") + ".")
        if limitation_result.anchor_event_label and limitation_result.anchor_date:
            lim_parts.append(
                f"Starting event used: {limitation_result.anchor_event_label} ({limitation_result.anchor_date.isoformat()})."
            )
        if limitation_result.assumption:
            lim_parts.append(f"Assumption: {limitation_result.assumption.rstrip('.') + '.'}")
        parts.append("Time limits: " + " ".join(lim_parts))

    # 6. Uncertainties & Escalate on arguable rules
    has_arguable = limitation_result.is_arguable or bool(uncertainty_list)
    if uncertainty_list:
        clean_u = [u.strip().rstrip(".") + "." for u in uncertainty_list if u.strip()]
        parts.append("Uncertainties to keep in mind: " + " ".join(clean_u))

    # Always recommend lawyer / NALSA if arguable or uncertain, even when abstain=False
    if abstain:
        parts.append(NALSA_MESSAGE)
    elif has_arguable:
        parts.append(
            "Because the starting date or legal application is contested, you should consult a qualified lawyer "
            "(or reach NALSA free legal aid at 15100) to confirm your exact deadlines before taking legal action."
        )

    # Clean up double periods or extra whitespace
    res = " ".join(p for p in parts if p)
    res = re.sub(r"\.\.+", ".", res)
    res = re.sub(r"\s+", " ", res).strip()
    return res


def _make_abstain(
    case: CaseFile,
    issue_type: IssueType,
    reason: str,
    today: date,
    detail: str | None = None,
    removed_claims: list[dict] | None = None,
    data_quality_flags: list[str] | None = None,
    case_law_declined: bool = False,
) -> Explanation:
    limitation_dict: dict[str, Any] = {}
    cfg = get_config(issue_type)
    if cfg:
        try:
            lr = compute_limitation(case, cfg, today=today)
            limitation_dict = lr.model_dump()
            for k in ("start_date", "deadline"):
                v = limitation_dict.get(k)
                if isinstance(v, date):
                    limitation_dict[k] = v.isoformat()
        except Exception:
            limitation_dict = {"computable": False}

    reply = _abstain_message(reason, detail)

    return Explanation(
        case_id=case.case_id,
        issue_type=issue_type,
        state=case.state,
        reply_text=reply,
        summary="",
        options=[],
        other_side=[],
        evidence_gaps=[],
        uncertainties=[detail] if detail else [],
        limitation=limitation_dict,
        abstain=True,
        abstain_reason=reason,
        citations_used=[],
        removed_claims=removed_claims or [],
        data_quality_flags=data_quality_flags or [],
        case_law_declined=case_law_declined,
    )


if __name__ == "__main__":
    class SmokeLLMClient(LLMClient):
        def complete(self, prompt: str, schema: type) -> LLMExplanation:
            return LLMExplanation(
                summary="You are owed salary under Section 17 of Code on Wages.",
                summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
                options=[
                    Option(
                        title="Claim before Authority under Section 45",
                        description="Recover wages with up to 10x compensation.",
                        next_steps="File claim.",
                        chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    )
                ],
                other_side=[
                    OtherSideArg(
                        argument="Employer may claim authorized deduction under Section 18.",
                        chunk_ids=["IND-FED-COW-2019-SEC-018"],
                    )
                ],
                evidence_gaps=["Appointment letter"],
                uncertainties=[],
            )

    demo_case = CaseFile(
        case_id="demo-unpaid-salary",
        language="en",
        state="Delhi",
        issue=Issue(primary="unpaid_salary", confidence=1.0),
        slots={
            "monthly_wage_inr": Slot(value=50000, status="known"),
            "unpaid_period_from": Slot(value="2026-01-01", status="known"),
            "amount_unpaid_inr": Slot(value=100000, status="known"),
            "still_employed": Slot(value=False, status="known"),
            "employment_end_date": Slot(value="2026-03-01", status="known"),
        },
    )
    result = explain(demo_case, today=date(2026, 11, 10), llm_client=SmokeLLMClient())
    print("Smoke test success! Abstain:", result.abstain)
    print("Summary:", result.summary)
    print("Options:", len(result.options))
    print("Limitation deadline:", result.limitation.get("deadline"))
    print("Reply preview:", result.reply_text[:120], "...")

