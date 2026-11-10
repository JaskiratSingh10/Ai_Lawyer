"""Tests for the domain (explain) agent with mocked LLM output."""

from datetime import date
from typing import Any

import pytest

from case_schema import CaseFile, Issue, Slot
from corpus.corpus_rag_engine import LegalRAGEngine
from domain_agent import (
    Explanation,
    LLMExplanation,
    Option,
    OtherSideArg,
    explain,
)
from intake_agent import LLMClient
from limitation import consumer_protection_deadline_info

TODAY = date(2026, 11, 10)


class FakeDomainLLMClient(LLMClient):
    def __init__(self, explanation: LLMExplanation):
        self.explanation = explanation
        self.last_prompt: str | None = None

    def complete(self, prompt: str, schema: type) -> LLMExplanation:
        self.last_prompt = prompt
        return self.explanation


def make_salary_case(
    state: str = "Delhi",
    slots: dict[str, Any] | None = None,
    user_goal_text: str | None = None,
) -> CaseFile:
    default_slots = {
        "monthly_wage_inr": Slot(value=50000, status="known"),
        "unpaid_period_from": Slot(value="2026-01-01", status="known"),
        "unpaid_period_to": Slot(value="2026-03-01", status="known"),
        "amount_unpaid_inr": Slot(value=100000, status="known"),
        "still_employed": Slot(value=False, status="known"),
        "employment_end_date": Slot(value="2026-03-01", status="known"),
        "demand_made": Slot(value="2026-03-05", status="known"),
        "employment_proof_available": Slot(value="yes", status="known"),
    }
    if slots:
        default_slots.update({k: Slot(value=v, status="known") for k, v in slots.items()})

    return CaseFile(
        case_id="salary-test-1",
        language="en",
        state=state,
        issue=Issue(primary="unpaid_salary", confidence=1.0),
        user_goal_text=user_goal_text,
        slots=default_slots,
    )


def make_deposit_case(
    state: str = "Delhi",
    slots: dict[str, Any] | None = None,
    user_goal_text: str | None = None,
) -> CaseFile:
    default_slots = {
        "property_type": Slot(value="residential", status="known"),
        "deposit_amount_inr": Slot(value=60000, status="known"),
        "deposit_paid_date": Slot(value="2024-03-01", status="known"),
        "tenancy_end_date": Slot(value="2026-01-01", status="known"),
        "possession_handed_over": Slot(value="yes", status="known"),
        "landlord_reason_for_withholding": Slot(value="repairs", status="known"),
        "demand_made": Slot(value="2026-01-15", status="known"),
    }
    if slots:
        default_slots.update({k: Slot(value=v, status="known") for k, v in slots.items()})

    return CaseFile(
        case_id="deposit-test-1",
        language="en",
        state=state,
        issue=Issue(primary="security_deposit", confidence=1.0),
        user_goal_text=user_goal_text,
        slots=default_slots,
    )


# --------------------------------------------------------------------------
# 1. A good cited answer
# --------------------------------------------------------------------------
def test_good_cited_answer():
    case = make_salary_case()
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary=(
                "You are owed unpaid salary of 100000 INR. Under Section 17 of the "
                "Code on Wages, 2019, earned wages must be disbursed within two working "
                "days following resignation or removal."
            ),
            summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
            summary_supporting_quote="pay or cause to be paid wages",
            options=[
                Option(
                    title="File a claim before the Authority under Section 45",
                    description=(
                        "You can file an application before the appointed Authority under "
                        "the Code on Wages to recover your wages with compensation up to ten times."
                    ),
                    next_steps="Gather your appointment letter, bank statements, and written demand.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                )
            ],
            other_side=[
                OtherSideArg(
                    argument=(
                        "The employer may contend that deductions were made lawfully under Section 18 "
                        "or for absence from duty."
                    ),
                    chunk_ids=["IND-FED-COW-2019-SEC-018"],
                    supporting_quote="there shall be no deductions from the wages",
                )
            ],
            evidence_gaps=["Formal resignation acceptance letter"],
            uncertainties=["Whether employer maintains an exempt status"],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    assert res.abstain_reason is None
    assert "You are owed unpaid salary" in res.summary
    assert len(res.options) == 1
    assert res.options[0].title == "File a claim before the Authority under Section 45"
    assert len(res.other_side) == 1
    assert res.removed_claims == []
    assert "IND-FED-COW-2019-SEC-017" in res.citations_used
    assert "IND-FED-COW-2019-SEC-045" in res.citations_used
    assert "IND-FED-COW-2019-SEC-018" in res.citations_used
    assert res.limitation["computable"] is True
    assert res.limitation["verified_against_corpus"] is True
    assert res.limitation["period_years"] == 3


# --------------------------------------------------------------------------
# 2. An uncited claim being dropped
# --------------------------------------------------------------------------
def test_uncited_claim_dropped():
    case = make_salary_case()
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="You have a valid claim for unpaid salary.",
            summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
            summary_supporting_quote="pay or cause to be paid wages",
            options=[
                Option(
                    title="Formal claim before Authority",
                    description="Claim under Section 45 before the Authority.",
                    next_steps="File claim form.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                ),
                Option(
                    title="Uncited Option With No Backing",
                    description="You can demand an automatic police raid on the office.",
                    next_steps="Go to police station.",
                    chunk_ids=[],  # Uncited claim!
                    supporting_quote="",
                ),
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    # Valid claims remain (summary + 1 option), so do not abstain, but drop the uncited option
    assert res.abstain is False
    assert len(res.options) == 1
    assert res.options[0].title == "Formal claim before Authority"
    assert len(res.removed_claims) == 1
    assert res.removed_claims[0]["item"] == "option:Uncited Option With No Backing"
    assert "uncited_claim" in res.removed_claims[0]["reasons"]


# --------------------------------------------------------------------------
# 3. A fake section number being caught
# --------------------------------------------------------------------------
def test_fake_section_caught():
    case = make_salary_case()
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="You have a valid claim for unpaid wages.",
            summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
            summary_supporting_quote="pay or cause to be paid wages",
            options=[
                Option(
                    title="Real option",
                    description="Claim under Section 45 before the Authority.",
                    next_steps="File application.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                ),
                Option(
                    title="Hallucinated section option",
                    description="Under Section 999 of the Labour Act, you get automatic triple damages.",
                    next_steps="Demand triple damages.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                ),
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    assert len(res.options) == 1
    assert res.options[0].title == "Real option"
    assert len(res.removed_claims) == 1
    assert res.removed_claims[0]["item"] == "option:Hallucinated section option"
    assert any("uncited_section:999" in r for r in res.removed_claims[0]["reasons"])


# --------------------------------------------------------------------------
# 4. Abstain on weak retrieval
# --------------------------------------------------------------------------
def test_abstain_on_weak_retrieval():
    case = make_salary_case()

    class EmptyRetrievalEngine:
        def search(self, *args, **kwargs):
            return {"results": [], "flags": {}}

    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Summary here.",
            summary_chunk_ids=[],
            options=[],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm, engine=EmptyRetrievalEngine())

    assert res.abstain is True
    assert res.abstain_reason == "weak_retrieval"
    assert "I'm not sure about this — please consult a qualified lawyer." in res.reply_text
    assert "15100" in res.reply_text
    assert res.summary == ""
    assert res.options == []


# --------------------------------------------------------------------------
# 5. Abstain on unsupported state
# --------------------------------------------------------------------------
def test_abstain_on_unsupported_state():
    # Rent laws only support Delhi, Maharashtra, Karnataka, Tamil Nadu
    case = make_deposit_case(state="Kerala")
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Should not be called.",
            summary_chunk_ids=[],
            options=[],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is True
    assert res.abstain_reason == "unsupported_state"
    assert "Kerala" in res.reply_text
    assert "15100" in res.reply_text
    assert "I'm not sure" in res.reply_text


# --------------------------------------------------------------------------
# 6. Limitation near-expiry warning
# --------------------------------------------------------------------------
def test_limitation_near_expiry():
    # Start date 2 years and 11 months before today (today is 2026-11-10)
    # Start date 2023-11-25 -> 3-year deadline is 2026-11-25 (15 days away, <= 30)
    case = make_salary_case(
        slots={"unpaid_period_from": "2023-11-25"}
    )
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Salary is unpaid.",
            summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
            summary_supporting_quote="pay or cause to be paid wages",
            options=[
                Option(
                    title="Claim wages",
                    description="Claim under Section 45.",
                    next_steps="File claim.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                )
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    assert res.limitation["computable"] is True
    assert res.limitation["close"] is True
    assert res.limitation["expired"] is False
    assert res.limitation["days_left"] == 15
    assert "close" in res.limitation["warning"].lower()
    assert any("close" in u.lower() and "15 days" in u.lower() for u in res.uncertainties)
    assert "close" in res.reply_text.lower()


# --------------------------------------------------------------------------
# 7. Pre-Code wage dates raising uncertainty note
# --------------------------------------------------------------------------
def test_pre_code_wage_dates_raising_uncertainty():
    # Wages unpaid from June 2025 (predates 21 November 2025)
    case = make_salary_case(
        slots={"unpaid_period_from": "2025-06-01"}
    )
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Pre-Code wages dispute.",
            summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
            summary_supporting_quote="pay or cause to be paid wages",
            options=[
                Option(
                    title="Claim under Code on Wages Section 45",
                    description="Apply before the Authority.",
                    next_steps="File claim.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                )
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    assert any("21 November 2025" in u or "predates" in u or "legacy" in u for u in res.uncertainties)
    assert any("period_may_fall_under_repealed_acts" in f for f in res.data_quality_flags)
    assert any("consult a lawyer" in u.lower() or "consult a legal practitioner" in u.lower() for u in res.uncertainties)


# --------------------------------------------------------------------------
# 8. "Which Supreme Court case supports me?" being declined
# --------------------------------------------------------------------------
def test_supreme_court_case_declined():
    case = make_salary_case(
        user_goal_text="Which Supreme Court case supports me in recovering my unpaid salary?"
    )
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Should not be called.",
            summary_chunk_ids=[],
            options=[],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is True
    assert res.case_law_declined is True
    assert res.abstain_reason == "case_law_request"
    assert "Supreme Court" in res.reply_text or "judgments" in res.reply_text
    assert "15100" in res.reply_text
    assert "I'm not sure" in res.reply_text


# --------------------------------------------------------------------------
# 9. Stale "Pending Notification" label flagged in data_quality_flags
# --------------------------------------------------------------------------
def test_stale_label_audit_flagged():
    case = make_salary_case()

    class StaleLabelMockEngine:
        def __init__(self):
            self._real = LegalRAGEngine()

        def search(self, *args, **kwargs):
            out = self._real.search(*args, **kwargs)
            # Inject a chunk carrying a stale note
            if out.get("results"):
                for r in out["results"]:
                    if "COW-2019" in r["id"]:
                        r["legal_status_notes"] = "Substantively Pending Notification in official gazette."
            return out

    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="You are owed wages.",
            summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
            summary_supporting_quote="pay or cause to be paid wages",
            options=[
                Option(
                    title="Claim wages",
                    description="Claim under Section 45.",
                    next_steps="File claim.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                )
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm, engine=StaleLabelMockEngine())

    assert any("STALE_LABEL" in f and "pending" in f.lower() for f in res.data_quality_flags)


# --------------------------------------------------------------------------
# 10. Limitation expired warning
# --------------------------------------------------------------------------
def test_limitation_expired():
    # Start date 2020-01-01 -> 3-year deadline 2023-01-01 -> expired relative to TODAY (2026-11-10)
    case = make_salary_case(
        slots={"unpaid_period_from": "2020-01-01"}
    )
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Wages from 2020.",
            summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
            summary_supporting_quote="pay or cause to be paid wages",
            options=[
                Option(
                    title="Claim",
                    description="Claim under Section 45.",
                    next_steps="File claim.",
                    chunk_ids=["IND-FED-COW-2019-SEC-045"],
                    supporting_quote="appoint one or more authorities",
                )
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.limitation["computable"] is True
    assert res.limitation["expired"] is True
    assert res.limitation["days_left"] < 0
    assert "passed" in res.limitation["warning"].lower()
    assert any("passed" in u.lower() for u in res.uncertainties)


# --------------------------------------------------------------------------
# 11. Too many invalid claims leads to abstain
# --------------------------------------------------------------------------
def test_too_many_invalid_claims_abstain():
    case = make_salary_case()
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Uncited summary.",
            summary_chunk_ids=["FAKE-CHUNK-ID-1"],
            summary_supporting_quote="fake quote",
            options=[
                Option(
                    title="Fake 1",
                    description="Fake claim 1",
                    next_steps="steps",
                    chunk_ids=["FAKE-CHUNK-ID-2"],
                    supporting_quote="fake quote",
                ),
                Option(
                    title="Fake 2",
                    description="Fake claim 2",
                    next_steps="steps",
                    chunk_ids=["FAKE-CHUNK-ID-3"],
                    supporting_quote="fake quote",
                ),
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is True
    assert res.abstain_reason in ("validation_failure", "too_many_invalid_claims")
    assert "15100" in res.reply_text
    assert "I'm not sure" in res.reply_text


# --------------------------------------------------------------------------
# 12. Consumer Protection Act deadline (CPA 2019 s. 69: 2 years, not Limitation Act)
# --------------------------------------------------------------------------
def test_consumer_protection_deadline_info():
    cpa_info = consumer_protection_deadline_info()
    assert cpa_info["basis"] == "consumer_protection_act"
    assert cpa_info["period_years"] == 2
    assert cpa_info["chunk_id"] == "IND-FED-CPA-2019-SEC-069"
    assert "Section 69" in cpa_info["chunk_section"]


# --------------------------------------------------------------------------
# 13. Tamil Nadu security deposit: statutory 3-month cap retrieved
# --------------------------------------------------------------------------
def test_security_deposit_tamil_nadu_retrieval():
    case = make_deposit_case(state="Tamil Nadu")
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Landlord has not refunded your deposit in Tamil Nadu.",
            summary_chunk_ids=["IND-TN-TNRRRLTA-2017-SEC-011"],
            summary_supporting_quote="not exceeding three months rent",
            options=[
                Option(
                    title="Rely on Section 11 statutory cap and refund",
                    description=(
                        "Under Section 11 of the TNRRRLT Act, 2017, security deposit for residential "
                        "premises cannot exceed 3 months rent."
                    ),
                    next_steps="Issue legal notice citing Section 11.",
                    chunk_ids=["IND-TN-TNRRRLTA-2017-SEC-011"],
                    supporting_quote="not exceeding three months rent",
                )
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    assert "IND-TN-TNRRRLTA-2017-SEC-011" in res.citations_used
    assert res.limitation["computable"] is True
    assert res.limitation["period_years"] == 3


# --------------------------------------------------------------------------
# 14. Option next_steps as list and chunk normalization
# --------------------------------------------------------------------------
def test_option_list_next_steps_and_chunk_coercion():
    data = {
        "title": ["Send", "Demand Notice"],
        "description": "Send a formal written notice to landlord.",
        "next_steps": [
            "Make a formal written demand via registered post",
            "Give 15 days to respond",
            "Collect postal receipt as proof"
        ],
        "chunk_ids": "IND-MH-MRCA-1999-SEC-24",
        "supporting_quote": "deliver possession of such premises to the landlord"
    }
    opt = Option.model_validate(data)
    assert opt.title == "Send Demand Notice"
    assert opt.next_steps == (
        "Make a formal written demand via registered post; "
        "Give 15 days to respond; "
        "Collect postal receipt as proof"
    )
    assert opt.chunk_ids == ["IND-MH-MRCA-1999-SEC-24"]
    assert opt.supporting_quote == "deliver possession of such premises to the landlord"


# --------------------------------------------------------------------------
# 15. End-to-end explain with list next_steps and missing leading-zero chunk
# --------------------------------------------------------------------------
def test_explain_with_list_next_steps_and_chunk_variants():
    case = make_deposit_case(state="Maharashtra")
    raw_json = """
    {
      "summary": "Under Section 24 of the Maharashtra Rent Control Act, premises are delivered on expiry.",
      "summary_chunk_ids": ["IND-MH-MRCA-1999-SEC-24"],
      "summary_supporting_quote": "deliver possession of such premises to the landlord",
      "options": [
        {
          "title": "Deliver vacant possession",
          "description": "Ensure possession is delivered as stated in Section 24.",
          "next_steps": [
            "Draft formal handover letter",
            "Send via Speed Post or Registered AD"
          ],
          "chunk_ids": ["IND-MH-MRCA-1999-SEC-24"],
          "supporting_quote": "deliver possession of such premises to the landlord"
        }
      ],
      "other_side": [
        {
          "argument": "The landlord may claim licensee did not deliver possession.",
          "chunk_ids": ["[IND-MH-MRCA-1999-SEC-024]"],
          "supporting_quote": "failure of the licensee to so deliver the possession"
        }
      ],
      "evidence_gaps": ["Handover receipt of keys"],
      "uncertainties": ["Whether notice was already sent"]
    }
    """
    llm_expl = LLMExplanation.model_validate_json(raw_json)

    mock_llm = FakeDomainLLMClient(llm_expl)
    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    assert len(res.options) == 1
    assert "Draft formal handover letter" in res.options[0].next_steps
    assert "Send via Speed Post" in res.options[0].next_steps
    assert "IND-MH-MRCA-1999-SEC-024" in res.citations_used
    assert res.removed_claims == []


# --------------------------------------------------------------------------
# 16. Anti-hallucination quote check: fake quote gets dropped
# --------------------------------------------------------------------------
def test_unsupported_quote_dropped_as_hallucination():
    case = make_deposit_case(state="Maharashtra")
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Valid summary under Article 22.",
            summary_chunk_ids=["IND-FED-LIM-1963-ART-022"],
            summary_supporting_quote="Money deposited under an agreement that it shall be payable on demand",
            options=[
                Option(
                    title="Real option",
                    description="Money deposited payable on demand under Article 22.",
                    next_steps="Draft written demand.",
                    chunk_ids=["IND-FED-LIM-1963-ART-022"],
                    supporting_quote="Money deposited under an agreement that it shall be payable on demand",
                ),
                Option(
                    title="Fake quote option",
                    description="Landlord must refund deposit within 15 days or pay triple damages.",
                    next_steps="Go to police station.",
                    chunk_ids=["IND-MH-MRCA-1999-SEC-024"],
                    supporting_quote="landlord must refund deposit within 15 days",  # NOT in chunk!
                ),
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    assert len(res.options) == 1
    assert res.options[0].title == "Real option"
    assert len(res.removed_claims) == 1
    assert res.removed_claims[0]["item"] == "option:Fake quote option"
    assert any("unsupported_quote" in r for r in res.removed_claims[0]["reasons"])


# --------------------------------------------------------------------------
# 17. Conservative limitation: earliest plausible date selected
# --------------------------------------------------------------------------
def test_conservative_limitation_anchor_selection():
    # User paid deposit on 2024-03-01, moved out on 2024-08-01
    case = make_deposit_case(
        state="Maharashtra",
        slots={
            "deposit_paid_date": "2024-03-01",
            "tenancy_end_date": "2024-08-01",
            "demand_made": "i contact him weekly via call",
        }
    )
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Position summary.",
            summary_chunk_ids=["IND-FED-LIM-1963-ART-022"],
            summary_supporting_quote="Money deposited under an agreement that it shall be payable on demand",
            options=[
                Option(
                    title="Demand refund",
                    description="Take action within limitation.",
                    next_steps="Send written notice.",
                    chunk_ids=["IND-FED-LIM-1963-ART-022"],
                    supporting_quote="Money deposited under an agreement that it shall be payable on demand",
                )
            ],
            other_side=[],
            evidence_gaps=[],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    assert res.abstain is False
    lim = res.limitation
    assert lim["computable"] is True
    # Conservative deadline is earliest: 2024-03-01 + 3 years = 2027-03-01 (not 2027-08-01)
    assert lim["deadline"] == "2027-03-01"
    assert lim["anchor_event"] == "deposit_paid"
    assert lim["is_arguable"] is True
    assert "earliest plausible starting event" in lim["assumption"]
    assert "2027-08-01" in lim["assumption"]
    assert "weekly via call" in lim["assumption"] or "calls" in lim["assumption"]
    # Escalate on arguable rules: consult a lawyer line in reply text even when abstain=False
    assert "consult a qualified lawyer" in res.reply_text.lower() or "15100" in res.reply_text


# --------------------------------------------------------------------------
# 18. Known intake slots are not repeated as evidence gaps
# --------------------------------------------------------------------------
def test_resolved_intake_slots_not_in_evidence_gaps():
    case = make_deposit_case(
        state="Maharashtra",
        slots={
            "possession_handed_over": "yes i handed back the keys but there is no proof for that",
            "agreement_type": "written rent agreement",
        }
    )
    mock_llm = FakeDomainLLMClient(
        LLMExplanation(
            summary="Position summary.",
            summary_chunk_ids=["IND-FED-LIM-1963-ART-022"],
            summary_supporting_quote="Money deposited under an agreement that it shall be payable on demand",
            options=[],
            other_side=[],
            evidence_gaps=[
                "Proof of handing over keys",  # Already answered by user!
                "Original rent agreement",      # Already confirmed by user!
                "Bank transfer proof of payment",  # Genuine gap
            ],
            uncertainties=[],
        )
    )

    res = explain(case, today=TODAY, llm_client=mock_llm)

    # Possession handover and agreement should be filtered out from evidence_gaps
    assert not any("handing over keys" in g.lower() for g in res.evidence_gaps)
    assert not any("rent agreement" in g.lower() for g in res.evidence_gaps)
    assert any("bank transfer proof" in g.lower() for g in res.evidence_gaps)
