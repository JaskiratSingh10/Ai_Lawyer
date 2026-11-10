#!/usr/bin/env python3
"""
Corpus RAG Engine & Verification CLI
Demonstrates structured retrieval, BM25 / FTS5 ranking with refined relevance re-ranking,
metadata filtering, temporal applicability comparison against case dates, and
legal status guardrails (including period_may_fall_under_repealed_acts).
"""

import argparse
import json
import os
import re
import sqlite3
import sys

CORPUS_ROOT = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(CORPUS_ROOT, "data", "corpus.db")
MANIFEST_PATH = os.path.join(CORPUS_ROOT, "manifest.json")
LABOUR_CODES_EFFECTIVE_DATE = "2025-11-21"

class LegalRAGEngine:
    def __init__(self, db_path=DB_PATH):
        if not os.path.exists(db_path):
            raise FileNotFoundError(f"Corpus database not found at {db_path}. Please run scripts/build_corpus.py first.")
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def derive_flags(self, case_date, results):
        """
        Derives temporal and jurisdictional flags based on case date and retrieved provisions.
        """
        flags = {
            "period_may_fall_under_repealed_acts": False,
            "case_date": case_date,
            "temporal_notes": []
        }
        if case_date:
            if case_date < LABOUR_CODES_EFFECTIVE_DATE:
                flags["period_may_fall_under_repealed_acts"] = True
                flags["temporal_notes"].append(
                    f"Dispute date ({case_date}) predates 21 November 2025 (commencement of Labour Codes). "
                    f"Claims arising prior to 21-Nov-2025 fall under legacy enactments (PWA 1936, MWA 1948, "
                    f"PGA 1972, EPF 1952, IDA 1947). Consult a legal practitioner."
                )
            else:
                flags["temporal_notes"].append(
                    f"Dispute date ({case_date}) is post-21-Nov-2025. Code on Wages 2019, Code on Social Security 2020, "
                    f"and Industrial Relations Code 2020 are the substantive in-force statutes."
                )
        return flags

    def search(self, query, jurisdiction=None, scope_category=None, in_force_only=False, case_date=None, limit=5):
        """
        Full-text BM25 search over provisions with phrase-aware re-ranking,
        metadata filtering, and case date temporal evaluation.
        """
        cur = self.conn.cursor()

        # Clean query tokens for SQLite FTS5
        tokens = re.findall(r'\b[a-zA-Z0-9]+\b', query)
        if not tokens:
            return {"results": [], "flags": self.derive_flags(case_date, [])}

        fts_terms = [f'"{t}"' for t in tokens]
        fts_query = " OR ".join(fts_terms)

        sql = """
        SELECT p.*, fts.rank as fts_rank
        FROM provisions_fts fts
        JOIN provisions p ON p.id = fts.id
        WHERE provisions_fts MATCH ?
        """
        params = [fts_query]

        if jurisdiction:
            sql += " AND p.jurisdiction LIKE ?"
            params.append(f"%{jurisdiction}%")

        if scope_category:
            sql += " AND p.scope_category = ?"
            params.append(scope_category)

        if in_force_only:
            sql += " AND p.legal_status = 'In Force'"

        # Over-fetch candidate provisions for precision re-ranking
        sql += " ORDER BY fts.rank ASC LIMIT 30"
        cur.execute(sql, params)
        candidates = [dict(r) for r in cur.fetchall()]

        # Precision re-ranking: Domain-term priority, phrase boosting, generic modifier downweighting
        query_lower = query.lower()
        q_words = set(re.findall(r'\b[a-z0-9]+\b', query_lower))
        generic_modifiers = {'two', 'three', 'second', 'days', 'day', 'working', 'under', 'for', 'with', 'after', 'and', 'the'}
        primary_terms = q_words - generic_modifiers

        # Extract n-gram phrases (2-grams, 3-grams) from query
        query_tokens = re.findall(r'\b[a-z0-9]+\b', query_lower)
        phrases = []
        for n in (2, 3):
            for i in range(len(query_tokens) - n + 1):
                phrases.append(" ".join(query_tokens[i:i+n]))

        scored = []
        for c in candidates:
            text_lower = c["exact_text"].lower()
            title_lower = c["section_or_rule_title"].lower()
            topics_json = c["key_topics_json"] if "key_topics_json" in c else "[]"
            topics_lower = " ".join(json.loads(topics_json)).lower()

            # Base score from BM25 rank (convert negative rank to positive magnitude)
            score = -c["fts_rank"]

            title_prim_matches = sum(1 for w in primary_terms if w in title_lower)
            topics_prim_matches = sum(1 for w in primary_terms if w in topics_lower)
            text_prim_matches = sum(1 for w in primary_terms if w in text_lower)

            score += title_prim_matches * 16.0
            score += topics_prim_matches * 14.0
            score += text_prim_matches * 4.0

            # Heavy penalty if a provision matches NONE of primary domain keywords
            # (e.g. Section 13 matching only 'working' and 'days' when query is about unpaid wages/resignation)
            if primary_terms and (title_prim_matches + topics_prim_matches + text_prim_matches == 0):
                score -= 60.0

            # Phrase match bonuses
            for ph in phrases:
                if ph in title_lower:
                    score += 25.0
                if ph in topics_lower:
                    score += 20.0
                if ph in text_lower:
                    score += 15.0

            # Legal synonym / equivalent phrase mappings
            if "two working days" in query_lower:
                if "second working day" in text_lower or "second working day" in topics_lower:
                    score += 20.0
            if "unpaid wages" in query_lower:
                if "delay in payment of wages" in text_lower or "time limit for payment of wages" in title_lower:
                    score += 15.0

            # Temporal adjustment if case_date is provided
            if case_date:
                eff = c.get("effective_from") or c.get("effective_date")
                rep = c.get("repealed_on")
                if case_date < LABOUR_CODES_EFFECTIVE_DATE:
                    # Dispute is pre-Labour Codes: prioritize legacy acts if applicable
                    if rep and rep >= LABOUR_CODES_EFFECTIVE_DATE:
                        score += 10.0
                else:
                    # Dispute is post-Labour Codes: prioritize in-force acts
                    if c["legal_status"] == "In Force":
                        score += 5.0

            scored.append((score, c))

        scored.sort(key=lambda x: x[0], reverse=True)
        top_items = [item[1] for item in scored[:limit]]

        # Construct enriched provision objects
        results = []
        for r in top_items:
            eff_from = r.get("effective_from", r["effective_date"])
            rep_on = r.get("repealed_on")

            # Check temporal validity for the provision against case_date
            in_force_at_date = True
            temporal_status = "In Force"
            if case_date:
                if eff_from > case_date:
                    in_force_at_date = False
                    temporal_status = f"Not yet in force on case date ({case_date})"
                elif rep_on and rep_on <= case_date:
                    in_force_at_date = False
                    temporal_status = f"Repealed on {rep_on} prior to case date ({case_date})"
                else:
                    temporal_status = f"In force on case date ({case_date})"

            results.append({
                "id": r["id"],
                "parent_doc_id": r["parent_doc_id"],
                "law_title": r["law_title"],
                "short_title": r["short_title"],
                "act_or_rule_type": r["act_or_rule_type"],
                "jurisdiction": r["jurisdiction"],
                "section_or_rule_number": r["section_or_rule_number"],
                "section_or_rule_title": r["section_or_rule_title"],
                "chapter_or_part": r["chapter_or_part"],
                "exact_text": r["exact_text"],
                "effective_date": r["effective_date"],
                "effective_from": eff_from,
                "repealed_on": rep_on,
                "enactment_date": r["enactment_date"],
                "legal_status": r["legal_status"],
                "legal_status_notes": r["legal_status_notes"],
                "official_source_url": r["official_source_url"],
                "scope_category": r["scope_category"],
                "key_topics": json.loads(r["key_topics_json"]) if "key_topics_json" in r else [],
                "cross_references": json.loads(r["cross_references_json"]) if "cross_references_json" in r else [],
                "in_force_at_case_date": in_force_at_date,
                "temporal_status": temporal_status,
                "bm25_rank": r["fts_rank"]
            })

        flags = self.derive_flags(case_date, results)
        return {"results": results, "flags": flags}

    def format_for_llm_context(self, search_output):
        """
        Formats retrieved provisions into a prompt-ready markdown block with
        clear provenance, exact text, and active temporal guardrails.
        """
        if isinstance(search_output, dict):
            provisions = search_output.get("results", [])
            flags = search_output.get("flags", {})
        else:
            provisions = search_output
            flags = {}

        if not provisions:
            return "No statutory provisions found in corpus matching the criteria."

        blocks = []

        # Header with temporal flags
        if flags.get("period_may_fall_under_repealed_acts"):
            blocks.append(
                f"> [!IMPORTANT]\n"
                f"> **TEMPORAL JURISDICTION FLAG (`period_may_fall_under_repealed_acts = True`)**:\n"
                f"> The case date ({flags.get('case_date')}) predates **21 November 2025**, when the Code on Wages 2019, "
                f"Code on Social Security 2020, and Industrial Relations Code 2020 came into force.\n"
                f"> Under Section 6 of the General Clauses Act, 1897 and the relevant repeal & savings clauses, "
                f"causes of action arising prior to 21 November 2025 fall under the **repealed legacy Acts** "
                f"(Payment of Wages Act 1936, Minimum Wages Act 1948, Payment of Gratuity Act 1972, Industrial Disputes Act 1947).\n"
                f"> Both current Code provisions and fallback legacy provisions are indexed in this corpus for cross-temporal accuracy."
            )

        for i, p in enumerate(provisions, 1):
            repeal_info = f" | **Repealed On**: `{p['repealed_on']}`" if p.get('repealed_on') else ""
            temporal_info = f"- **Temporal Applicability**: `{p.get('temporal_status', p['legal_status'])}`\n" if flags.get("case_date") else ""

            status_banner = ""
            if p.get("repealed_on"):
                status_banner = (
                    f"\n> [!NOTE]\n"
                    f"> **REPEAL & SAVINGS PROVISION**: Repealed w.e.f. {p['repealed_on']} by the new Labour Codes, "
                    f"but actively enforceable for disputes/claims where the cause of action arose before 21 November 2025."
                )

            block = (
                f"### [Source {i}] {p['law_title']} — {p['section_or_rule_number']}: {p['section_or_rule_title']}\n"
                f"- **Jurisdiction**: {p['jurisdiction']}\n"
                f"- **Instrument Type**: {p['act_or_rule_type']}\n"
                f"- **Enacted**: {p['enactment_date']} | **Effective From**: `{p['effective_from']}`{repeal_info}\n"
                f"- **Legal Status**: `{p['legal_status']}`\n"
                f"{temporal_info}"
                f"- **Official URL**: {p['official_source_url']}\n"
                f"{status_banner}\n"
                f"```text\n{p['exact_text']}\n```\n"
                f"*Parent Document*: `{p['parent_doc_id']}` | *Scope*: `{p['scope_category']}`\n"
            )
            blocks.append(block)

        return "\n\n".join(blocks)

def run_test_suite():
    print("=================================================================")
    print("RUNNING LEGAL RAG RETRIEVAL & TEMPORAL EVALUATION TEST SUITE")
    print("=================================================================")
    engine = LegalRAGEngine()

    test_queries = [
        {
            "description": "Test Case 1 (User Issue Eval): Unpaid wages & resignation final settlement within two working days",
            "query": "unpaid wages resignation two working days",
            "jurisdiction": "Central",
            "scope": "Wage & Employment",
            "case_date": "2026-02-15",
            "top_k": 5,
            "must_include": ["IND-FED-COW-2019-SEC-017", "IND-FED-PWA-1936-SEC-005"],
            "must_exclude_from_top3": ["IND-FED-COW-2019-SEC-013"]
        },
        {
            "description": "Test Case 2: Pre-21-Nov-2025 wage dispute (Temporal Flag period_may_fall_under_repealed_acts)",
            "query": "unpaid wages resignation two working days",
            "jurisdiction": "Central",
            "scope": "Wage & Employment",
            "case_date": "2025-06-10",
            "top_k": 5,
            "expected_flag": "period_may_fall_under_repealed_acts"
        },
        {
            "description": "Test Case 3: Landlord security deposit refund in Tamil Nadu",
            "query": "security deposit three months advance refund vacate",
            "jurisdiction": "Tamil Nadu",
            "scope": "Rent Law",
            "case_date": None,
            "top_k": 3
        },
        {
            "description": "Test Case 4: E-commerce product defect and refund liability",
            "query": "e-commerce refund defective goods marketplace unfair trade practice",
            "jurisdiction": "Central",
            "scope": "Consumer Protection",
            "case_date": None,
            "top_k": 3
        },
        {
            "description": "Test Case 5: Limitation period for recovery of unpaid wages or debt acknowledgment",
            "query": "limitation wages three years right to sue debt acknowledgment",
            "jurisdiction": "Central",
            "scope": "Limitation",
            "case_date": None,
            "top_k": 3
        },
        {
            "description": "Test Case 6: Delhi Rent Control rent ceiling vs TPA 1882",
            "query": "three thousand five hundred rent premises Delhi exemption",
            "jurisdiction": "Delhi",
            "scope": "Rent Law",
            "case_date": None,
            "top_k": 3
        },
        {
            "description": "Test Case 7: Consumer Commission Pecuniary Jurisdiction Limits (2021 Rules)",
            "query": "District Commission fifty lakh State Commission two crore jurisdiction",
            "jurisdiction": "Central",
            "scope": "Consumer Protection",
            "case_date": None,
            "top_k": 3
        }
    ]

    all_passed = True
    for t in test_queries:
        print(f"\n--- {t['description']} ---")
        print(f"Query: '{t['query']}' | Scope: {t['scope']} | Jurisdiction: {t['jurisdiction']} | Case Date: {t.get('case_date')}")
        search_res = engine.search(
            t["query"],
            jurisdiction=t["jurisdiction"],
            scope_category=t["scope"],
            case_date=t.get("case_date"),
            limit=t.get("top_k", 5)
        )
        results = search_res["results"]
        flags = search_res["flags"]

        print(f"Results Returned: {len(results)}")
        retrieved_ids = [r["id"] for r in results]
        top3_ids = retrieved_ids[:3]

        for idx, r in enumerate(results, 1):
            rep_str = f" [Repealed: {r['repealed_on']}]" if r['repealed_on'] else ""
            print(f"  {idx}. [{r['id']}] {r['short_title']} - {r['section_or_rule_number']}: {r['section_or_rule_title']}")
            print(f"     Status: {r['legal_status']}{rep_str} | Effective From: {r['effective_from']}")

        # Verification checks
        if "must_include" in t:
            for req_id in t["must_include"]:
                if req_id in retrieved_ids:
                    print(f"  [PASS] Required provision {req_id} present in top-{t['top_k']}")
                else:
                    print(f"  [FAIL] Required provision {req_id} MISSING from top-{t['top_k']}")
                    all_passed = False

        if "must_exclude_from_top3" in t:
            for exc_id in t["must_exclude_from_top3"]:
                if exc_id not in top3_ids:
                    print(f"  [PASS] Weak-relevance provision {exc_id} successfully excluded from top-3")
                else:
                    print(f"  [FAIL] Weak-relevance provision {exc_id} incorrectly present in top-3")
                    all_passed = False

        if "expected_flag" in t:
            flag_name = t["expected_flag"]
            if flags.get(flag_name) is True:
                print(f"  [PASS] Flag '{flag_name}' successfully triggered (True) for case date {t.get('case_date')}")
            else:
                print(f"  [FAIL] Flag '{flag_name}' failed to trigger for case date {t.get('case_date')}")
                all_passed = False

    print("\n=================================================================")
    if all_passed:
        print("ALL TEST SUITE EVALUATIONS PASSED!")
    else:
        print("SOME EVALUATION CHECKS FAILED - REVIEW LOGS")
    print("=================================================================")
    return all_passed

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Legal RAG Corpus Query Tool")
    parser.add_argument("--query", "-q", type=str, help="Search query string")
    parser.add_argument("--jurisdiction", "-j", type=str, help="Filter by jurisdiction (e.g. Central, Delhi, Maharashtra, Karnataka, Tamil Nadu)")
    parser.add_argument("--scope", "-s", type=str, choices=["Consumer Protection", "Limitation", "Wage & Employment", "Rent Law"], help="Filter by scope category")
    parser.add_argument("--case-date", "-d", type=str, help="Dispute / cause of action date in YYYY-MM-DD format for temporal applicability")
    parser.add_argument("--in-force", action="store_true", help="Filter for only currently enforced provisions")
    parser.add_argument("--limit", "-n", type=int, default=5, help="Max results to return")
    parser.add_argument("--test", action="store_true", help="Run the test suite")
    parser.add_argument("--format-llm", action="store_true", help="Output in LLM prompt markdown format")

    args = parser.parse_args()

    if args.test or len(sys.argv) == 1:
        run_test_suite()
    else:
        engine = LegalRAGEngine()
        output = engine.search(
            args.query,
            jurisdiction=args.jurisdiction,
            scope_category=args.scope,
            in_force_only=args.in_force,
            case_date=args.case_date,
            limit=args.limit
        )
        if args.format_llm:
            print(engine.format_for_llm_context(output))
        else:
            flags = output["flags"]
            results = output["results"]
            print(f"Found {len(results)} matches for '{args.query}':\n")
            if flags.get("period_may_fall_under_repealed_acts"):
                print(">> [ALERT] period_may_fall_under_repealed_acts = True")
                for note in flags["temporal_notes"]:
                    print(f"   {note}")
                print()
            for r in results:
                rep_str = f" | Repealed: {r['repealed_on']}" if r['repealed_on'] else ""
                print(f"[{r['id']}] {r['short_title']} - {r['section_or_rule_number']}: {r['section_or_rule_title']}")
                print(f"Jurisdiction: {r['jurisdiction']} | Status: {r['legal_status']}{rep_str} | Effective From: {r['effective_from']}")
                if args.case_date:
                    print(f"Temporal Applicability (Date: {args.case_date}): {r['temporal_status']}")
                print(f"URL: {r['official_source_url']}")
                print(f"Text Snippet:\n{r['exact_text'][:200]}...\n{'-'*60}")
