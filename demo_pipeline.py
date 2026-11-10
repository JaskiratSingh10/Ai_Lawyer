#!/usr/bin/env python3
"""End-to-End Pipeline Demonstration Script.

Runs the complete AI Legal Assistant pipeline:
  Intake Case File -> Domain (Explain) Agent -> Limitation & Citation Validation -> Explanation.

Can be run offline with mock LLM responses or online with real Gemini if GEMINI_API_KEY is exported:
    python3 demo_pipeline.py
"""

import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from case_schema import CaseFile, Issue, Slot
from domain_agent import Explanation, LLMExplanation, Option, OtherSideArg, explain
from intake_agent import GeminiLLMClient, LLMClient

TODAY = date(2026, 11, 10)


class MockExplainLLMClient(LLMClient):
    """Deterministic LLM response used when GEMINI_API_KEY is not set."""

    def __init__(self, issue_type: str):
        self.issue_type = issue_type

    def complete(self, prompt: str, schema: type) -> LLMExplanation:
        if self.issue_type == "security_deposit":
            return LLMExplanation(
                summary=(
                    "You vacated the rented premises and your landlord has withheld your security deposit "
                    "of ₹20,000 without returning it within the customary move-out period. Under Article 22 "
                    "of the Limitation Act, 1963, you have three years from when the demand is made to take legal action."
                ),
                summary_chunk_ids=["IND-FED-LIM-1963-ART-022"],
                summary_supporting_quote="Money deposited under an agreement that it shall be payable on demand",
                options=[
                    Option(
                        title="Send a formal legal notice for refund of security deposit",
                        description=(
                            "Issue a written demand notice specifying the deposit amount, handover date, "
                            "and demanding full repayment within 15 days."
                        ),
                        next_steps="Draft notice with dates and bank account details; send via registered post or email.",
                        chunk_ids=["IND-FED-LIM-1963-ART-022"],
                        supporting_quote="Money deposited under an agreement that it shall be payable on demand",
                    ),
                    Option(
                        title="File a recovery complaint before the competent civil authority / Rent Authority",
                        description=(
                            "If the landlord fails to refund the deposit after the demand notice, you can "
                            "file a recovery application."
                        ),
                        next_steps="Gather handover proof, rent agreement, bank transfer receipts, and the demand notice copy.",
                        chunk_ids=["IND-FED-LIM-1963-ART-022"],
                        supporting_quote="Money deposited under an agreement that it shall be payable on demand",
                    ),
                ],
                other_side=[
                    OtherSideArg(
                        argument=(
                            "The landlord may argue deductions for damages, pending utility dues, or repaint costs "
                            "under the tenancy terms."
                        ),
                        chunk_ids=["IND-FED-LIM-1963-ART-022"],
                        supporting_quote="Money deposited under an agreement that it shall be payable on demand",
                    )
                ],
                evidence_gaps=[
                    "Move-out condition photos or video documenting property handover condition",
                    "Written handover acknowledgment or message confirming return of keys",
                ],
                uncertainties=[
                    "Whether the rent agreement specifies any agreed move-out inspection procedure or mandatory deduction clause",
                ],
            )
        else:
            return LLMExplanation(
                summary=(
                    "Your employer owes you ₹100,000 in unpaid wages. Under Section 17 of the Code on Wages, 2019, "
                    "earned wages upon resignation or termination must be paid within two working days."
                ),
                summary_chunk_ids=["IND-FED-COW-2019-SEC-017"],
                summary_supporting_quote="pay or cause to be paid wages",
                options=[
                    Option(
                        title="File a claim before the Authority under Section 45",
                        description=(
                            "File an application before the appointed Authority under the Code on Wages to recover "
                            "unpaid wages plus statutory compensation up to 10 times."
                        ),
                        next_steps="Submit payslips, appointment letter, and written resignation proof.",
                        chunk_ids=["IND-FED-COW-2019-SEC-045"],
                        supporting_quote="appoint one or more authorities",
                    )
                ],
                other_side=[
                    OtherSideArg(
                        argument="The employer may claim deductions for unserved notice period under Section 18.",
                        chunk_ids=["IND-FED-COW-2019-SEC-018"],
                        supporting_quote="there shall be no deductions from the wages",
                    )
                ],
                evidence_gaps=["Formal relieving letter or email acceptance of resignation"],
                uncertainties=[],
            )


def run_demo(issue_type: str = "security_deposit") -> None:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if api_key:
        print("[Mode: Real Gemini API via GEMINI_API_KEY]")
        client: LLMClient = GeminiLLMClient(api_key=api_key)
    else:
        print("[Mode: Offline Demonstration via Mock LLM Client (Set GEMINI_API_KEY to run live with Gemini)]")
        client = MockExplainLLMClient(issue_type)

    if issue_type == "security_deposit":
        case = CaseFile(
            case_id="demo-security-deposit",
            language="en",
            state="Delhi",
            issue=Issue(primary="security_deposit", confidence=1.0),
            slots={
                "property_type": Slot(value="residential", status="known"),
                "deposit_amount_inr": Slot(value=20000, status="known"),
                "deposit_paid_date": Slot(value="2024-03-01", status="known"),
                "tenancy_end_date": Slot(value="2026-10-01", status="known"),
                "possession_handed_over": Slot(value="yes", status="known"),
                "landlord_reason_for_withholding": Slot(value="not responding", status="known"),
                "demand_made": Slot(value="2026-10-15", status="known"),
            },
        )
    else:
        case = CaseFile(
            case_id="demo-unpaid-salary",
            language="en",
            state="Delhi",
            issue=Issue(primary="unpaid_salary", confidence=1.0),
            slots={
                "monthly_wage_inr": Slot(value=50000, status="known"),
                "unpaid_period_from": Slot(value="2026-01-01", status="known"),
                "unpaid_period_to": Slot(value="2026-03-01", status="known"),
                "amount_unpaid_inr": Slot(value=100000, status="known"),
                "still_employed": Slot(value=False, status="known"),
                "employment_end_date": Slot(value="2026-03-01", status="known"),
                "demand_made": Slot(value="2026-03-05", status="known"),
                "employment_proof_available": Slot(value="yes", status="known"),
            },
        )

    print(f"\nCase ID: {case.case_id} | Issue: {case.issue.primary} | State: {case.state}")
    print("=" * 65)

    expl: Explanation = explain(case, today=TODAY, llm_client=client)

    print(f"\nDomain Agent Explanation (Abstained: {expl.abstain})")
    print("-" * 65)
    print(expl.reply_text)

    if expl.options:
        print("\nStructured Options:")
        for idx, opt in enumerate(expl.options, 1):
            print(f"  {idx}. {opt.title}")
            print(f"     Next Steps: {opt.next_steps}")
            print(f"     Citations: {opt.chunk_ids}")

    if expl.other_side:
        print("\nWhat the Other Side May Argue:")
        for idx, arg in enumerate(expl.other_side, 1):
            print(f"  {idx}. {arg.argument} (Citations: {arg.chunk_ids})")

    if expl.evidence_gaps:
        print("\nEvidence Gaps:")
        for gap in expl.evidence_gaps:
            print(f"  - {gap}")

    if expl.limitation:
        print("\nLimitation / Time Limit Status (Deterministic):")
        print(f"  Deadline: {expl.limitation.get('deadline')}")
        print(f"  Days Remaining: {expl.limitation.get('days_left')}")
        print(f"  Warning: {expl.limitation.get('warning')}")
        print(f"  Statutory Basis: {expl.limitation.get('chunk_section')}")
        print(f"  Corpus Verified: {expl.limitation.get('verified_against_corpus')}")

    if expl.citations_used:
        print(f"\nCorpus Provisions Cited ({len(expl.citations_used)}): {', '.join(expl.citations_used)}")

    if expl.removed_claims:
        print(f"\nValidation Removed Claims: {expl.removed_claims}")

    print("=" * 65)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "security_deposit"
    run_demo(target)
