"""Tests for the intake agent with mocked LLM output."""

from datetime import date

import pytest

from case_schema import CaseFile, Slot, Issue, Risk
from intake_agent import (
    Extraction,
    LLMClient,
    RiskIndicators,
    SlotFill,
    process_turn,
)

TODAY = date(2026, 11, 10)


class FakeLLMClient(LLMClient):
    def __init__(self, extraction: Extraction):
        self.extraction = extraction

    def complete(self, prompt: str, schema: type) -> Extraction:
        return self.extraction


def make_case(primary="security_deposit", state="Delhi", slots=None, language="en"):
    case = CaseFile(case_id="t", language=language, state=state,
                    issue=Issue(primary=primary, confidence=0.9))
    if slots:
        case.slots = {k: Slot(value=v, status="known") for k, v in slots.items()}
    return case


def make_extraction(primary="security_deposit", conf=0.9, state=None,
                    risk=None, slot_fills=None, detected_language="en",
                    notice_received=False, notice_sender=None, notice_claims=None,
                    notice_demanded_amount=None, notice_reply_deadline=None,
                    amounts=None):
    return Extraction(
        primary_issue=primary,
        issue_confidence=conf,
        secondary_issues=[],
        state=state,
        city=None,
        user_role=None,
        slot_fills=[SlotFill(**f) for f in (slot_fills or [])],
        parties=[],
        timeline=[],
        amounts=amounts or [],
        evidence=[],
        risk=RiskIndicators(**(risk or {})),
        notice_received=notice_received,
        notice_sender=notice_sender,
        notice_claims=notice_claims,
        notice_demanded_amount=notice_demanded_amount,
        notice_reply_deadline=notice_reply_deadline,
        detected_language=detected_language,
        summary="",
    )


def run(case, user_message, extraction=None, today=TODAY):
    client = FakeLLMClient(extraction) if extraction else FakeLLMClient(make_extraction())
    return process_turn(case, user_message, today=today, llm_client=client)


# --------------------------------------------------------------------------
# 1. Ready case
# --------------------------------------------------------------------------
def test_ready_case():
    case = make_case(
        state="Delhi",
        slots={
            "property_type": "residential",
            "deposit_amount_inr": 50000,
            "deposit_paid_date": "2024-03",
            "agreement_type": "written registered",
            "tenancy_end_date": "2025-12-31",
            "possession_handed_over": "yes",
            "landlord_reason_for_withholding": "none",
            "demand_made": "yes via WhatsApp",
        },
    )
    res = run(case, "All details given.",
              extraction=make_extraction(primary="security_deposit", state="Delhi"))
    assert res.verdict == "ready"
    assert res.missing_required == []
    assert res.asked_questions == []
    assert "I have enough information" in res.reply_text


# --------------------------------------------------------------------------
# 2. Not ready with missing slots (asks up to 3, priority order)
# --------------------------------------------------------------------------
def test_not_ready_missing_slots():
    case = make_case(state="Delhi")
    res = run(case, "My landlord won't return my deposit.",
              extraction=make_extraction(primary="security_deposit", state="Delhi"))
    assert res.verdict == "not_ready"
    assert len(res.asked_questions) <= 3
    # first required slot in registry is property_type
    assert res.asked_questions[0] == "property_type"
    assert "property_type" in res.missing_required
    assert "I don't know" in res.reply_text


# --------------------------------------------------------------------------
# 3. Escalation triggers (each one)
# --------------------------------------------------------------------------
def test_escalation_police_or_arrest():
    case = make_case(state="Delhi")
    res = run(case, "The landlord threatened to call the police.",
              extraction=make_extraction(
                  primary="security_deposit", state="Delhi",
                  risk={"police_or_arrest": True},
              ))
    assert res.verdict == "escalate"
    assert "police_or_arrest" in res.escalation_reasons
    assert "15100" in res.reply_text


def test_escalation_threats_or_violence():
    case = make_case(state="Delhi")
    res = run(case, "He threatened to beat me.",
              extraction=make_extraction(
                  primary="security_deposit", state="Delhi",
                  risk={"threats_or_violence": True},
              ))
    assert res.verdict == "escalate"
    assert "threats_or_violence" in res.escalation_reasons


def test_escalation_domestic_violence():
    case = make_case(state="Delhi")
    res = run(case, "Husband harassment at home.",
              extraction=make_extraction(
                  primary="security_deposit", state="Delhi",
                  risk={"domestic_violence": True},
              ))
    assert res.verdict == "escalate"
    assert "domestic_violence" in res.escalation_reasons


def test_escalation_court_date_within_7_days():
    case = make_case(state="Delhi")
    res = run(case, "I have a court hearing soon.",
              extraction=make_extraction(
                  primary="security_deposit", state="Delhi",
                  risk={"court_summons_or_hearing_date": "2026-11-12"},  # 2 days away
              ))
    assert res.verdict == "escalate"
    assert any("court_date" in r for r in res.escalation_reasons)


def test_escalation_notice_deadline_passed():
    case = make_case(state="Delhi")
    res = run(case, "I got a legal notice.",
              extraction=make_extraction(
                  primary="security_deposit", state="Delhi",
                  risk={"notice_reply_deadline": "2026-11-05"},  # already passed
                  notice_reply_deadline="2026-11-05",
              ))
    assert res.verdict == "escalate"
    assert any("notice_deadline" in r for r in res.escalation_reasons)


def test_escalation_out_of_scope_issue():
    case = make_case(state="Delhi")
    res = run(case, "I have a criminal defence problem.",
              extraction=make_extraction(primary="other", state="Delhi"))
    assert res.verdict == "escalate"
    assert "out_of_scope_issue" in res.escalation_reasons


def test_escalation_unsupported_state_for_rent():
    case = make_case(primary="security_deposit", state="West Bengal")
    res = run(case, "Deposit issue in Kolkata.",
              extraction=make_extraction(primary="security_deposit", state="West Bengal"))
    assert res.verdict == "escalate"
    assert "unsupported_state_for_rent" in res.escalation_reasons


# --------------------------------------------------------------------------
# 4. Language stays English (English-only mode)
# --------------------------------------------------------------------------
def test_language_stays_english():
    case = make_case(state="Delhi", language="en")
    res = run(case, "My landlord won't return my deposit.",
              extraction=make_extraction(
                  primary="security_deposit", state="Delhi",
                  detected_language="en",
              ))
    assert res.case.language == "en"
    assert res.verdict == "not_ready"


# --------------------------------------------------------------------------
# 5. User refuses a slot: stops re-asking after MAX_ASKS_PER_SLOT
# --------------------------------------------------------------------------
def test_refusal_slot_stops_reasking():
    case = make_case(state="Delhi")
    extraction = make_extraction(primary="security_deposit", state="Delhi")
    # Turn 1: property_type asked (asked_count 0 -> 1)
    r1 = run(case, "I won't say.", extraction=extraction)
    assert r1.verdict == "not_ready"
    assert "property_type" in r1.asked_questions
    assert case.slots["property_type"].asked_count == 1
    # Turn 2: still refused, asked again (1 -> 2)
    r2 = run(case, "Still not telling you.", extraction=extraction)
    assert r2.verdict == "not_ready"
    assert "property_type" in r2.asked_questions
    assert case.slots["property_type"].asked_count == 2
    # Turn 3: MAX reached -> no longer asked, no longer blocking
    r3 = run(case, "I refuse.", extraction=extraction)
    assert r3.verdict == "not_ready"
    assert "property_type" not in r3.asked_questions
    assert case.slots["property_type"].asked_count == 2
    assert "property_type" not in r3.missing_required


# --------------------------------------------------------------------------
# 6. English message with police threat caught by keyword safety net
#    (even if the LLM misses the extraction)
# --------------------------------------------------------------------------
def test_english_police_threat_keyword_net():
    case = make_case(state="Delhi")
    # LLM returns NO risk (missed it), but English text contains police + arrest
    res = run(case, "The police are threatening to arrest me.",
              extraction=make_extraction(
                  primary="security_deposit", state="Delhi", risk={},
              ))
    assert res.verdict == "escalate"
    assert "police_or_arrest" in res.escalation_reasons
    assert "15100" in res.reply_text


# --------------------------------------------------------------------------
# 7. Security deposit with amount + duration -> not_ready (asks for state)
# --------------------------------------------------------------------------
def test_security_deposit_not_ready_asks_state():
    """'landlord has 20,000 of my security deposit for 30 days' -> not_ready."""
    case = make_case(state=None)
    res = run(case, "The landlord has 20,000 of my security deposit for 30 days.",
              extraction=make_extraction(
                  primary="security_deposit", state=None,
                  slot_fills=[{"key": "deposit_amount_inr", "value": 20000, "confidence": 0.9}],
              ))
    assert res.verdict == "not_ready"
    assert "state" in res.missing_required
    assert len(res.asked_questions) <= 3


# --------------------------------------------------------------------------
# 8. Out-of-scope (divorce) with high confidence -> escalate / referral
# --------------------------------------------------------------------------
def test_out_of_scope_divorce_escalate_referral():
    """Divorce question -> primary='other', confidence>=0.6 -> escalate/referral."""
    case = make_case(state="Delhi")
    res = run(case, "I want to file for divorce from my spouse.",
              extraction=make_extraction(
                  primary="other", state="Delhi",
                  conf=0.9,
              ))
    assert res.verdict == "escalate"
    assert "out_of_scope_issue" in res.escalation_reasons
    assert res.severity == "referral"
    assert "can't help with this type" in res.reply_text
    assert "15100" in res.reply_text


# --------------------------------------------------------------------------
# 9. 'other' with low confidence (< 0.6) -> NOT escalated, falls to not_ready
# --------------------------------------------------------------------------
def test_other_low_confidence_not_escalated():
    """primary='other' but confidence=0.3 -> not escalated, treated as not_ready."""
    case = make_case(state=None)
    res = run(case, "Something legal is happening but I'm not sure what.",
              extraction=make_extraction(
                  primary="other", state=None,
                  conf=0.3,
              ))
    assert res.verdict == "not_ready"
    assert "out_of_scope_issue" not in res.escalation_reasons
    assert "state" in res.missing_required


# --------------------------------------------------------------------------
# 10. User deposit message recovery & state prioritization
# --------------------------------------------------------------------------
def test_user_deposit_message_recovery_and_state_prioritization():
    """'lawyer, landlord has 20,000 of my security...' classifies as security_deposit and asks state first."""
    case = make_case(state=None, slots=None)
    res = run(
        case,
        "lawyer, landlord has 20,000 of my security and is not returning it from past 30 days",
        extraction=make_extraction(
            primary="other",  # Even if LLM originally returned 'other'
            state=None,
            slot_fills=[{"key": "deposit_amount_inr", "value": 20000, "confidence": 1.0}],
        ),
    )
    assert res.verdict == "not_ready"
    assert res.case.issue.primary == "security_deposit"
    assert "state" in res.asked_questions
    assert res.asked_questions[0] == "state"


# --------------------------------------------------------------------------
# 11. Multi-turn slot absorption without repeating loops
# --------------------------------------------------------------------------
def test_multiturn_intake_absorption_no_loop():
    """Verify slots are absorbed across turns and not asked repeatedly."""
    case = CaseFile(case_id="multi-turn-test", language="en")

    class MultiTurnLLM(LLMClient):
        def complete(self, prompt, schema):
            if "30,000 to my room owner" in prompt:
                return make_extraction(
                    primary="security_deposit",
                    state=None,
                    amounts=[{"label": "security deposit", "value_inr": 30000}],
                    slot_fills=[{"key": "deposit_amount_inr", "value": 30000, "confidence": 1.0}],
                )
            else:
                return make_extraction(
                    primary="security_deposit",
                    state="Karnataka",
                    slot_fills=[
                        {"key": "property_type", "value": "residential", "confidence": 1.0},
                        {"key": "deposit_amount_inr", "value": 30000, "confidence": 1.0},
                        {"key": "tenancy_end_date", "value": "40 days since i left the room", "confidence": 1.0},
                    ],
                )

    # Turn 1
    t1 = process_turn(
        case,
        "i paid 30,000 to my room owner as security deposit but it has been many days he has not returned it",
        today=TODAY,
        llm_client=MultiTurnLLM(),
    )
    assert t1.verdict == "not_ready"
    assert case.slots["deposit_amount_inr"].value == 30000
    assert "deposit_amount_inr" not in t1.asked_questions
    assert t1.asked_questions == ["state", "property_type", "deposit_paid_date"]

    # Turn 2
    t2 = process_turn(
        case,
        "Karnataka 2) residential 3)30000 . it has been 40 days since i left the room",
        today=TODAY,
        llm_client=MultiTurnLLM(),
    )
    assert t2.verdict == "not_ready"
    assert case.state == "Karnataka"
    assert case.slots["property_type"].value == "residential"
    assert case.slots["tenancy_end_date"].value == "2026-10-01"
    # Verify no loop: previously answered questions are NOT asked again
    assert "state" not in t2.asked_questions
    assert "property_type" not in t2.asked_questions
    assert "deposit_amount_inr" not in t2.asked_questions
    assert t2.asked_questions == ["deposit_paid_date", "agreement_type", "possession_handed_over"]


