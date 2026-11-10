# Curated Indian Legislation Corpus for Retrieval-Augmented Generation (RAG)

A traceable, verbatim, and structured statutory corpus of Indian legislation curated specifically for Retrieval-Augmented Generation (RAG), conversational AI lawyers, and legal compliance workflows.

Every statutory record contains **exact, unparaphrased statutory text**, canonical provenance links to official Government of India portals (India Code, eGazette, Ministry and State portals), comprehensive commencement and amendment histories, and explicit legal status guardrails.

---

## 1. Statutory Scope Covered

This corpus strictly adheres to the four designated legal domains:

1. **Consumer Protection Framework**:
   - *The Consumer Protection Act, 2019 (Act No. 35 of 2019)* (Definitions, Commissions, E-filing, Remedies, Product Liability, Repeal of 1986 Act).
   - *Consumer Protection (E-Commerce) Rules, 2020 (G.S.R. 462(E))* (Rules 1 to 8: marketplace and inventory liability, grievance officer 48h/1mo deadlines, refund rules).
   - *Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021 (G.S.R. 912(E))* (Pecuniary jurisdiction: District $\le$ ₹50 Lakh; State ₹50 Lakh to ₹2 Crore; National > ₹2 Crore).
   - *Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020 (G.S.R. 449(E))* (Fee schedules: nil fee up to ₹5 Lakh).

2. **The Limitation Act, 1963 (Act No. 36 of 1963)**:
   - *Substantive Sections*: Section 1 to 29 (Bar of limitation s. 3, condonation in appeals/applications only s. 5, legal disability s. 6, exclusion of certified copy time s. 12, wrong forum in good faith s. 14, fraud/mistake s. 17, written acknowledgment clock-reset s. 18, part-payment s. 19, savings for special acts s. 29(2)).
   - *Schedule Articles for Common Civil Claims*: Article 7 (wages: 3 years), Article 8 (hotel dues: 3 years), Article 19 (loans: 3 years), Article 22 (security deposits: 3 years from demand), Article 24 (money had and received / refunds: 3 years), Article 47 (failure of consideration / cancelled contract: 3 years), Article 52 (rent arrears: 3 years), Article 55 (contract breach: 3 years), Article 66 & 67 (landlord recovery of possession: 12 years), Article 113 (residuary civil suit: 3 years), Article 137 (residuary application: 3 years).

3. **Wage and Employment Laws (Private Sector Only)**:
   - *Target Claims*: Salaried, contract, and daily-wage employees with unpaid/delayed wages, unauthorized deductions, overtime, minimum wages, final settlement upon resignation or termination, gratuity, and retrenchment compensation.
   - *Sources Curated*:
     - **The Code on Wages, 2019 (Act No. 29 of 2019)** (ss. 1, 2(y) wage definition and 50% allowance cap, 6, 13, 14 overtime, 15 mode, 16 wage period, 17 time of payment and **2 working days final settlement**, 18 deductions and 50% cap, 45 claims before Authority, 67 repeal).
     - **The Code on Social Security, 2020 (Act No. 36 of 2020)** [Gratuity & PF only] (ss. 16, 17 PF contributions, 53 gratuity eligibility and fixed-term inclusion, 54 continuous service, 55 30-day payment & interest, 164 repeal).
     - **The Industrial Relations Code, 2020 (Act No. 35 of 2020)** [Termination & Retrenchment only] (ss. 2(zh) retrenchment, 70 conditions precedent, 79 establishments with 300+ workers, 83 Worker Reskilling Fund, 104 repeal).
     - **Active Interim Legacy Framework**: *Payment of Wages Act, 1936* (s. 5(2) 2-day termination payment, s. 15 claims); *Payment of Gratuity Act, 1972* (s. 4 eligibility, s. 7 30-day rule); *Industrial Disputes Act, 1947* (s. 25F retrenchment compensation, s. 33C recovery before Labour Court).
   - *Out of Scope Excluded*: Government employees, gig/platform workers, workplace sexual harassment, maternity benefits, workplace safety.

4. **Rent Laws (Selected Jurisdictions & Central Fallback)**:
   - **Central Fallback**: *Transfer of Property Act, 1882 (ss. 105-117)* (Lease definition, 15-day notice to quit s. 106, 11-month lease origin s. 107, quiet enjoyment & repair deductions s. 108, determination of lease s. 111, relief against forfeiture s. 114, holding over s. 116).
   - **Delhi**: *The Delhi Rent Control Act, 1958* (Section 3(c) ₹3,500/month threshold excluding modern tenancies to TPA 1882; Section 14 eviction grounds).
   - **Maharashtra**: *The Maharashtra Rent Control Act, 1999* (Section 3 corporate exemptions; Section 24 summary eviction and double license fee for overstay; Section 55 mandatory written registered agreement under penalty of imprisonment).
   - **Karnataka**: *The Karnataka Rent Act, 1999* (Section 2(3)(e) ₹3,500/month threshold in Bengaluru; Section 4 compulsory registration; Section 27 eviction).
   - **Tamil Nadu**: *The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017* (Repealed 1960 Act; Section 4 portal registration; Section 9 3-month rent revision notice; Section 11 **statutory cap of 3 months rent on residential security deposits**; Section 22 double/quadruple rent holding over penalty).

---

## 2. Directory Structure

```text
corpus/
├── data/
│   ├── indian_legal_corpus.json       # Master hierarchical JSON (Documents + Provisions)
│   ├── provisions.jsonl               # Streamable JSONL for embeddings and RAG vector stores
│   └── corpus.db                      # SQLite relational database with FTS5 BM25 search
├── provisions_by_domain/              # Domain-partitioned JSONL files
│   ├── consumer_protection/
│   │   ├── cpa_2019.jsonl
│   │   ├── ecommerce_rules_2020.jsonl
│   │   ├── jurisdiction_rules_2021.jsonl
│   │   └── commission_rules_2020.jsonl
│   ├── limitation/
│   │   └── limitation_act_1963.jsonl
│   ├── wage_and_employment/
│   │   ├── code_on_wages_2019.jsonl
│   │   ├── code_on_social_security_2020.jsonl
│   │   ├── industrial_relations_code_2020.jsonl
│   │   └── legacy_employment_acts_interim.jsonl
│   └── rent_laws/
│       ├── transfer_of_property_act_1882_ch5.jsonl
│       ├── delhi_rent_control_act_1958.jsonl
│       ├── maharashtra_rent_control_act_1999.jsonl
│       ├── karnataka_rent_act_1999.jsonl
│       └── tamil_nadu_act_2017.jsonl
├── scripts/
│   ├── build_corpus.py                # Validation and corpus compilation pipeline
│   └── provisions/                    # Statutory text definitions with strict provenance
│       ├── consumer_data.py
│       ├── limitation_data.py
│       ├── employment_data.py
│       └── rent_data.py
├── corpus_rag_engine.py               # Production RAG search CLI with BM25 & legal guardrails
├── legal_status_audit.md              # In-depth legislative status report & gazette analysis
├── manifest.json                      # Corpus inventory, stats, and document summaries
└── README.md                          # Comprehensive documentation
```

---

## 3. Structured Record Schema

Every provision in `data/provisions.jsonl` and `data/corpus.db` adheres strictly to this schema:

| Field Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `id` | `string` | Unique provision identifier | `IND-FED-CPA-2019-SEC-034` |
| `parent_doc_id` | `string` | Foreign key to parent legislative document | `IND-FED-CPA-2019` |
| `law_title` | `string` | Official statutory title | `The Consumer Protection Act, 2019` |
| `short_title` | `string` | Common abbreviated title | `Consumer Protection Act, 2019` |
| `act_or_rule_type` | `string` | Classification (`Central Act`, `Central Rule`, `State Act`) | `Central Act` |
| `jurisdiction` | `string` | Territory / Federal classification | `Central (Union of India)` |
| `section_or_rule_number` | `string` | Provision number | `Section 34` |
| `section_or_rule_title` | `string` | Official heading of the provision | `Jurisdiction of District Commission` |
| `chapter_or_part` | `string` | Chapter, Part, or Schedule | `Chapter IV: Consumer Disputes Redressal Commission` |
| `exact_text` | `string` | **Verbatim statutory text** (no paraphrasing) | `(1) Subject to the other provisions...` |
| `effective_date` | `string` | Date brought into force via Gazette notification | `2020-07-20` |
| `effective_from` | `string` | Machine-comparable ISO date of commencement | `2020-07-20` |
| `repealed_on` | `string \| null` | Machine-comparable ISO date of repeal (null if in force) | `null` or `2025-11-21` |
| `enactment_date` | `string` | Date of Presidential / Gubernatorial assent | `2019-08-09` |
| `legal_status` | `string` | `In Force` \| `Repealed (Active for Pre-21-Nov-2025 Claims)` | `In Force` |
| `legal_status_notes` | `string` | Analysis of commencement, gazette S.O., and savings clauses | Explains S.O. 5322(E) commencement and s. 67 savings |
| `version_as_of_date` | `string` | Current corpus verification date | `2026-11-10` |
| `official_source_url` | `string` | Canonical link to India Code / Ministry / Gazette | `https://www.indiacode.nic.in/handle/123456789/15256` |
| `retrieval_date` | `string` | Date recorded | `2026-11-09` |
| `scope_category` | `string` | Domain category | `Consumer Protection` |
| `key_topics` | `list[str]` | Keywords and concepts for hybrid search | `["pecuniary jurisdiction", "District Commission"]` |
| `cross_references` | `list[str]` | Linked provisions or parent rules | `["IND-FED-CPJDR-2021-RULE-003", "Section 35"]` |

---

## 4. Critical Legal Status Guardrails for AI Systems

A common failure mode of AI legal systems is hallucinating that newly passed enactments are in force before notification, or claiming repealed statutes cannot be referenced when a claim actually arose prior to repeal. This corpus incorporates explicit temporal guardrails:

### Guardrail A: The Labour Codes Commencement & Dual Temporal Coverage
- **The Reality**: The 4 Labour Codes came into force across India on **21 November 2025** via official Gazette Notifications:
  - *Code on Wages, 2019*: **S.O. 5322(E)**
  - *Industrial Relations Code, 2020*: **S.O. 5320(E)**
  - *Code on Social Security, 2020*: **S.O. 5323(E)**
- **Repeal & Savings Architecture**: Section 67 COW, Section 164 COSS, and Section 104 IRC repealed the legacy Central Acts (Payment of Wages Act 1936, Minimum Wages Act 1948, Payment of Gratuity Act 1972, EPF Act 1952, Industrial Disputes Act 1947). However, under Section 6 of the General Clauses Act, 1897 and statutory savings clauses, **claims and disputes where the cause of action arose before 21 November 2025 remain actionable under the legacy Acts**.
- **How Handled in Corpus**:
  1. Every chunk carries `effective_from` and `repealed_on`.
  2. Both the new Labour Codes (`effective_from: "2025-11-21"`, `repealed_on: null`, `legal_status: "In Force"`) and the legacy Acts (`repealed_on: "2025-11-21"`, `legal_status: "Repealed (Active for Pre-21-Nov-2025 Claims)"`) are indexed with verbatim text.
  3. The RAG engine compares the case dispute date (`--case-date`) against `2025-11-21`. If a dispute arose prior to 21-Nov-2025, it raises the explicit flag:
     `period_may_fall_under_repealed_acts = True`
     and alerts the LLM to apply the legacy statutory scheme while prioritizing legacy provisions.

### Guardrail B: Pecuniary Ceilings under Consumer Protection Act, 2019
- **The Trap**: Section 34 of the CPA 2019 statute text reads "does not exceed one crore rupees".
- **The Reality**: On 30 December 2021, the Central Government promulgated **G.S.R. 912(E)**, lowering the District Commission ceiling to **₹50 Lakh**, setting the State Commission between **₹50 Lakh and ₹2 Crore**, and the National Commission above **₹2 Crore**.
- **How Handled in Corpus**: Both Section 34 and Rule 3 of the 2021 Rules are cross-referenced with explicit warnings.

### Guardrail C: Delhi Rent Control Act ₹3,500 Monetary Ceiling
- **The Reality**: Under Section 3(c) of the Delhi Rent Control Act, 1958, properties with monthly rent exceeding **₹3,500** are exempt from rent control.
- **Practical Consequence**: Modern residential tenancies in Delhi almost universally fall under the **Transfer of Property Act, 1882 (ss. 105-117)** before ordinary civil courts.

---

## 5. How to Ingest & Query the Corpus

### Quick Test via CLI
The corpus includes `corpus_rag_engine.py` featuring precision BM25 ranking, phrase-aware scoring, and temporal flag derivation:

```bash
# Run the built-in 7-case test suite (including the resignation unpaid wages eval)
python3 corpus_rag_engine.py --test

# Query for unpaid wages upon resignation for a post-21-Nov-2025 dispute:
python3 corpus_rag_engine.py -q "unpaid wages resignation two working days" -s "Wage & Employment" -d "2026-03-01" --format-llm

# Query for a dispute occurring BEFORE 21 November 2025 (triggers period_may_fall_under_repealed_acts):
python3 corpus_rag_engine.py -q "unpaid wages resignation two working days" -s "Wage & Employment" -d "2025-06-15" --format-llm

# Query for security deposit refund in Tamil Nadu (statutory 3-month cap under TNRRRLT Act 2017)
python3 corpus_rag_engine.py -q "security deposit refund three months" -j "Tamil Nadu" -s "Rent Law" --format-llm
```

### Python RAG Integration Example

```python
import sqlite3
import json

conn = sqlite3.connect("data/corpus.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

# Search using SQLite FTS5 BM25
query = "two working days final settlement resignation"
cur.execute("""
    SELECT p.law_title, p.section_or_rule_number, p.section_or_rule_title, 
           p.legal_status, p.exact_text, p.official_source_url
    FROM provisions_fts fts
    JOIN provisions p ON p.id = fts.id
    WHERE provisions_fts MATCH ?
    ORDER BY fts.rank ASC LIMIT 3
""", (query,))

for row in cur.fetchall():
    print(f"[{row['law_title']}] {row['section_or_rule_number']}: {row['section_or_rule_title']}")
    print(f"Status: {row['legal_status']}")
    print(f"Statutory Text:\n{row['exact_text']}\n")
```

---

## 6. Verification and Rebuilding

To re-validate all schema constraints and regenerate database tables from source modules:

```bash
python3 scripts/build_corpus.py
```
