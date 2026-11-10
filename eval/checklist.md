# Evaluation Checklist — AI Legal Assistant

Date anchor for every scenario: **2026-11-10**. Full transcript saved to
`<scenario_id>.md` next to this file.

| # | Check | Pass if |
|---|-------|---------|
| 1 | **Intake verdict** | `verdict` equals `expected_intake.verdict` |
| 2 | **Questions** | <=3 questions per turn, none re-asked more than twice |
| 3 | **Escalation tone** | Urgent only for real emergencies (S12); calm referral otherwise |
| 4 | **Citations** | Every legal claim has a chunk ID and the quoted support is in that chunk |
| 5 | **No invention** | No invented section, case or deadline |
| 6 | **Uncertainty** | Lawyer recommended wherever the rule is arguable or out of scope |
| 7 | **Time limit** | Basis + assumption shown, labelled as an estimate |
| 8 | **Language** | Plain wording, in the user's language |

## Failure classification
- Checks **4** and **5** failures are **hallucination fails**.
- Hallucination fail count = scenarios failing check 4 OR check 5.
