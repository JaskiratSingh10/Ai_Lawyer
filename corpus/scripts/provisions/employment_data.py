"""
Wage and Employment Laws statutory data module:
Updated with the official commencement of the Labour Codes on 21 November 2025:
- The Code on Wages, 2019 (Act No. 29 of 2019) [In Force w.e.f. 2025-11-21 via S.O. 5322(E)]
- The Code on Social Security, 2020 (Act No. 36 of 2020) [In Force w.e.f. 2025-11-21 via S.O. 5323(E)]
- The Industrial Relations Code, 2020 (Act No. 35 of 2020) [In Force w.e.f. 2025-11-21 via S.O. 5320(E)]
- Full Fallback Legacy Acts [Repealed on 2025-11-21, active for pre-21-Nov-2025 claims under savings provisions]:
  * Payment of Wages Act, 1936 (Act 4 of 1936)
  * Minimum Wages Act, 1948 (Act 11 of 1948)
  * Payment of Gratuity Act, 1972 (Act 39 of 1972)
  * Employees' Provident Funds and Miscellaneous Provisions Act, 1952 (Act 19 of 1952)
  * Industrial Disputes Act, 1947 (Act 14 of 1947)
"""

DOCUMENTS = [
    {
        "id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 29 of 2019",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "2019-08-08",
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "COMMENCEMENT VERIFICATION: Enacted on 8 August 2019. Brought fully into force across India on "
            "21 November 2025 vide Ministry of Labour and Employment Notification S.O. 5322(E) published in "
            "the Gazette of India. Section 67 thereof formally repealed the Payment of Wages Act 1936 and "
            "the Minimum Wages Act 1948 w.e.f. 21 November 2025."
        ),
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    },
    {
        "id": "IND-FED-COSS-2020",
        "law_title": "The Code on Social Security, 2020",
        "short_title": "Code on Social Security, 2020 (Gratuity and PF parts)",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 36 of 2020",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "2020-09-28",
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "COMMENCEMENT VERIFICATION: Enacted on 28 September 2020. Brought into force on 21 November 2025 "
            "vide Ministry of Labour and Employment Notification S.O. 5323(E). Section 164 thereof formally repealed "
            "the Payment of Gratuity Act 1972 and Employees' Provident Funds & Miscellaneous Provisions Act 1952 "
            "w.e.f. 21 November 2025."
        ),
        "official_source_url": "https://labour.gov.in/sites/default/files/SS_Code_Gazette.pdf",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    },
    {
        "id": "IND-FED-IRC-2020",
        "law_title": "The Industrial Relations Code, 2020",
        "short_title": "Industrial Relations Code, 2020 (Termination and Retrenchment parts)",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 35 of 2020",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "2020-09-28",
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "COMMENCEMENT VERIFICATION: Enacted on 28 September 2020. Brought into force on 21 November 2025 "
            "vide Ministry of Labour and Employment Notification S.O. 5320(E). Section 104 thereof formally repealed "
            "the Industrial Disputes Act, 1947 w.e.f. 21 November 2025."
        ),
        "official_source_url": "https://labour.gov.in/sites/default/files/IR_Gazette_of_India.pdf",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    },
    {
        "id": "IND-FED-PWA-1936",
        "law_title": "The Payment of Wages Act, 1936",
        "short_title": "Payment of Wages Act, 1936",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 4 of 1936",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "1936-04-23",
        "effective_date": "1937-03-28",
        "effective_from": "1937-03-28",
        "repealed_on": "2025-11-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "Repealed on 21 November 2025 by Section 67(1) of the Code on Wages, 2019. Under Section 67(2) read with "
            "Section 6 of the General Clauses Act, 1897, continues to apply to causes of action, unpaid wage claims, "
            "and disputes that arose prior to 21 November 2025."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2381",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    },
    {
        "id": "IND-FED-MWA-1948",
        "law_title": "The Minimum Wages Act, 1948",
        "short_title": "Minimum Wages Act, 1948",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 11 of 1948",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "1948-03-15",
        "effective_date": "1948-03-15",
        "effective_from": "1948-03-15",
        "repealed_on": "2025-11-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "Repealed on 21 November 2025 by Section 67(1) of the Code on Wages, 2019. Governs minimum wage "
            "claims and overtime rates for work performed prior to 21 November 2025."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1511",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    },
    {
        "id": "IND-FED-PGA-1972",
        "law_title": "The Payment of Gratuity Act, 1972",
        "short_title": "Payment of Gratuity Act, 1972",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 39 of 1972",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "1972-08-21",
        "effective_date": "1972-09-16",
        "effective_from": "1972-09-16",
        "repealed_on": "2025-11-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "Repealed on 21 November 2025 by Section 164(1)(f) of the Code on Social Security, 2020. "
            "Governs gratuity claims and disputes for employees whose employment terminated prior to 21 November 2025."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1512",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    },
    {
        "id": "IND-FED-EPF-1952",
        "law_title": "The Employees' Provident Funds and Miscellaneous Provisions Act, 1952",
        "short_title": "Employees' Provident Funds Act, 1952",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 19 of 1952",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "1952-03-04",
        "effective_date": "1952-11-01",
        "effective_from": "1952-11-01",
        "repealed_on": "2025-11-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "Repealed on 21 November 2025 by Section 164(1)(c) of the Code on Social Security, 2020. "
            "Governs PF compliance, contributions, and recovery for periods prior to 21 November 2025."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1513",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    },
    {
        "id": "IND-FED-IDA-1947",
        "law_title": "The Industrial Disputes Act, 1947",
        "short_title": "Industrial Disputes Act, 1947",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 14 of 1947",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "1947-03-11",
        "effective_date": "1947-04-01",
        "effective_from": "1947-04-01",
        "repealed_on": "2025-11-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "Repealed on 21 November 2025 by Section 104(1) of the Industrial Relations Code, 2020. "
            "Governs retrenchment compensation, closure notice, and recovery applications (s. 33C) for events "
            "occurring prior to 21 November 2025."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2380",
        "ministry": "Ministry of Labour and Employment",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
    }
]

PROVISIONS = [
    # =========================================================================
    # CODE ON WAGES, 2019 (In Force w.e.f. 2025-11-21)
    # =========================================================================
    {
        "id": "IND-FED-COW-2019-SEC-001",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 1",
        "section_or_rule_title": "Short title, extent and commencement",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "(1) This Act may be called the Code on Wages, 2019.\n"
            "(2) It extends to the whole of India.\n"
            "(3) It shall come into force on such date as the Central Government may, by notification in the Official Gazette, appoint; "
            "and different dates may be appointed for different provisions of this Code and any reference in any such provision to "
            "the commencement of this Code shall be construed as a reference to the coming into force of that provision."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "Brought into force w.e.f. 21 November 2025 vide Gazette Notification S.O. 5322(E).",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["short title", "extent", "commencement", "notification power"],
        "cross_references": ["Section 42", "Section 67", "S.O. 5322(E)"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-002",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 2",
        "section_or_rule_title": "Definitions (Operative Private-Sector Clauses)",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "In this Code, unless the context otherwise requires,—\n"
            "(f) 'contractor', in relation to an establishment, means a person, who— (i) undertakes to produce a given result for the establishment, other than a mere supply of goods or articles of manufacture to such establishment, through contract labour; or (ii) supplies contract labour for any work of the establishment as mere human resource and includes a sub-contractor;\n"
            "(g) 'contract labour' means a worker who shall be deemed to be employed in or in connection with the work of an establishment when he is hired in or in connection with such work by or through a contractor, with or without the knowledge of the principal employer...;\n"
            "(k) 'employee' means, any person (other than an apprentice engaged under the Apprentices Act, 1961), employed on wages by an establishment to do any skilled, semi-skilled or unskilled, manual, operational, supervisory, managerial, administrative, technical or clerical work for hire or reward, whether the terms of employment be express or implied, and also includes a person declared to be an employee by the appropriate Government, but does not include any member of the Armed Forces of the Union;\n"
            "(l) 'employer' means a person who employs, whether directly or through any person, or on his behalf or on behalf of any person, one or more employees in his establishment...;\n"
            "(y) 'wages' means all remuneration whether by way of salaries, allowances or otherwise, expressed in terms of money or capable of being so expressed which would, if the terms of employment, express or implied, were fulfilled, be payable to a person employed in respect of his employment or of work done in such employment, and includes basic pay, dearness allowance, and retaining allowance, but excludes bonus, HRA, PF contributions, conveyance, overtime allowance, gratuity, and retrenchment compensation:\n"
            "Provided that, for calculating the wages under this clause, if payments made by the employer to the employee under excluded clauses exceeds one-half (50%), or such other per cent. as may be notified, of all remuneration calculated under this clause, the amount which exceeds such one-half, or the per cent. so notified, shall be deemed as remuneration and shall be accordingly added in wages under this clause;\n"
            "(z) 'worker' means any person employed in any industry to do any manual, unskilled, skilled, technical, operational, clerical or supervisory work for hire or reward... but does not include any such person who is employed mainly in a managerial or administrative capacity, or who, being employed in a supervisory capacity, draws wages exceeding fifteen thousand rupees per month."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. 50% cap on excluded allowances.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["employee", "employer", "contract labour", "wages definition", "worker", "fifty percent cap on allowances"],
        "cross_references": ["Section 6", "Section 14", "Section 15", "Section 17", "Section 18"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-006",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 6",
        "section_or_rule_title": "Fixation of minimum rate of wages",
        "chapter_or_part": "Chapter II: Minimum Wages",
        "exact_text": (
            "(1) Subject to the provisions of section 9, the appropriate Government shall fix the minimum rates of wages payable to employees in accordance with the provisions of section 8.\n"
            "(2) For the purpose of sub-section (1), the appropriate Government may fix a minimum rate of wages for time work or piece work.\n"
            "(6) In fixing minimum rates of wages under this section, the appropriate Government shall take into account the skill of workers (unskilled, skilled, semi-skilled, highly-skilled) and geographical area."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["minimum wages", "time work", "piece work", "skill categories", "geographic area"],
        "cross_references": ["Section 8", "Section 9", "Section 14"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-013",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 13",
        "section_or_rule_title": "Fixing hours of work for normal working day",
        "chapter_or_part": "Chapter II: Minimum Wages",
        "exact_text": (
            "(1) Where the minimum rates of wages have been fixed under this Code, the appropriate Government may—\n"
            "(a) fix the number of hours of work which shall constitute a normal working day, inclusive of one or more specified intervals;\n"
            "(b) provide for a day of rest in every period of seven days which shall be allowed to all employees and for payment of remuneration in respect of such days of rest;\n"
            "(c) provide for payment for work on a day of rest at a rate not less than the overtime rate."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["normal working day", "hours of work", "weekly rest day", "rest day wages"],
        "cross_references": ["Section 14"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-014",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 14",
        "section_or_rule_title": "Wages for overtime work",
        "chapter_or_part": "Chapter II: Minimum Wages",
        "exact_text": (
            "Where an employee whose minimum rate of wages has been fixed under this Code works on any day in excess of "
            "the number of hours constituting a normal working day, the employer shall pay him for every hour or for part of "
            "an hour so worked in excess, at the overtime rate which shall not be less than twice the normal rate of wages."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. Overtime at not less than twice normal wages.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["overtime wages", "twice normal rate", "double rate", "work in excess of normal hours"],
        "cross_references": ["Section 13", "Section 17"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-015",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 15",
        "section_or_rule_title": "Mode of payment of wages",
        "chapter_or_part": "Chapter III: Payment of Wages",
        "exact_text": (
            "All wages shall be paid in current coin or currency notes or by cheque or by crediting the wages in the bank account "
            "of the employee or by the electronic mode."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. Authorizes bank transfer, electronic mode, cheque, or currency notes.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["mode of payment", "bank account", "cheque", "electronic mode", "currency notes"],
        "cross_references": ["Section 16", "Section 17"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-016",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 16",
        "section_or_rule_title": "Fixation of wage period",
        "chapter_or_part": "Chapter III: Payment of Wages",
        "exact_text": (
            "The employer shall fix the wage period for employees either as daily, weekly, fortnightly or monthly, "
            "and no wage period shall exceed one month."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. Prohibits wage periods exceeding one month.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["wage period", "daily", "weekly", "fortnightly", "monthly", "max one month"],
        "cross_references": ["Section 17"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-017",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 17",
        "section_or_rule_title": "Time limit for payment of wages and final settlement after resignation or termination",
        "chapter_or_part": "Chapter III: Payment of Wages",
        "exact_text": (
            "(1) The employer shall pay or cause to be paid wages to the employees, engaged on—\n"
            "(i) daily basis, at the end of the shift;\n"
            "(ii) weekly basis, on the last working day of the week, that is to say, before the weekly holiday;\n"
            "(iii) fortnightly basis, before the end of the second day after the end of the fortnight;\n"
            "(iv) monthly basis, before the expiry of the seventh day of the succeeding month.\n"
            "(2) Where an employee has been—\n"
            "(i) removed or dismissed from service; or\n"
            "(ii) retrenched or has resigned from service, or became unemployed due to closure of the establishment,\n"
            "the wages payable to him shall be paid within two working days of his removal, dismissal, retrenchment or, as the case may be, his resignation.\n"
            "(3) Notwithstanding anything contained in sub-section (1) or sub-section (2), the appropriate Government may, having regard to the size and nature of establishment, by notification, extend the time limit of payment of wages in such conditions as may be specified in such notification."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": (
            "CRITICAL IN-FORCE SETTLEMENT RULE: In force w.e.f. 21 November 2025. Section 17(2) explicitly mandates payment "
            "of all wages within TWO WORKING DAYS of resignation, removal, dismissal, retrenchment, or closure."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["time limit for payment", "seventh day of succeeding month", "resignation", "termination", "retrenchment", "two working days final settlement", "unpaid wages", "second working day"],
        "cross_references": ["IND-FED-PWA-1936-SEC-005", "Section 18", "Section 45"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-018",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 18",
        "section_or_rule_title": "Deductions which may be made from wages",
        "chapter_or_part": "Chapter III: Payment of Wages",
        "exact_text": (
            "(1) Notwithstanding anything contained in any other law for the time being in force, there shall be no deductions from the wages of the employee, except those authorised under this Code.\n"
            "Explanation.—Every payment made by the employee to the employer or his agent shall be deemed to be a deduction from his wages.\n"
            "(2) Deductions from the wages of an employee shall be made only in accordance with the provisions of this Code, and may be made only for the following purposes, namely:—\n"
            "(a) fines imposed on him;\n"
            "(b) deductions for his absence from duty;\n"
            "(c) deductions for damage to or loss of goods expressly entrusted to the employee for custody, or for loss of money for which he is required to account, where such damage or loss is directly attributable to his neglect or default;\n"
            "(d) deductions for house-accommodation supplied by the employer or by appropriate Government...;\n"
            "(f) deductions for recovery of advances of whatever nature... and loans granted...;\n"
            "(h) deductions for payment to co-operative societies...;\n"
            "(i) deductions made with the written authorisation of the employee, for payment of life insurance premium or PF contribution...;\n"
            "(3) Notwithstanding anything contained in this Code and subject to any other law for the time being in force, the total amount of deductions which may be made under sub-section (2) in any wage period from the wages of an employee shall not exceed fifty per cent. of such wages."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. Exhaustively lists lawful deductions and caps total deductions at 50% of wages.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["deductions from wages", "unlawful deductions", "fines", "absence from duty", "damage or loss", "advances", "fifty percent deduction limit"],
        "cross_references": ["Section 17", "Section 45", "IND-FED-PWA-1936-SEC-007"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-045",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 45",
        "section_or_rule_title": "Claims under Code and procedure",
        "chapter_or_part": "Chapter V: Claims",
        "exact_text": (
            "(1) The appropriate Government may, by notification, appoint one or more authorities, not below the rank of a Gazetted Officer, "
            "to hear and determine the claims which arises under the provisions of this Code.\n"
            "(2) The authority appointed under sub-section (1), while deciding the claim under that sub-section, may order, having regard to "
            "the circumstances under which the claim arises, the payment of compensatory amount in addition to the claim amount which "
            "may extend to ten times of the claim amount and the employer shall be liable to pay such amount.\n"
            "(3) An application under sub-section (1) may be filed by the employee concerned, or any Trade Union registered under the Trade Unions Act, 1926... or the Inspector-cum-Facilitator.\n"
            "(6) An application under sub-section (1) shall be presented within a period of three years from the date on which the claim arose: "
            "Provided that the authority may admit an application after the expiry of the said period of three years, if the applicant satisfies "
            "the authority that he had sufficient cause for not making the application within such period."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. 3 years limitation for filing wage claims; up to ten times compensation for delayed/unpaid wages.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["wage claims", "claims authority", "ten times compensation", "three years limitation", "delayed wages recovery", "condonation of delay"],
        "cross_references": ["Section 17", "Section 18", "IND-FED-PWA-1936-SEC-015"]
    },
    {
        "id": "IND-FED-COW-2019-SEC-067",
        "parent_doc_id": "IND-FED-COW-2019",
        "law_title": "The Code on Wages, 2019",
        "short_title": "Code on Wages, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 67",
        "section_or_rule_title": "Repeal and savings",
        "chapter_or_part": "Chapter VIII: Miscellaneous",
        "exact_text": (
            "(1) The Payment of Wages Act, 1936, the Minimum Wages Act, 1948, the Payment of Bonus Act, 1965 and the Equal Remuneration Act, 1976 are hereby repealed.\n"
            "(2) Notwithstanding such repeal, anything done or any action taken or purported to have been done or taken under the enactments hereby repealed shall, in so far as it is not inconsistent with the provisions of this Code, be deemed to have been done or taken under the corresponding provisions of this Code.\n"
            "(3) The mention of particular matters in sub-section (2) shall not be held to prejudice or affect the general application of section 6 of the General Clauses Act, 1897 with regard to the effect of repeal."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2019-08-08",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Operative w.e.f. 21 November 2025. Expressly repealed Payment of Wages Act 1936 and Minimum Wages Act 1948 "
            "subject to Section 6 of the General Clauses Act, 1897 savings for pre-21-Nov-2025 rights and liabilities."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/the_code_on_wages_2019_no._29_of_2019.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["repeal and savings", "Payment of Wages Act 1936", "Minimum Wages Act 1948", "General Clauses Act 1897"],
        "cross_references": ["Section 1", "IND-FED-PWA-1936", "IND-FED-MWA-1948"]
    },

    # =========================================================================
    # CODE ON SOCIAL SECURITY, 2020 (In Force w.e.f. 2025-11-21) - Gratuity & PF
    # =========================================================================
    {
        "id": "IND-FED-COSS-2020-SEC-016",
        "parent_doc_id": "IND-FED-COSS-2020",
        "law_title": "The Code on Social Security, 2020",
        "short_title": "Code on Social Security, 2020 (PF parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 16",
        "section_or_rule_title": "Schemes (Employees' Provident Fund, Pension, and Insurance)",
        "chapter_or_part": "Chapter III: Employees' Provident Fund",
        "exact_text": (
            "(1) The Central Government may, by notification—\n"
            "(a) frame a scheme to be called the Employees' Provident Fund Scheme for the establishment of provident funds under this Chapter for employees or for any class of employees...;\n"
            "(b) frame a scheme to be called the Employees' Pension Scheme...;\n"
            "(c) frame a scheme to be called the Employees' Deposit-Linked Insurance Scheme..."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025 vide S.O. 5323(E). Replaced Section 5 of EPF Act 1952.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/SS_Code_Gazette.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["provident fund", "pension scheme", "deposit-linked insurance", "EPF"],
        "cross_references": ["Section 17", "Section 164"]
    },
    {
        "id": "IND-FED-COSS-2020-SEC-017",
        "parent_doc_id": "IND-FED-COSS-2020",
        "law_title": "The Code on Social Security, 2020",
        "short_title": "Code on Social Security, 2020 (PF parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 17",
        "section_or_rule_title": "Contributions to Provident Fund",
        "chapter_or_part": "Chapter III: Employees' Provident Fund",
        "exact_text": (
            "(1) The contribution which shall be paid by the employer to the Fund shall be ten per cent. of the wages for the time being payable to each of the employees (whether employed by him directly or by or through a contractor), and the employee's contribution shall be equal to the contribution payable by the employer in respect of him:\n"
            "Provided that the Central Government may, by notification, specify twelve per cent. for certain establishments.\n"
            "(2) The employer shall pay employee's contribution that is so deducted by him from the wages of the employee, into the Fund within such period as may be specified in the Provident Fund Scheme."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. 10% or 12% statutory PF contributions.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/SS_Code_Gazette.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["PF contribution", "ten percent", "twelve percent", "employer contribution", "employee contribution", "contract labour PF"],
        "cross_references": ["Section 16", "IND-FED-EPF-1952-SEC-006"]
    },
    {
        "id": "IND-FED-COSS-2020-SEC-053",
        "parent_doc_id": "IND-FED-COSS-2020",
        "law_title": "The Code on Social Security, 2020",
        "short_title": "Code on Social Security, 2020 (Gratuity parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 53",
        "section_or_rule_title": "Payment of gratuity",
        "chapter_or_part": "Chapter V: Gratuity",
        "exact_text": (
            "(1) Gratuity shall be payable to an employee on the termination of his employment after he has rendered continuous service for not less than five years,—\n"
            "(a) on his superannuation; or\n"
            "(b) on his retirement or resignation; or\n"
            "(c) on his death or disablement due to accident or disease; or\n"
            "(d) on termination of his contract period under fixed term employment; or\n"
            "(e) on happening of any such event as may be notified by the Central Government:\n"
            "Provided that the completion of continuous service of five years shall not be necessary where the termination of the employment of any employee is due to death or disablement or expiration of fixed term employment:\n"
            "Provided further that in the case of fixed term employment or a deceased employee, the employer shall pay gratuity on pro rata basis:\n"
            "Provided also that in the case of working journalist, the expression 'five years' shall be read as 'three years'.\n"
            "(2) For every completed year of service or part thereof in excess of six months, the employer shall pay gratuity to an employee at the rate of fifteen days' wages based on the rate of wages last drawn by the employee concerned."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": (
            "In force w.e.f. 21 November 2025. Extends gratuity to fixed-term employees pro-rata without 5-year barrier. "
            "15 days wages per completed year of service on resignation/retirement."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/SS_Code_Gazette.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["gratuity eligibility", "five years continuous service", "fixed term employment", "resignation", "retirement", "fifteen days wages per year"],
        "cross_references": ["Section 54", "Section 55", "IND-FED-PGA-1972-SEC-004"]
    },
    {
        "id": "IND-FED-COSS-2020-SEC-054",
        "parent_doc_id": "IND-FED-COSS-2020",
        "law_title": "The Code on Social Security, 2020",
        "short_title": "Code on Social Security, 2020 (Gratuity parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 54",
        "section_or_rule_title": "Continuous service calculation",
        "chapter_or_part": "Chapter V: Gratuity",
        "exact_text": (
            "For the purposes of this Chapter,—\n"
            "(1) an employee shall be said to be in continuous service for a period if he has, for that period, been in uninterrupted service...\n"
            "(2) where an employee is not in continuous service for one year, he shall be deemed to be in continuous service if he has actually worked under the employer for not less than 240 days (190 days in mines or 5-day week establishments)."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. 240 days rule.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/SS_Code_Gazette.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["continuous service", "240 days rule", "uninterrupted service", "gratuity computation"],
        "cross_references": ["Section 53"]
    },
    {
        "id": "IND-FED-COSS-2020-SEC-055",
        "parent_doc_id": "IND-FED-COSS-2020",
        "law_title": "The Code on Social Security, 2020",
        "short_title": "Code on Social Security, 2020 (Gratuity parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 55",
        "section_or_rule_title": "Determination and payment of amount of gratuity",
        "chapter_or_part": "Chapter V: Gratuity",
        "exact_text": (
            "(1) A person who is eligible for payment of gratuity under this Chapter shall send a written application to the employer...\n"
            "(2) As soon as gratuity becomes payable, the employer shall, whether an application has been made or not, determine the amount of gratuity and give notice in writing to the employee and competent authority...\n"
            "(3) The employer shall arrange to pay the amount of gratuity within thirty days from the date it becomes payable.\n"
            "(4) If the amount of gratuity is not paid within thirty days, the employer shall pay simple interest at the rate notified by the Central Government from the date it became payable to the date of payment."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. Mandates payment within 30 days and simple interest on delay.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/SS_Code_Gazette.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["gratuity determination", "thirty days timeline", "simple interest on delay", "competent authority"],
        "cross_references": ["Section 53", "IND-FED-PGA-1972-SEC-007"]
    },
    {
        "id": "IND-FED-COSS-2020-SEC-164",
        "parent_doc_id": "IND-FED-COSS-2020",
        "law_title": "The Code on Social Security, 2020",
        "short_title": "Code on Social Security, 2020 (Repeal parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 164",
        "section_or_rule_title": "Repeal and savings",
        "chapter_or_part": "Chapter XIV: Miscellaneous",
        "exact_text": (
            "(1) The following Acts are hereby repealed, namely:— (c) the Employees' Provident Funds and Miscellaneous Provisions Act, 1952; (f) the Payment of Gratuity Act, 1972...\n"
            "(2) Notwithstanding such repeal, anything done or any action taken under the enactments hereby repealed shall, in so far as it is not inconsistent with the provisions of this Code, be deemed to have been done or taken under the corresponding provisions of this Code.\n"
            "(3) The mention of particular matters in this section shall not be held to prejudice or affect the general application of section 6 of the General Clauses Act, 1897 with regard to the effect of repeal."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "Operative w.e.f. 21 November 2025. Repealed Payment of Gratuity Act 1972 and EPF Act 1952 subject to savings.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/SS_Code_Gazette.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["repeal and savings", "Payment of Gratuity Act 1972", "EPF Act 1952"],
        "cross_references": ["Section 1", "IND-FED-PGA-1972", "IND-FED-EPF-1952"]
    },

    # =========================================================================
    # INDUSTRIAL RELATIONS CODE, 2020 (In Force w.e.f. 2025-11-21)
    # =========================================================================
    {
        "id": "IND-FED-IRC-2020-SEC-002",
        "parent_doc_id": "IND-FED-IRC-2020",
        "law_title": "The Industrial Relations Code, 2020",
        "short_title": "Industrial Relations Code, 2020 (Termination parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 2",
        "section_or_rule_title": "Definitions (Retrenchment, Closure, Worker, Average Pay)",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "In this Code, unless the context otherwise requires,—\n"
            "(c) 'average pay' means the average of the wages payable to a worker in the three complete calendar months (monthly paid), four weeks (weekly paid), or twelve working days (daily paid)...\n"
            "(d) 'closure' means the permanent closing down of a place of employment or part thereof;\n"
            "(zh) 'retrenchment' means the termination by the employer of the service of a worker for any reason whatsoever, otherwise than as a punishment inflicted by way of disciplinary action, but does not include voluntary retirement, superannuation, non-renewal of contract, completion of fixed term employment, or continued ill-health;\n"
            "(zr) 'worker' means any person employed in any industry to do any manual, unskilled, skilled, technical, operational, clerical or supervisory work for hire or reward... but does not include any such person who is employed mainly in a managerial or administrative capacity, or supervisory capacity drawing wages exceeding eighteen thousand rupees per month."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025 vide S.O. 5320(E).",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/IR_Gazette_of_India.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["retrenchment definition", "closure", "average pay", "worker definition", "exclusions from retrenchment"],
        "cross_references": ["Section 70", "Section 79", "IND-FED-IDA-1947-SEC-002OO"]
    },
    {
        "id": "IND-FED-IRC-2020-SEC-070",
        "parent_doc_id": "IND-FED-IRC-2020",
        "law_title": "The Industrial Relations Code, 2020",
        "short_title": "Industrial Relations Code, 2020 (Termination parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 70",
        "section_or_rule_title": "Conditions precedent to retrenchment of worker (Establishments not covered by Chapter X)",
        "chapter_or_part": "Chapter IX: Special Provisions Relating to Lay-off, Retrenchment and Closure",
        "exact_text": (
            "No worker employed in any industry who has been in continuous service for not less than one year under an employer shall be retrenched by that employer until—\n"
            "(a) the worker has been given one month's notice in writing indicating the reasons for retrenchment and the period of notice has expired, or the worker has been paid in lieu of such notice, wages for the period of the notice;\n"
            "(b) the worker has been paid, at the time of retrenchment, compensation which shall be equivalent to fifteen days' average pay, or for such higher days as may be given under any award or agreement, for every completed year of continuous service or any part thereof in excess of six months; and\n"
            "(c) notice in the prescribed manner is served on the appropriate Government."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. 1 month notice or pay in lieu + 15 days average pay per completed year of service.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/IR_Gazette_of_India.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["retrenchment compensation", "one month notice", "fifteen days average pay", "continuous service one year", "notice to government"],
        "cross_references": ["Section 79", "Section 83", "IND-FED-IDA-1947-SEC-025F"]
    },
    {
        "id": "IND-FED-IRC-2020-SEC-079",
        "parent_doc_id": "IND-FED-IRC-2020",
        "law_title": "The Industrial Relations Code, 2020",
        "short_title": "Industrial Relations Code, 2020 (Termination parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 79",
        "section_or_rule_title": "Conditions precedent to retrenchment of worker in certain establishments (300 or more workers)",
        "chapter_or_part": "Chapter X: Special Provisions Relating to Lay-off, Retrenchment and Closure in Certain Establishments",
        "exact_text": (
            "(1) No worker employed in any industrial establishment to which this Chapter applies [employing not less than 300 workers] "
            "who has been in continuous service for not less than one year under an employer shall be retrenched by that employer until,—\n"
            "(a) the worker has been given three months' notice in writing indicating the reasons for retrenchment and the period of notice has expired, or the worker has been paid in lieu of such notice, wages for the period of the notice;\n"
            "(b) the prior permission of the appropriate Government has been obtained on an application made in this behalf.\n"
            "(6) Where an order has been passed permitting the retrenchment of a worker... the worker shall be entitled to receive, "
            "at the time of retrenchment, compensation which shall be equivalent to fifteen days' average pay for every completed year "
            "of continuous service or any part thereof in excess of six months."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. 300+ workers threshold: 3 months notice & prior government permission.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/IR_Gazette_of_India.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["retrenchment in large establishments", "300 workers threshold", "prior government permission", "three months notice", "fifteen days compensation"],
        "cross_references": ["Section 70", "IND-FED-IDA-1947-SEC-025N"]
    },
    {
        "id": "IND-FED-IRC-2020-SEC-083",
        "parent_doc_id": "IND-FED-IRC-2020",
        "law_title": "The Industrial Relations Code, 2020",
        "short_title": "Industrial Relations Code, 2020 (Termination parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 83",
        "section_or_rule_title": "Worker Reskilling Fund",
        "chapter_or_part": "Chapter XI: Worker Reskilling Fund",
        "exact_text": (
            "(1) The appropriate Government shall, by notification, set up a fund to be called the Worker Reskilling Fund.\n"
            "(2) The fund shall consist of the contribution of the employer of an industrial establishment of an amount equal to fifteen days wages last drawn by the worker immediately before the retrenchment... for every retrenched worker.\n"
            "(3) The fund shall be utilised by crediting fifteen days wages last drawn by the worker to his account who is retrenched, within forty-five days of such retrenchment."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "In force w.e.f. 21 November 2025. Employer contributes 15 days wages into fund within 45 days of retrenchment.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/IR_Gazette_of_India.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["worker reskilling fund", "fifteen days wages contribution", "retrenchment benefit", "forty-five days deadline"],
        "cross_references": ["Section 70", "Section 79"]
    },
    {
        "id": "IND-FED-IRC-2020-SEC-104",
        "parent_doc_id": "IND-FED-IRC-2020",
        "law_title": "The Industrial Relations Code, 2020",
        "short_title": "Industrial Relations Code, 2020 (Repeal parts)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 104",
        "section_or_rule_title": "Repeal and savings",
        "chapter_or_part": "Chapter XIV: Miscellaneous",
        "exact_text": (
            "(1) The Trade Unions Act, 1926, the Industrial Employment (Standing Orders) Act, 1946 and the Industrial Disputes Act, 1947 are hereby repealed.\n"
            "(2) Notwithstanding such repeal, anything done or any action taken under the enactments hereby repealed shall, in so far as it is not inconsistent with the provisions of this Code, be deemed to have been done or taken under the corresponding provisions of this Code.\n"
            "(3) The mention of particular matters in this section shall not be held to prejudice or affect the general application of section 6 of the General Clauses Act, 1897 with regard to the effect of repeal."
        ),
        "effective_date": "2025-11-21",
        "effective_from": "2025-11-21",
        "repealed_on": None,
        "enactment_date": "2020-09-28",
        "legal_status": "In Force",
        "legal_status_notes": "Operative w.e.f. 21 November 2025. Repealed Industrial Disputes Act 1947 subject to savings for pre-21-Nov-2025 causes of action.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://labour.gov.in/sites/default/files/IR_Gazette_of_India.pdf",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["repeal and savings", "Industrial Disputes Act 1947", "savings clause"],
        "cross_references": ["Section 1", "IND-FED-IDA-1947"]
    },

    # =========================================================================
    # REPEALED LEGACY ACTS (Active for Pre-21-Nov-2025 Claims under Savings)
    # =========================================================================
    {
        "id": "IND-FED-PWA-1936-SEC-003",
        "parent_doc_id": "IND-FED-PWA-1936",
        "law_title": "The Payment of Wages Act, 1936",
        "short_title": "Payment of Wages Act, 1936",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 3",
        "section_or_rule_title": "Responsibility for payment of wages",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "Every employer shall be responsible for the payment to persons employed by him of all wages required to be paid under this Act:\n"
            "Provided that, in the case of persons employed (otherwise than by a contractor) in factories, industrial establishments, "
            "or railways, the manager or person responsible to the employer for supervision shall also be responsible for such payment."
        ),
        "effective_date": "1937-03-28",
        "effective_from": "1937-03-28",
        "repealed_on": "2025-11-21",
        "enactment_date": "1936-04-23",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025 by Code on Wages 2019. Governs claims arising before 21 Nov 2025.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2381",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["responsibility for payment", "employer liability", "manager responsibility"],
        "cross_references": ["Section 5", "Section 15"]
    },
    {
        "id": "IND-FED-PWA-1936-SEC-005",
        "parent_doc_id": "IND-FED-PWA-1936",
        "law_title": "The Payment of Wages Act, 1936",
        "short_title": "Payment of Wages Act, 1936",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 5",
        "section_or_rule_title": "Time of payment of wages (Including Termination Settlement)",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) The wages of every person employed upon or in any railway, factory or other establishment upon or in which less than "
            "one thousand persons are employed, shall be paid before the expiry of the seventh day... and in any other establishment "
            "before the expiry of the tenth day after the last day of the wage-period...\n"
            "(2) Where the employment of any person is terminated by or on behalf of the employer, the wages earned by him shall be paid "
            "before the expiry of the second working day from the day on which his employment is terminated:\n"
            "Provided that where the employment of any person in an establishment is terminated due to the closure of the establishment... "
            "the wages earned by him shall be paid before the expiry of the second working day from the day on which his employment is so terminated."
        ),
        "effective_date": "1937-03-28",
        "effective_from": "1937-03-28",
        "repealed_on": "2025-11-21",
        "enactment_date": "1936-04-23",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "HISTORIC & PRE-NOV-2025 RULE: Repealed on 21 November 2025 by Code on Wages 2019. "
            "Mandated payment before the expiry of the SECOND WORKING DAY following termination of employment."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2381",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["time of payment", "seventh day", "tenth day", "termination settlement", "second working day rule", "two working days", "resignation settlement"],
        "cross_references": ["Section 15", "IND-FED-COW-2019-SEC-017"]
    },
    {
        "id": "IND-FED-PWA-1936-SEC-007",
        "parent_doc_id": "IND-FED-PWA-1936",
        "law_title": "The Payment of Wages Act, 1936",
        "short_title": "Payment of Wages Act, 1936",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 7",
        "section_or_rule_title": "Deductions which may be made from wages",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) Notwithstanding the provisions of any other law for the time being in force, the wages of an employed person shall be paid "
            "to him without deductions of any kind except those authorised by or under this Act.\n"
            "(2) Deductions from the wages of an employed person shall be made only in accordance with the provisions of this Act, and may be "
            "of the following kinds only, namely:— (a) fines; (b) deductions for absence from duty; (c) deductions for damage to or loss of goods... "
            "(d) deductions for house-accommodation; (e) deductions for amenities and services; (f) deductions for recovery of advances..."
        ),
        "effective_date": "1937-03-28",
        "effective_from": "1937-03-28",
        "repealed_on": "2025-11-21",
        "enactment_date": "1936-04-23",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025. Governs unauthorized deductions prior to 21 Nov 2025.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2381",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["deductions", "unlawful deductions", "fines", "absence from duty", "damage or loss", "advances"],
        "cross_references": ["Section 15", "IND-FED-COW-2019-SEC-018"]
    },
    {
        "id": "IND-FED-PWA-1936-SEC-015",
        "parent_doc_id": "IND-FED-PWA-1936",
        "law_title": "The Payment of Wages Act, 1936",
        "short_title": "Payment of Wages Act, 1936",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 15",
        "section_or_rule_title": "Claims arising out of deductions from wages or delay in payment of wages",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) The appropriate Government may, by notification, appoint a presiding officer of any Labour Court... to be the authority "
            "to hear and decide for any specified area all claims arising out of deductions from the wages, or delay in payment of the wages...\n"
            "(2) Where contrary to the provisions of this Act any deduction has been made from the wages of an employed person, or any payment "
            "of wages has been delayed, such person himself, or any legal practitioner or official of a registered trade union... may apply "
            "to such authority for a direction under sub-section (3):\n"
            "Provided that every such application shall be presented within twelve months from the date on which the deduction was made "
            "or payment was due: Provided further that any application may be admitted after the said period of twelve months when the applicant "
            "satisfies the authority that he had sufficient cause for not making the application within such period.\n"
            "(3) When any application under sub-section (2) is entertained, the authority shall hear the applicant and the employer... and may "
            "direct the refund of the amount deducted, or the payment of the delayed wages, together with compensation not exceeding ten times "
            "the amount deducted in the former case and not exceeding three thousand rupees in the latter."
        ),
        "effective_date": "1937-03-28",
        "effective_from": "1937-03-28",
        "repealed_on": "2025-11-21",
        "enactment_date": "1936-04-23",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "HISTORIC & PRE-NOV-2025 CLAIMS MECHANISM: Repealed on 21 November 2025. "
            "12-month limitation for filing wage claim; compensation up to 10x deducted wages."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2381",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["wage claims", "claims authority", "twelve months limitation", "condonation of delay", "ten times compensation", "delayed wages", "unpaid wages"],
        "cross_references": ["Section 5", "IND-FED-COW-2019-SEC-045"]
    },
    {
        "id": "IND-FED-MWA-1948-SEC-012",
        "parent_doc_id": "IND-FED-MWA-1948",
        "law_title": "The Minimum Wages Act, 1948",
        "short_title": "Minimum Wages Act, 1948",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 12",
        "section_or_rule_title": "Payment of minimum rates of wages",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) Where in respect of any scheduled employment a notification under section 5 is in force, the employer shall pay to every "
            "employee engaged in a scheduled employment under him wages at a rate not less than the minimum rate of wages fixed by such "
            "notification for that class of employees in that employment without any deductions except as may be authorised."
        ),
        "effective_date": "1948-03-15",
        "effective_from": "1948-03-15",
        "repealed_on": "2025-11-21",
        "enactment_date": "1948-03-15",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025 by Code on Wages 2019.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1511",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["minimum wages", "scheduled employment", "mandatory minimum rate"],
        "cross_references": ["Section 14", "Section 20", "IND-FED-COW-2019-SEC-006"]
    },
    {
        "id": "IND-FED-MWA-1948-SEC-014",
        "parent_doc_id": "IND-FED-MWA-1948",
        "law_title": "The Minimum Wages Act, 1948",
        "short_title": "Minimum Wages Act, 1948",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 14",
        "section_or_rule_title": "Overtime",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) Where an employee, whose minimum rate of wages is fixed under this Act by the hour, by the day or by such a longer wage-period "
            "as may be prescribed, works on any day in excess of the number of hours constituting a normal working day, the employer shall "
            "pay him for every hour or for part of an hour so worked in excess at the overtime rate fixed under this Act or under any law of the "
            "appropriate Government for the time being in force, whichever is higher."
        ),
        "effective_date": "1948-03-15",
        "effective_from": "1948-03-15",
        "repealed_on": "2025-11-21",
        "enactment_date": "1948-03-15",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025 by Code on Wages 2019.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1511",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["overtime rate", "work in excess of normal working day"],
        "cross_references": ["Section 12", "IND-FED-COW-2019-SEC-014"]
    },
    {
        "id": "IND-FED-MWA-1948-SEC-020",
        "parent_doc_id": "IND-FED-MWA-1948",
        "law_title": "The Minimum Wages Act, 1948",
        "short_title": "Minimum Wages Act, 1948",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 20",
        "section_or_rule_title": "Claims",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) The appropriate Government may, by notification in the Official Gazette, appoint an Authority to hear and decide for any specified "
            "area all claims arising out of payment of less than the minimum rates of wages or in respect of the payment of remuneration for days "
            "of rest or for work done on such days under clause (b) or clause (c) of sub-section (1) of section 13 or of wages at the overtime rate under section 14...\n"
            "(2) Where an employee has any claim of the nature referred to in sub-section (1), the employee himself, or any legal practitioner "
            "or any official of a registered trade union... may apply to such Authority for a direction under sub-section (3):\n"
            "Provided that every such application shall be presented within six months from the date on which the minimum wages or other amount became payable."
        ),
        "effective_date": "1948-03-15",
        "effective_from": "1948-03-15",
        "repealed_on": "2025-11-21",
        "enactment_date": "1948-03-15",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025 by Code on Wages 2019. Prescribed 6-month window for minimum wage claims.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1511",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["minimum wage claims", "claims authority", "six months limitation", "overtime claims"],
        "cross_references": ["Section 12", "Section 14", "IND-FED-COW-2019-SEC-045"]
    },
    {
        "id": "IND-FED-PGA-1972-SEC-004",
        "parent_doc_id": "IND-FED-PGA-1972",
        "law_title": "The Payment of Gratuity Act, 1972",
        "short_title": "Payment of Gratuity Act, 1972",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 4",
        "section_or_rule_title": "Payment of gratuity",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) Gratuity shall be payable to an employee on the termination of his employment after he has rendered continuous service "
            "for not less than five years,—\n"
            "(a) on his superannuation, or\n"
            "(b) on his retirement or resignation, or\n"
            "(c) on his death or disablement due to accident or disease:\n"
            "Provided that the completion of continuous service of five years shall not be necessary where the termination of the employment "
            "of any employee is due to death or disablement...\n"
            "(2) For every completed year of service or part thereof in excess of six months, the employer shall pay gratuity to an employee "
            "at the rate of fifteen days' wages based on the rate of wages last drawn by the employee concerned...\n"
            "Explanation.—In the case of a monthly rated employee, the fifteen days' wages shall be calculated by dividing the monthly rate "
            "of wages last drawn by him by twenty-six and multiplying the quotient by fifteen (15/26 formula).\n"
            "(3) The amount of gratuity payable to an employee shall not exceed twenty lakh rupees."
        ),
        "effective_date": "1972-09-16",
        "effective_from": "1972-09-16",
        "repealed_on": "2025-11-21",
        "enactment_date": "1972-08-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "HISTORIC & PRE-NOV-2025 GRATUITY ELIGIBILITY: Repealed on 21 November 2025 by Code on Social Security 2020. "
            "Requires 5 years continuous service for resignation/retirement; 15/26 formula; ₹20 Lakhs ceiling."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1512",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["gratuity payment", "five years continuous service", "fifteen days wages", "twenty-six formula", "twenty lakh ceiling", "resignation gratuity"],
        "cross_references": ["Section 7", "IND-FED-COSS-2020-SEC-053"]
    },
    {
        "id": "IND-FED-PGA-1972-SEC-007",
        "parent_doc_id": "IND-FED-PGA-1972",
        "law_title": "The Payment of Gratuity Act, 1972",
        "short_title": "Payment of Gratuity Act, 1972",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 7",
        "section_or_rule_title": "Determination of the amount of gratuity",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) A person who is eligible for payment of gratuity under this Act or any person authorised... shall send a written application "
            "to the employer, within such time and in such form, as may be prescribed, for payment of such gratuity.\n"
            "(2) As soon as gratuity becomes payable, the employer shall, whether an application referred to in sub-section (1) has been made "
            "or not, determine the amount of gratuity and give notice in writing to the person to whom the gratuity is payable and also to the "
            "controlling authority specifying the amount of gratuity so determined.\n"
            "(3) The employer shall arrange to pay the amount of gratuity within thirty days from the date it becomes payable...\n"
            "(3A) If the amount of gratuity payable under sub-section (3) is not paid by the employer within the period specified in sub-section (3), "
            "the employer shall pay, from the date on which the gratuity becomes payable to the date on which it is paid, simple interest at such "
            "rate, not exceeding the rate notified by the Central Government from time to time for repayment of long-term deposits..."
        ),
        "effective_date": "1972-09-16",
        "effective_from": "1972-09-16",
        "repealed_on": "2025-11-21",
        "enactment_date": "1972-08-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "HISTORIC & PRE-NOV-2025 RULE: Repealed on 21 November 2025. 30 days mandatory payment window and statutory simple interest on delay."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1512",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["gratuity determination", "thirty days payment", "simple interest on delay", "controlling authority"],
        "cross_references": ["Section 4", "Section 8", "IND-FED-COSS-2020-SEC-055"]
    },
    {
        "id": "IND-FED-PGA-1972-SEC-008",
        "parent_doc_id": "IND-FED-PGA-1972",
        "law_title": "The Payment of Gratuity Act, 1972",
        "short_title": "Payment of Gratuity Act, 1972",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 8",
        "section_or_rule_title": "Recovery of gratuity",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "If the amount of gratuity payable under this Act is not paid by the employer, within the prescribed time, to the person entitled thereto, "
            "the controlling authority shall, on an application made to it in this behalf by the aggrieved person, issue a certificate for that "
            "amount to the Collector, who shall recover the same, together with compound interest thereon at such rate as the Central Government may, "
            "by notification, specify, from the date of expiry of the prescribed time, as arrears of land revenue and pay the same to the person entitled thereto."
        ),
        "effective_date": "1972-09-16",
        "effective_from": "1972-09-16",
        "repealed_on": "2025-11-21",
        "enactment_date": "1972-08-21",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025. Recovery via Collector as arrears of land revenue with compound interest.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1512",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["recovery of gratuity", "certificate to Collector", "arrears of land revenue", "compound interest"],
        "cross_references": ["Section 4", "Section 7"]
    },
    {
        "id": "IND-FED-EPF-1952-SEC-006",
        "parent_doc_id": "IND-FED-EPF-1952",
        "law_title": "The Employees' Provident Funds and Miscellaneous Provisions Act, 1952",
        "short_title": "Employees' Provident Funds Act, 1952",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 6",
        "section_or_rule_title": "Contributions and matters which may be provided for in Schemes",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "The contribution which shall be paid by the employer to the Fund shall be ten per cent. of the basic wages, dearness allowance "
            "and retaining allowance (if any) for the time being payable to each of the employees (whether employed by him directly or by or through a contractor), "
            "and the employee's contribution shall be equal to the contribution payable by the employer in respect of him:\n"
            "Provided that in its application to any establishment or class of establishments which the Central Government, after making such inquiry "
            "as it deems fit, may, by notification in the Official Gazette, specify, this section shall have effect as if for the words 'ten per cent.', "
            "the words 'twelve per cent.' had been substituted."
        ),
        "effective_date": "1952-11-01",
        "effective_from": "1952-11-01",
        "repealed_on": "2025-11-21",
        "enactment_date": "1952-03-04",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025 by Code on Social Security 2020. 10% / 12% contribution rates.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1513",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["PF contributions", "ten percent", "twelve percent", "basic wages", "dearness allowance"],
        "cross_references": ["IND-FED-COSS-2020-SEC-017"]
    },
    {
        "id": "IND-FED-EPF-1952-SEC-007A",
        "parent_doc_id": "IND-FED-EPF-1952",
        "law_title": "The Employees' Provident Funds and Miscellaneous Provisions Act, 1952",
        "short_title": "Employees' Provident Funds Act, 1952",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 7A",
        "section_or_rule_title": "Determination of moneys due from employers",
        "chapter_or_part": "Substantive Provisions",
        "exact_text": (
            "(1) The Central Provident Fund Commissioner, any Additional Central Provident Fund Commissioner, any Deputy Provident Fund Commissioner, "
            "any Regional Provident Fund Commissioner, or any Assistant Provident Fund Commissioner may, by order,—\n"
            "(a) in a case where a dispute arises regarding the applicability of this Act to an establishment, decide such dispute; and\n"
            "(b) determine the amount due from any employer under any provision of this Act, the Scheme or the Pension Scheme or the Insurance Scheme...\n"
            "(2) The officer conducting the inquiry under sub-section (1) shall, for the purposes of such inquiry have the same powers as are vested "
            "in a court under the Code of Civil Procedure, 1908, in respect of enforcing attendance, compelling production of documents, and issuing commissions."
        ),
        "effective_date": "1952-11-01",
        "effective_from": "1952-11-01",
        "repealed_on": "2025-11-21",
        "enactment_date": "1952-03-04",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": "Repealed on 21 November 2025 by Code on Social Security 2020. Quasi-judicial inquiry to determine PF default.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1513",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["determination of PF dues", "7A inquiry", "Provident Fund Commissioner", "unpaid PF recovery"],
        "cross_references": ["Section 6"]
    },
    {
        "id": "IND-FED-IDA-1947-SEC-025F",
        "parent_doc_id": "IND-FED-IDA-1947",
        "law_title": "The Industrial Disputes Act, 1947",
        "short_title": "Industrial Disputes Act, 1947",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 25F",
        "section_or_rule_title": "Conditions precedent to retrenchment of workmen",
        "chapter_or_part": "Chapter VA: Lay-off and Retrenchment",
        "exact_text": (
            "No workman employed in any industry who has been in continuous service for not less than one year under an employer shall be retrenched by that employer until—\n"
            "(a) the workman has been given one month's notice in writing indicating the reasons for retrenchment and the period of notice has expired, or the workman has been paid in lieu of such notice, wages for the period of the notice;\n"
            "(b) the workman has been paid, at the time of retrenchment, compensation which shall be equivalent to fifteen days' average pay for every completed year of continuous service or any part thereof in excess of six months; and\n"
            "(c) notice in the prescribed manner is served on the appropriate Government or such authority as may be specified by the appropriate Government by notification in the Official Gazette."
        ),
        "effective_date": "1953-10-24",
        "effective_from": "1953-10-24",
        "repealed_on": "2025-11-21",
        "enactment_date": "1947-03-11",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "HISTORIC & PRE-NOV-2025 RULE: Repealed on 21 November 2025 by Industrial Relations Code 2020. "
            "Governs retrenchment of workmen in establishments with up to 100 workers prior to 21 Nov 2025."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2380",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["retrenchment compensation", "one month notice", "fifteen days average pay", "workman", "continuous service one year", "termination compensation"],
        "cross_references": ["Section 25N", "Section 33C", "IND-FED-IRC-2020-SEC-070"]
    },
    {
        "id": "IND-FED-IDA-1947-SEC-033C",
        "parent_doc_id": "IND-FED-IDA-1947",
        "law_title": "The Industrial Disputes Act, 1947",
        "short_title": "Industrial Disputes Act, 1947",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 33C",
        "section_or_rule_title": "Recovery of money due from an employer",
        "chapter_or_part": "Chapter VII: Miscellaneous",
        "exact_text": (
            "(1) Where any money is due to a workman from an employer under a settlement or an award or under the provisions of Chapter VA or Chapter VB, "
            "the workman himself or any other person authorised by him in writing... may make an application to the appropriate Government "
            "for the recovery of the money due to him, and if the appropriate Government is satisfied that any money is so due, it shall issue a certificate "
            "for that amount to the Collector who shall proceed to recover the same in the same manner as an arrear of land revenue...\n"
            "(2) Where any workman is entitled to receive from the employer any money or any benefit which is capable of being computed in terms of money... "
            "the question may be decided by such Labour Court as may be specified in this behalf by the appropriate Government within a period not exceeding three months."
        ),
        "effective_date": "1947-04-01",
        "effective_from": "1947-04-01",
        "repealed_on": "2025-11-21",
        "enactment_date": "1947-03-11",
        "legal_status": "Repealed (Active for Pre-21-Nov-2025 Claims)",
        "legal_status_notes": (
            "HISTORIC & PRE-NOV-2025 RECOVERY: Repealed on 21 November 2025. Execution and recovery mechanism for retrenchment dues "
            "and wage arrears before Labour Court."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2380",
        "retrieval_date": "2026-11-09",
        "scope_category": "Wage & Employment",
        "key_topics": ["recovery of dues", "Labour Court", "arrears of land revenue", "settlement dues", "retrenchment recovery", "33C application"],
        "cross_references": ["Section 25F", "IND-FED-COW-2019-SEC-045"]
    }
]

for _p in PROVISIONS:
    _p.setdefault("effective_from", _p.get("effective_date"))
    _p.setdefault("repealed_on", None)
