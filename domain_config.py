"""
Per-issue configuration registry for the domain (explain) agent.

Design: ONE shared domain agent, driven by this small per-issue config registry.
Adding a new issue type = adding one entry to ISSUE_CONFIG (plus, if needed,
a LimitationSpec). No new agent class required.

Each config holds:
  - corpus scope filter  (scope_categories + jurisdiction)
  - query hints          (retrieval query seed terms)
  - relevant slot keys   (case slots pulled into retrieval queries)
  - limitation rule key  (LimitationSpec: period, provenance chunk, anchor slot)

The limitation period and its provenance chunk_id come from here / the corpus,
never from the LLM.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

IssueType = Literal["security_deposit", "unpaid_salary"]


@dataclass(frozen=True)
class LimitationSpec:
    """Deterministic limitation metadata. Never sourced from the LLM.

    basis:
      - "limitation_act"            -> Limitation Act, 1963 schedule article
      - "consumer_protection_act"   -> CPA 2019 s. 69 (2 years)
                                      (consumer complaints use the CPA's own
                                       deadline, never the Limitation Act)
    """

    basis: Literal["limitation_act", "consumer_protection_act"]
    period_years: int
    start_slot: str            # case slot that anchors the limitation clock
    chunk_id: str              # corpus provision that states the period (provenance)
    chunk_section: str         # human label, e.g. "Article 22"
    fallback_slot: str | None = None  # used if start_slot has no date


@dataclass(frozen=True)
class IssueConfig:
    issue_type: IssueType
    display_name: str
    scope_categories: list[str]          # corpus scope_category filters
    supported_states: list[str] | None   # None => any state OK
    jurisdiction_by_state: dict[str, str]  # state -> corpus jurisdiction filter
    default_jurisdiction: str            # used when state is not keyed / N/A
    query_hints: list[str]               # retrieval query seed terms
    relevant_slot_keys: list[str]        # case slots pulled into retrieval queries
    limitation: LimitationSpec


# ---------------------------------------------------------------------------
# Issue configs
# ---------------------------------------------------------------------------

SECURITY_DEPOSIT = IssueConfig(
    issue_type="security_deposit",
    display_name="Security deposit refund",
    scope_categories=["Rent Law", "Limitation"],
    supported_states=["Delhi", "Maharashtra", "Karnataka", "Tamil Nadu"],
    jurisdiction_by_state={
        "Delhi": "National Capital Territory of Delhi",
        "Maharashtra": "State of Maharashtra",
        "Karnataka": "State of Karnataka",
        "Tamil Nadu": "State of Tamil Nadu",
    },
    default_jurisdiction="Central (Union of India)",
    query_hints=[
        "security deposit refund",
        "advance deposit",
        "vacate premises",
        "repayment of deposit",
        "tenant vacating property",
        "money deposited payable on demand",
        "money received for plaintiff use",
        "failure of consideration refund",
        "limitation period deposit",
        "rights and liabilities lessor lessee",
    ],
    relevant_slot_keys=[
        "deposit_amount_inr",
        "deposit_paid_date",
        "tenancy_end_date",
        "possession_handed_over",
        "landlord_reason_for_withholding",
        "demand_made",
    ],
    limitation=LimitationSpec(
        basis="limitation_act",
        period_years=3,
        start_slot="demand_made",
        fallback_slot="tenancy_end_date",
        chunk_id="IND-FED-LIM-1963-ART-022",
        chunk_section="Limitation Act, 1963 — Article 22",
    ),
)

UNPAID_SALARY = IssueConfig(
    issue_type="unpaid_salary",
    display_name="Unpaid salary / wages",
    scope_categories=["Wage & Employment", "Limitation"],
    supported_states=None,  # Central laws apply across states
    jurisdiction_by_state={},
    default_jurisdiction="Central (Union of India)",
    query_hints=[
        "unpaid wages",
        "final settlement",
        "time limit for payment of wages",
        "resignation",
        "termination",
        "delayed wages recovery",
        "claims before authority",
        "two working days",
        "limitation period wages",
        "recovery of wages authority",
    ],
    relevant_slot_keys=[
        "monthly_wage_inr",
        "unpaid_period_from",
        "unpaid_period_to",
        "amount_unpaid_inr",
        "still_employed",
        "employment_end_date",
        "employer_reason_for_nonpayment",
        "demand_made",
    ],
    limitation=LimitationSpec(
        basis="limitation_act",
        period_years=3,
        start_slot="unpaid_period_from",
        fallback_slot="employment_end_date",
        chunk_id="IND-FED-LIM-1963-ART-007",
        chunk_section="Limitation Act, 1963 — Article 7",
    ),
)

ISSUE_CONFIG: dict[IssueType, IssueConfig] = {
    "security_deposit": SECURITY_DEPOSIT,
    "unpaid_salary": UNPAID_SALARY,
}


def get_config(issue_type: IssueType) -> IssueConfig | None:
    return ISSUE_CONFIG.get(issue_type)
