#!/usr/bin/env python3
"""Simple CLI chat loop for manual testing of the intake agent."""

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from case_schema import CaseFile
from intake_agent import (
    GeminiLLMClient,
    LLMClient,
    process_turn,
    save_case,
    load_case,
    TurnResult,
)

DEFAULT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "case.json")


def main() -> None:
    ap = argparse.ArgumentParser(description="Intake & Domain agent CLI")
    ap.add_argument("--case-id", default="default", help="Case identifier")
    ap.add_argument("--path", default=DEFAULT_PATH, help="JSON state file path")
    ap.add_argument("--new", action="store_true", help="Start a new case instead of loading existing case.json")
    ap.add_argument("--explain", action="store_true", help="Run domain agent explain directly on existing case.json")
    args = ap.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise SystemExit(
            "GEMINI_API_KEY environment variable not set. "
            "Export it and retry, e.g.:\n"
            "    export GEMINI_API_KEY='your-gemini-api-key-here'\n"
            "    python3 chat_cli.py"
        )
    client: LLMClient = GeminiLLMClient(api_key=api_key)

    if args.new and os.path.exists(args.path):
        os.remove(args.path)

    case: CaseFile = load_case(args.path) if os.path.exists(args.path) else CaseFile(
        case_id=args.case_id, language="en"
    )

    if args.explain:
        print(f"Running Domain Agent directly on case: {case.case_id} (state={case.state}, issue={case.issue.primary})...")
        from domain_agent import explain
        expl = explain(case, llm_client=client)
        print_explanation(expl)
        return

    print(f"Intake agent ready. Case: {case.case_id}")
    print("Commands: 'quit' | 'save' | 'status' | 'explain' | 'new' | just type your message.")
    print("=" * 60)

    while True:
        try:
            msg = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        if not msg:
            continue
        if msg == "quit":
            save_case(case, args.path)
            print("Saved. Goodbye.")
            break
        if msg == "save":
            save_case(case, args.path)
            print("(saved to", args.path, ")")
            continue
        if msg == "status":
            print(case.model_dump_json(indent=2, ensure_ascii=False)[:3000])
            continue
        if msg == "new":
            import time
            case = CaseFile(case_id=f"case-{int(time.time())}", language="en")
            save_case(case, args.path)
            print(f"Started fresh case: {case.case_id}")
            continue
        if msg == "explain":
            from domain_agent import explain
            print("\nCalling Domain Agent (explain)...")
            try:
                expl = explain(case, llm_client=client)
                print_explanation(expl)
            except Exception as e:
                print(f"\n[Domain Agent Error]: {e}")
            continue

        result: TurnResult = process_turn(case, msg, llm_client=client)
        case = result.case
        print(f"\nAgent [{result.verdict}]: {result.reply_text}")
        if result.escalation_reasons:
            print(f"[escalation reasons: {result.escalation_reasons}]")
        if result.missing_required:
            print(f"[still missing: {result.missing_required}]")
        save_case(case, args.path)

        # Automatic handoff when intake reaches 'ready'
        if result.verdict == "ready":
            print("\n" + "=" * 60)
            print("AUTOMATIC HANDOFF: Intake is READY -> Handing off to Domain Specialist...")
            print("=" * 60)
            from domain_agent import explain
            try:
                expl = explain(case, llm_client=client)
                print_explanation(expl)
            except Exception as e:
                print(f"\n[Domain Agent Error]: {e}")
            print("=" * 60)


def print_explanation(expl) -> None:
    print(f"\n--- Domain Specialist Explanation (abstain={expl.abstain}) ---")
    if expl.abstain:
        print(f"Status: ABSTAINED (Reason: {expl.abstain_reason})")
    print(f"\n{expl.reply_text}\n")
    if expl.options:
        print("Structured Legal Options:")
        for idx, opt in enumerate(expl.options, 1):
            cites = f" [Citations: {', '.join(opt.chunk_ids)}]" if opt.chunk_ids else ""
            print(f"  {idx}. {opt.title}{cites}")
            print(f"     Details: {opt.description}")
            print(f"     Next Steps: {opt.next_steps}")
    if expl.other_side:
        print("\nWhat the Other Side May Argue:")
        for idx, arg in enumerate(expl.other_side, 1):
            cites = f" [Citations: {', '.join(arg.chunk_ids)}]" if arg.chunk_ids else ""
            print(f"  {idx}. {arg.argument}{cites}")
    if expl.evidence_gaps:
        print("\nEvidence Gaps:")
        for gap in expl.evidence_gaps:
            print(f"  - {gap}")
    if expl.limitation and expl.limitation.get("computable"):
        print("\nLimitation / Time Limit Status:")
        print(f"  Deadline: {expl.limitation.get('deadline')}")
        print(f"  Days Remaining: {expl.limitation.get('days_left')}")
        print(f"  Warning: {expl.limitation.get('warning')}")
        print(f"  Basis: {expl.limitation.get('basis')} ({expl.limitation.get('chunk_section')})")
    if expl.citations_used:
        print(f"\nCorpus Citations Used ({len(expl.citations_used)}): {', '.join(expl.citations_used)}")
    if expl.removed_claims:
        print(f"\nDropped/Flagged Claims (Citation Validator): {expl.removed_claims}")
    if expl.data_quality_flags:
        print(f"\nCorpus Data Quality Flags: {expl.data_quality_flags}")


if __name__ == "__main__":
    main()
