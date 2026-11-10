#!/usr/bin/env python3
"""
Corpus Build and Validation Script for Indian Legislation RAG.
Aggregates all scoped statutory instruments, validates schema compliance,
generates JSON, JSONL, SQLite FTS5 database, domain-specific dumps,
and an integrity manifest.
"""

import json
import os
import sqlite3
import sys

# Ensure provisions package is importable
sys.path.insert(0, os.path.dirname(__file__))

from provisions.consumer_data import DOCUMENTS as CONSUMER_DOCS, PROVISIONS as CONSUMER_PROVS
from provisions.limitation_data import DOCUMENTS as LIMITATION_DOCS, PROVISIONS as LIMITATION_PROVS
from provisions.employment_data import DOCUMENTS as EMPLOYMENT_DOCS, PROVISIONS as EMPLOYMENT_PROVS
from provisions.rent_data import DOCUMENTS as RENT_DOCS, PROVISIONS as RENT_PROVS

CORPUS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(CORPUS_ROOT, "data")
DOMAIN_DIR = os.path.join(CORPUS_ROOT, "provisions_by_domain")

REQUIRED_PROV_FIELDS = [
    "id",
    "parent_doc_id",
    "law_title",
    "short_title",
    "act_or_rule_type",
    "jurisdiction",
    "section_or_rule_number",
    "section_or_rule_title",
    "chapter_or_part",
    "exact_text",
    "effective_date",
    "effective_from",
    "repealed_on",
    "enactment_date",
    "legal_status",
    "legal_status_notes",
    "version_as_of_date",
    "official_source_url",
    "retrieval_date",
    "scope_category",
    "key_topics",
    "cross_references"
]

REQUIRED_DOC_FIELDS = [
    "id",
    "law_title",
    "short_title",
    "act_or_rule_type",
    "act_number",
    "jurisdiction",
    "enactment_date",
    "effective_date",
    "effective_from",
    "repealed_on",
    "legal_status",
    "legal_status_notes",
    "official_source_url",
    "ministry",
    "retrieval_date",
    "scope_category"
]

def main():
    all_docs = CONSUMER_DOCS + LIMITATION_DOCS + EMPLOYMENT_DOCS + RENT_DOCS
    all_provs = CONSUMER_PROVS + LIMITATION_PROVS + EMPLOYMENT_PROVS + RENT_PROVS

    print("=================================================================")
    print("STARTING CORPUS BUILD & VALIDATION AUDIT")
    print("=================================================================")
    print(f"Total Parent Documents: {len(all_docs)}")
    print(f"Total Provisions:       {len(all_provs)}")

    # 1. Validation Checks
    doc_ids = set()
    for d in all_docs:
        for f in REQUIRED_DOC_FIELDS:
            if f not in d:
                raise ValueError(f"Document {d.get('id')} missing required field: {f}")
            if f != "repealed_on" and not str(d[f]).strip():
                raise ValueError(f"Document {d.get('id')} has empty field: {f}")
        if d["id"] in doc_ids:
            raise ValueError(f"Duplicate document id found: {d['id']}")
        doc_ids.add(d["id"])

    prov_ids = set()
    for p in all_provs:
        for f in REQUIRED_PROV_FIELDS:
            if f not in p:
                raise ValueError(f"Provision {p.get('id')} missing required field: {f}")
            if f != "repealed_on" and p[f] is None:
                raise ValueError(f"Provision {p.get('id')} has None for required field: {f}")
        if p["id"] in prov_ids:
            raise ValueError(f"Duplicate provision id found: {p['id']}")
        prov_ids.add(p["id"])
        if p["parent_doc_id"] not in doc_ids:
            raise ValueError(f"Provision {p['id']} references nonexistent parent_doc_id: {p['parent_doc_id']}")

    print(">> Schema validation passed cleanly: All fields present, foreign keys valid, no duplicates.")

    # 2. Write Master JSON
    master_json_path = os.path.join(DATA_DIR, "indian_legal_corpus.json")
    master_data = {
        "metadata": {
            "title": "Corpus of Indian Legislation for Retrieval-Augmented Generation (RAG)",
            "curator": "Legal Data Curation Agent",
            "version": "1.0.0",
            "as_of_date": "2026-11-09",
            "retrieval_date": "2026-11-09",
            "total_documents": len(all_docs),
            "total_provisions": len(all_provs),
            "scopes": [
                "Consumer Protection Act 2019 & Rules (E-Commerce 2020, Jurisdiction 2021/2020)",
                "The Limitation Act 1963 & Relevant Schedule Articles",
                "Wage & Employment Laws (Code on Wages 2019, Social Security 2020, IR Code 2020, Interim Active Acts)",
                "Rent Laws (Delhi, Maharashtra, Karnataka, Tamil Nadu, and TPA 1882 ss. 105-117 fallback)"
            ]
        },
        "documents": all_docs,
        "provisions": all_provs
    }
    with open(master_json_path, "w", encoding="utf-8") as f:
        json.dump(master_data, f, indent=2, ensure_ascii=False)
    print(f">> Master JSON written: {master_json_path} ({os.path.getsize(master_json_path)} bytes)")

    # 3. Write Master JSONL
    master_jsonl_path = os.path.join(DATA_DIR, "provisions.jsonl")
    with open(master_jsonl_path, "w", encoding="utf-8") as f:
        for p in all_provs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    print(f">> Master JSONL written: {master_jsonl_path} ({os.path.getsize(master_jsonl_path)} bytes)")

    # 4. Write Domain-Specific JSONL Files
    domain_map = {
        "Consumer Protection": os.path.join(DOMAIN_DIR, "consumer_protection"),
        "Limitation": os.path.join(DOMAIN_DIR, "limitation"),
        "Wage & Employment": os.path.join(DOMAIN_DIR, "wage_and_employment"),
        "Rent Law": os.path.join(DOMAIN_DIR, "rent_laws")
    }

    # By Document in domains
    doc_file_map = {
        "IND-FED-CPA-2019": ("consumer_protection", "cpa_2019.jsonl"),
        "IND-FED-CPECR-2020": ("consumer_protection", "ecommerce_rules_2020.jsonl"),
        "IND-FED-CPJDR-2021": ("consumer_protection", "jurisdiction_rules_2021.jsonl"),
        "IND-FED-CPCDRC-2020": ("consumer_protection", "commission_rules_2020.jsonl"),
        "IND-FED-LIM-1963": ("limitation", "limitation_act_1963.jsonl"),
        "IND-FED-COW-2019": ("wage_and_employment", "code_on_wages_2019.jsonl"),
        "IND-FED-COSS-2020": ("wage_and_employment", "code_on_social_security_2020.jsonl"),
        "IND-FED-IRC-2020": ("wage_and_employment", "industrial_relations_code_2020.jsonl"),
        "IND-FED-PWA-1936": ("wage_and_employment", "legacy_payment_of_wages_act_1936.jsonl"),
        "IND-FED-MWA-1948": ("wage_and_employment", "legacy_minimum_wages_act_1948.jsonl"),
        "IND-FED-PGA-1972": ("wage_and_employment", "legacy_payment_of_gratuity_act_1972.jsonl"),
        "IND-FED-EPF-1952": ("wage_and_employment", "legacy_epf_act_1952.jsonl"),
        "IND-FED-IDA-1947": ("wage_and_employment", "legacy_industrial_disputes_act_1947.jsonl"),
        "IND-FED-TPA-1882": ("rent_laws", "transfer_of_property_act_1882_ch5.jsonl"),
        "IND-DL-DRCA-1958": ("rent_laws", "delhi_rent_control_act_1958.jsonl"),
        "IND-MH-MRCA-1999": ("rent_laws", "maharashtra_rent_control_act_1999.jsonl"),
        "IND-KA-KRA-1999": ("rent_laws", "karnataka_rent_act_1999.jsonl"),
        "IND-TN-TNRRRLTA-2017": ("rent_laws", "tamil_nadu_act_2017.jsonl"),
    }

    for doc_id, (subfolder, filename) in doc_file_map.items():
        doc_provs = [p for p in all_provs if p["parent_doc_id"] == doc_id]
        out_path = os.path.join(DOMAIN_DIR, subfolder, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            for p in doc_provs:
                f.write(json.dumps(p, ensure_ascii=False) + "\n")
        print(f"   - Saved {filename}: {len(doc_provs)} provisions")

    # 5. Build SQLite Database with FTS5 Search Index
    db_path = os.path.join(DATA_DIR, "corpus.db")
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE documents (
        id TEXT PRIMARY KEY,
        law_title TEXT NOT NULL,
        short_title TEXT NOT NULL,
        act_or_rule_type TEXT NOT NULL,
        act_number TEXT NOT NULL,
        jurisdiction TEXT NOT NULL,
        enactment_date TEXT NOT NULL,
        effective_date TEXT NOT NULL,
        effective_from TEXT NOT NULL,
        repealed_on TEXT,
        legal_status TEXT NOT NULL,
        legal_status_notes TEXT NOT NULL,
        official_source_url TEXT NOT NULL,
        ministry TEXT NOT NULL,
        retrieval_date TEXT NOT NULL,
        scope_category TEXT NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE provisions (
        id TEXT PRIMARY KEY,
        parent_doc_id TEXT NOT NULL,
        law_title TEXT NOT NULL,
        short_title TEXT NOT NULL,
        act_or_rule_type TEXT NOT NULL,
        jurisdiction TEXT NOT NULL,
        section_or_rule_number TEXT NOT NULL,
        section_or_rule_title TEXT NOT NULL,
        chapter_or_part TEXT NOT NULL,
        exact_text TEXT NOT NULL,
        effective_date TEXT NOT NULL,
        effective_from TEXT NOT NULL,
        repealed_on TEXT,
        enactment_date TEXT NOT NULL,
        legal_status TEXT NOT NULL,
        legal_status_notes TEXT NOT NULL,
        version_as_of_date TEXT NOT NULL,
        official_source_url TEXT NOT NULL,
        retrieval_date TEXT NOT NULL,
        scope_category TEXT NOT NULL,
        key_topics_json TEXT NOT NULL,
        cross_references_json TEXT NOT NULL,
        FOREIGN KEY (parent_doc_id) REFERENCES documents (id)
    );
    """)

    # FTS5 virtual table for BM25 ranking and fast full-text retrieval
    cur.execute("""
    CREATE VIRTUAL TABLE provisions_fts USING fts5(
        id UNINDEXED,
        law_title,
        section_or_rule_number,
        section_or_rule_title,
        exact_text,
        key_topics,
        legal_status,
        jurisdiction,
        scope_category
    );
    """)

    for d in all_docs:
        cur.execute("""
        INSERT INTO documents VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            d["id"], d["law_title"], d["short_title"], d["act_or_rule_type"], d["act_number"],
            d["jurisdiction"], d["enactment_date"], d["effective_date"], d["effective_from"],
            d["repealed_on"], d["legal_status"], d["legal_status_notes"], d["official_source_url"],
            d["ministry"], d["retrieval_date"], d["scope_category"]
        ))

    for p in all_provs:
        cur.execute("""
        INSERT INTO provisions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["id"], p["parent_doc_id"], p["law_title"], p["short_title"], p["act_or_rule_type"],
            p["jurisdiction"], p["section_or_rule_number"], p["section_or_rule_title"],
            p["chapter_or_part"], p["exact_text"], p["effective_date"], p["effective_from"],
            p["repealed_on"], p["enactment_date"], p["legal_status"], p["legal_status_notes"],
            p["version_as_of_date"], p["official_source_url"], p["retrieval_date"], p["scope_category"],
            json.dumps(p["key_topics"]), json.dumps(p["cross_references"])
        ))

        cur.execute("""
        INSERT INTO provisions_fts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            p["id"], p["law_title"], p["section_or_rule_number"], p["section_or_rule_title"],
            p["exact_text"], " ".join(p["key_topics"]), p["legal_status"], p["jurisdiction"],
            p["scope_category"]
        ))

    conn.commit()
    conn.close()
    print(f">> SQLite FTS5 database built: {db_path} ({os.path.getsize(db_path)} bytes)")

    # 6. Generate Manifest
    manifest_path = os.path.join(CORPUS_ROOT, "manifest.json")
    manifest = {
        "corpus_name": "Indian Legislation RAG Corpus",
        "generated_at": "2026-11-10T00:15:00+05:30",
        "total_documents": len(all_docs),
        "total_provisions": len(all_provs),
        "breakdown_by_domain": {
            "Consumer Protection": len([p for p in all_provs if p["scope_category"] == "Consumer Protection"]),
            "Limitation": len([p for p in all_provs if p["scope_category"] == "Limitation"]),
            "Wage & Employment": len([p for p in all_provs if p["scope_category"] == "Wage & Employment"]),
            "Rent Law": len([p for p in all_provs if p["scope_category"] == "Rent Law"]),
        },
        "breakdown_by_legal_status": {
            "In Force": len([p for p in all_provs if p["legal_status"] == "In Force"]),
            "Repealed (Active for Pre-21-Nov-2025 Claims)": len([p for p in all_provs if "Repealed" in p["legal_status"]]),
        },
        "documents_summary": [
            {
                "id": d["id"],
                "short_title": d["short_title"],
                "act_or_rule_type": d["act_or_rule_type"],
                "jurisdiction": d["jurisdiction"],
                "legal_status": d["legal_status"],
                "effective_date": d["effective_date"],
                "effective_from": d["effective_from"],
                "repealed_on": d["repealed_on"],
                "provisions_count": len([p for p in all_provs if p["parent_doc_id"] == d["id"]]),
                "official_source_url": d["official_source_url"]
            }
            for d in all_docs
        ]
    }
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print(f">> Manifest written: {manifest_path}")

    print("=================================================================")
    print("CORPUS BUILD COMPLETED SUCCESSFULLY")
    print("=================================================================")

if __name__ == "__main__":
    main()
