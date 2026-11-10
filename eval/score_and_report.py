"""Score-and-report: reads scenario transcripts + a scores JSON and prints the
scenario x check pass/fail table, hallucination-fail tally, and a before/after diff.

Usage:
    python3 eval/score_and_report.py <scores.json> [--before before.json] [--after after.json]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


CHECK_LABELS = {
    "1_intake_verdict": "1. Intake verdict",
    "2_questions": "2. Questions",
    "3_escalation_tone": "3. Escalation tone",
    "4_citations": "4. Citations",
    "5_no_invention": "5. No invention",
    "6_uncertainty": "6. Uncertainty",
    "7_time_limit": "7. Time limit",
    "8_language": "8. Language",
}

CHECKS = list(CHECK_LABELS)


def load(path: str) -> list[dict]:
    """Load concatenated JSON objects (one per scenario) emitted by run_scenario.py."""
    raw = Path(path).read_text(encoding="utf-8")
    objects = []
    i = 0
    n = len(raw)
    while i < n:
        # Skip whitespace and separators
        while i < n and raw[i] in " \t\r\n,":
            i += 1
        if i >= n:
            break
        if raw[i] != "{":
            # skip to next brace-ish content
            i += 1
            continue
        # Try to parse a single object
        start = i
        depth = 0
        in_str = False
        escaped = False
        while i < n:
            c = raw[i]
            if in_str:
                if escaped:
                    escaped = False
                elif c == "\\":
                    escaped = True
                elif c == "\"":
                    in_str = False
            else:
                if c == "\"":
                    in_str = True
                elif c == "{":
                    depth += 1
                elif c == "}":
                    depth -= 1
                    if depth == 0:
                        objects.append(raw[start:i+1])
                        i += 1
                        break
            i += 1
    results = []
    for obj in objects:
        try:
            results.append(json.loads(obj))
        except json.JSONDecodeError:
            continue
    if not results:
        # Fallback: maybe a single JSON array
        try:
            data = json.loads(raw)
            if isinstance(data, dict):
                return [data]
            return data
        except json.JSONDecodeError:
            pass
    return results


def hallucination_fails(s: dict) -> int:
    return int(s.get("4_citations") == "fail" or s.get("5_no_invention") == "fail")


def print_table(results: list[dict], title: str = "Scenario x check"):
    print(f"\n{'='*100}")
    print(f" {title}")
    print(f"{'='*100}")
    header = f"{'Scenario':<8}" + "".join(f"{CHECK_LABELS.get(c,'?'):<22}" for c in CHECKS)
    print(header)
    print("-" * 100)
    for r in results:
        sid = r.get("id", "?")
        s = r.get("checks", {})
        row = f"{sid:<8}" + "".join(f"{s.get(c,'?'):<22}" for c in CHECKS)
        print(row)
    print("-" * 100)
    for r in results:
        sid = r.get("id", "?")
        s = r.get("checks", {})
        passed = sum(1 for c in CHECKS if s.get(c) == "pass")
        h = hallucination_fails(s)
        print(f"  {sid}: {passed}/8 passed, {h} hallucination fail(s)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scores", help="scores JSON produced by run_scenario.py --json")
    ap.add_argument("--before", help="baseline scores JSON for before/after")
    ap.add_argument("--after", help="after-fix scores JSON")
    args = ap.parse_args()

    results = load(args.scores)
    print_table(results)

    if args.before and args.after:
        before = load(args.before)
        after = load(args.after)
        bmap = {r.get("id"): r.get("checks", {}) for r in before}
        amap = {r.get("id"): r.get("checks", {}) for r in after}
        print("\n" + "="*100)
        print("BEFORE / AFTER (pass count / hallucination fails)")
        print("="*100)
        for sid in sorted(set(bmap) | set(amap)):
            b = bmap.get(sid, {})
            a = amap.get(sid, {})
            bp = sum(1 for c in CHECKS if b.get(c) == "pass")
            ap_ = sum(1 for c in CHECKS if a.get(c) == "pass")
            bh = hallucination_fails(b)
            ah = hallucination_fails(a)
            print(f"  {sid}: before {bp}/8 h={bh} | after {ap_}/8 h={ah}")


if __name__ == "__main__":
    main()
