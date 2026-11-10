"""
Deterministic limitation-date arithmetic for the domain agent.

The limitation period and its provenance come from the corpus (via
``domain_config``), NEVER from the LLM. This module returns the deadline,
days left, and a close/expired warning.

Consumer complaints use the Consumer Protection Act's own deadline
(CPA 2019 s. 69: 2 years), never the Limitation Act, 1963.
"""

from __future__ import annotations

import re
from datetime import date
from typing import Any

from pydantic import BaseModel, Field

from case_schema import _d
from domain_config import IssueConfig, LimitationSpec

# Threshold (days) under which a deadline counts as "close" and warrants a warning.
CLOSE_THRESHOLD_DAYS = 30


class PlausibleAnchor(BaseModel):
    event: str
    event_label: str
    anchor_date: date
    deadline: date
    days_left: int
    rule_applied: str
    assumption: str
    chunk_id: str | None = None


class LimitationResult(BaseModel):
    computable: bool
    reason: str | None = None
    basis: str | None = None
    period_years: int | None = None
    chunk_id: str | None = None
    chunk_section: str | None = None
    anchor_event: str | None = None
    anchor_event_label: str | None = None
    anchor_date: date | None = None
    rule_applied: str | None = None
    assumption: str | None = None
    is_arguable: bool = False
    all_anchors: list[PlausibleAnchor] = Field(default_factory=list)
    conservative_deadline: date | None = None
    start_date: date | None = None
    deadline: date | None = None
    days_left: int | None = None
    expired: bool = False
    close: bool = False
    warning: str | None = None
    verified_against_corpus: bool = False
    corpus_note: str | None = None


_WORD_TO_NUM: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "twelve": 12,
    "thirty": 30,
}


def _parse_date(value: Any) -> date | None:
    if value is None:
        return None
    res = _d(value)
    if res:
        return res
    if isinstance(value, str):
        m = re.search(r"\b(\d{4}(?:-\d{2}(?:-\d{2})?)?)\b", value)
        if m:
            return _d(m.group(1))
    return None


def _add_years(d: date, years: int) -> date:
    """Add whole years, clamping Feb 29 -> Feb 28 in non-leap years."""
    try:
        return date(d.year + years, d.month, d.day)
    except ValueError:
        # Feb 29 on a non-leap target year
        return date(d.year + years, 3, 1)


def _extract_period_years(text: str) -> int | None:
    """Best-effort: find a stated period in years within corpus text."""
    # Check digit representation: e.g. "3 years", "2 year"
    m = re.search(r"\b(\d+)\s*years?\b", text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    # Check word representation: e.g. "Three years", "Two years"
    pattern = r"\b(" + "|".join(_WORD_TO_NUM.keys()) + r")\s*years?\b"
    m_word = re.search(pattern, text, re.IGNORECASE)
    if m_word:
        return _WORD_TO_NUM[m_word.group(1).lower()]
    return None


def compute_limitation(
    case,
    issue_config: IssueConfig,
    today: date | None = None,
    corpus_chunk_text: str | None = None,
) -> LimitationResult:
    """Compute the limitation deadline deterministically.

    Identifies plausible statutory starting events, computes the earliest
    (conservative) deadline to prevent time-bar risk, and explains assumptions.
    """
    today = today or date.today()
    spec = issue_config.limitation
    issue_type = issue_config.issue_type

    result = LimitationResult(
        computable=False,
        basis=spec.basis,
        period_years=spec.period_years,
        chunk_id=spec.chunk_id,
        chunk_section=spec.chunk_section,
    )

    all_anchors: list[PlausibleAnchor] = []
    oral_demand_note: str | None = None

    slots = case.slots or {}

    if issue_type == "security_deposit":
        # 1. Deposit payment date (Article 24: money received for plaintiff's use)
        d_paid_val = getattr(slots.get("deposit_paid_date"), "value", None)
        d_paid = _parse_date(d_paid_val)
        if d_paid:
            dl_paid = _add_years(d_paid, spec.period_years)
            all_anchors.append(
                PlausibleAnchor(
                    event="deposit_paid",
                    event_label="Date deposit was paid",
                    anchor_date=d_paid,
                    deadline=dl_paid,
                    days_left=(dl_paid - today).days,
                    rule_applied="Limitation Act, 1963 — Article 24 (money received for plaintiff's use: runs from date money received)",
                    assumption="Counts from when the deposit money was received by the landlord (strictest reading; earliest deadline).",
                    chunk_id="IND-FED-LIM-1963-ART-024",
                )
            )

        # 2. Tenancy end date (Article 47 / 113: failure of consideration / right to refund accrues upon vacating)
        d_end_val = getattr(slots.get("tenancy_end_date"), "value", None)
        d_end = _parse_date(d_end_val)
        if d_end:
            dl_end = _add_years(d_end, spec.period_years)
            all_anchors.append(
                PlausibleAnchor(
                    event="tenancy_ended",
                    event_label="Date moved out / tenancy ended",
                    anchor_date=d_end,
                    deadline=dl_end,
                    days_left=(dl_end - today).days,
                    rule_applied="Limitation Act, 1963 — Article 47 / Article 113 (right to refund accrues upon vacating)",
                    assumption="Counts from when the tenancy ended and the right to refund accrued.",
                    chunk_id="IND-FED-LIM-1963-ART-047",
                )
            )

        # 3. Demand date (Article 22: money deposited payable on demand)
        d_dem_val = getattr(slots.get("demand_made"), "value", None)
        d_dem = _parse_date(d_dem_val)
        if d_dem:
            dl_dem = _add_years(d_dem, spec.period_years)
            all_anchors.append(
                PlausibleAnchor(
                    event="demand_made",
                    event_label="Date demand was made",
                    anchor_date=d_dem,
                    deadline=dl_dem,
                    days_left=(dl_dem - today).days,
                    rule_applied="Limitation Act, 1963 — Article 22 (money deposited payable on demand)",
                    assumption="Counts from when demand was made, if the agreement makes the refund payable on demand.",
                    chunk_id="IND-FED-LIM-1963-ART-022",
                )
            )
        elif d_dem_val:
            s_dem = str(d_dem_val).strip()
            if any(w in s_dem.lower() for w in ("call", "phone", "asked", "weekly", "spoke", "message", "whatsapp")):
                oral_demand_note = (
                    f"Notice regarding demand: You mentioned contacting the landlord ('{s_dem}'). "
                    "Under Article 22, oral or informal demands may already have started the time limit running. "
                    "Do NOT assume the timeline only begins when a formal legal notice is served."
                )

    elif issue_type == "unpaid_salary":
        # 1. Unpaid period start (Article 7: wages run from when wages accrue)
        d_from_val = getattr(slots.get("unpaid_period_from"), "value", None)
        d_from = _parse_date(d_from_val)
        if d_from:
            dl_from = _add_years(d_from, spec.period_years)
            all_anchors.append(
                PlausibleAnchor(
                    event="unpaid_period_from",
                    event_label="Start of unpaid wage period",
                    anchor_date=d_from,
                    deadline=dl_from,
                    days_left=(dl_from - today).days,
                    rule_applied="Limitation Act, 1963 — Article 7 (wages: runs from when wages accrue)",
                    assumption="Counts from earliest unpaid wage period (limitation runs separately for each wage cycle).",
                    chunk_id="IND-FED-LIM-1963-ART-007",
                )
            )

        # 2. Employment end date (Code on Wages Section 17 / Article 7)
        d_end_val = getattr(slots.get("employment_end_date"), "value", None)
        if not d_end_val:
            d_end_val = getattr(slots.get("unpaid_period_to"), "value", None)
        d_end = _parse_date(d_end_val)
        if d_end:
            dl_end = _add_years(d_end, spec.period_years)
            all_anchors.append(
                PlausibleAnchor(
                    event="employment_ended",
                    event_label="Date employment ended / resignation",
                    anchor_date=d_end,
                    deadline=dl_end,
                    days_left=(dl_end - today).days,
                    rule_applied="Code on Wages, 2019 — Section 17 / Limitation Act Article 7",
                    assumption="Wages payable within two working days of removal or resignation under Section 17.",
                    chunk_id="IND-FED-COW-2019-SEC-017",
                )
            )

    # Fallback to configured start_slot / fallback_slot if domain-specific scanning found nothing
    if not all_anchors:
        start_value = None
        if spec.start_slot in slots:
            val = getattr(slots[spec.start_slot], "value", None)
            if _parse_date(val) is not None:
                start_value = val
        if start_value is None and spec.fallback_slot and spec.fallback_slot in slots:
            slot2 = slots.get(spec.fallback_slot)
            if slot2:
                val = getattr(slot2, "value", None)
                if _parse_date(val) is not None:
                    start_value = val

        start_date = _parse_date(start_value) if start_value else None
        if start_date:
            dl = _add_years(start_date, spec.period_years)
            all_anchors.append(
                PlausibleAnchor(
                    event=spec.start_slot,
                    event_label=spec.start_slot.replace("_", " ").title(),
                    anchor_date=start_date,
                    deadline=dl,
                    days_left=(dl - today).days,
                    rule_applied=f"{spec.basis.replace('_', ' ').title()} — {spec.chunk_section}",
                    assumption=f"Based on {spec.start_slot}.",
                    chunk_id=spec.chunk_id,
                )
            )

    if not all_anchors:
        result.reason = (
            f"limitation start not computable: slot '{spec.start_slot}' "
            "has no parseable date"
        )
        return result

    # Sort anchors ascending by deadline: earliest is the conservative deadline
    all_anchors.sort(key=lambda a: a.deadline)
    earliest = all_anchors[0]

    result.anchor_event = earliest.event
    result.anchor_event_label = earliest.event_label
    result.anchor_date = earliest.anchor_date
    result.start_date = earliest.anchor_date
    result.rule_applied = earliest.rule_applied
    result.chunk_id = earliest.chunk_id or spec.chunk_id
    result.conservative_deadline = earliest.deadline
    result.deadline = earliest.deadline
    result.days_left = earliest.days_left
    result.expired = result.days_left < 0
    result.close = (not result.expired) and result.days_left <= CLOSE_THRESHOLD_DAYS
    result.all_anchors = all_anchors
    result.is_arguable = (len(all_anchors) > 1) or bool(oral_demand_note)

    if len(all_anchors) > 1:
        latest = all_anchors[-1]
        result.assumption = (
            f"Calculated using the earliest plausible starting event: {earliest.event_label} ({earliest.anchor_date.isoformat()}). "
            f"If counted from {latest.event_label} ({latest.anchor_date.isoformat()}), the deadline would be {latest.deadline.isoformat()}. "
            "Because the starting trigger date is contested under Indian contract and limitation law (date of payment vs date of vacating vs date of demand), "
            f"you should rely on the earlier date ({earliest.deadline.isoformat()}) to avoid being time-barred. "
            "This is an estimate only; confirm with a qualified lawyer. Act early and never delay."
        )
    else:
        result.assumption = (
            f"Calculated from {earliest.event_label} ({earliest.anchor_date.isoformat()}) under {earliest.rule_applied}. "
            "This is an estimate only; confirm with a qualified lawyer. Act early and never delay."
        )

    if oral_demand_note:
        result.assumption += f" {oral_demand_note}"

    # Corpus verification
    verified = False
    corpus_note = None
    if corpus_chunk_text:
        stated = _extract_period_years(corpus_chunk_text)
        if stated is not None and stated == spec.period_years:
            verified = True
        elif stated is not None:
            corpus_note = (
                f"corpus chunk {spec.chunk_id} states {stated} year(s), "
                f"which differs from configured {spec.period_years} years"
            )
        else:
            corpus_note = (
                f"corpus chunk {spec.chunk_id} did not state a clear year period"
            )
    result.verified_against_corpus = verified
    result.corpus_note = corpus_note

    # Warning message (labeled estimate, urges early action)
    if result.expired:
        result.warning = (
            f"Limitation warning: Earliest estimated deadline ({result.deadline.isoformat()}) appears to have passed "
            f"based on {earliest.event_label}. This may bar your claim. Consult a lawyer immediately."
        )
    elif result.close:
        result.warning = (
            f"Limitation warning: Earliest estimated deadline is close: {result.deadline.isoformat()} "
            f"({result.days_left} days left based on {earliest.event_label}). Act promptly — do not delay. "
            "Estimate only; confirm with a lawyer."
        )
    else:
        result.warning = (
            f"Limitation estimate: Conservative deadline is {result.deadline.isoformat()} "
            f"({result.days_left} days left based on {earliest.event_label}). "
            "Estimate only; confirm with a lawyer. Act early — do not wait until the deadline."
        )

    result.computable = True
    result.reason = None
    return result


def consumer_protection_deadline_info() -> dict[str, Any]:
    """CPA 2019 s. 69: two years from cause of action (consumer complaints).

    Kept separate from the Limitation Act per product requirement:
    consumer complaints use the CPA's own deadline, never the Limitation Act.
    """
    return {
        "basis": "consumer_protection_act",
        "period_years": 2,
        "chunk_id": "IND-FED-CPA-2019-SEC-069",
        "chunk_section": "Consumer Protection Act, 2019 — Section 69",
        "note": "Consumer complaints use the CPA's own two-year deadline, not the Limitation Act, 1963.",
    }
