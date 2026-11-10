"""
Rent Laws statutory data module:
Sources:
1. Central Fallback: Transfer of Property Act, 1882 (ss. 105-117)
2. Delhi: Delhi Rent Control Act, 1958 (Act No. 59 of 1958)
3. Maharashtra: Maharashtra Rent Control Act, 1999 (Act No. XVIII of 2000)
4. Karnataka: Karnataka Rent Act, 1999 (Act No. 34 of 2001)
5. Tamil Nadu: Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017 (Act No. 42 of 2017)
"""

DOCUMENTS = [
    {
        "id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 4 of 1882",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "enactment_date": "1882-02-17",
        "effective_date": "1882-07-01",
        "effective_from": "1882-07-01",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enacted on 17 February 1882, commenced 1 July 1882. Chapter V (Sections 105 to 117) "
            "serves as the foundational fallback law across India for all leases and tenancies that fall outside "
            "the protective threshold of state-specific rent control legislations (e.g. rent exceeding ₹3,500/month "
            "in Delhi or Karnataka, or corporate tenancies in Maharashtra)."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "ministry": "Ministry of Law and Justice, Legislative Department",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
    },
    {
        "id": "IND-DL-DRCA-1958",
        "law_title": "The Delhi Rent Control Act, 1958",
        "short_title": "Delhi Rent Control Act, 1958",
        "act_or_rule_type": "Central Act for Union Territory",
        "act_number": "Act No. 59 of 1958",
        "jurisdiction": "National Capital Territory of Delhi",
        "enactment_date": "1958-12-31",
        "effective_date": "1959-02-09",
        "effective_from": "1959-02-09",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enacted 31 December 1958, commenced 9 February 1959. CRITICAL JURISDICTION THRESHOLD: "
            "Under Section 3(c) (inserted by Act 57 of 1988), the Act DOES NOT APPLY to any premises whose monthly "
            "rent exceeds ₹3,500. Tenancies with rent > ₹3,500/month in Delhi are governed exclusively by the "
            "Transfer of Property Act, 1882 and contract law before regular civil courts."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1531",
        "ministry": "Ministry of Home Affairs / Government of NCT of Delhi",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
    },
    {
        "id": "IND-MH-MRCA-1999",
        "law_title": "The Maharashtra Rent Control Act, 1999",
        "short_title": "Maharashtra Rent Control Act, 1999",
        "act_or_rule_type": "State Act",
        "act_number": "Maharashtra Act No. XVIII of 2000",
        "jurisdiction": "State of Maharashtra",
        "enactment_date": "2000-03-10",
        "effective_date": "2000-03-31",
        "effective_from": "2000-03-31",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Assented to by President on 10 March 2000, commenced 31 March 2000. Repealed Bombay Rents, Hotel and "
            "Lodging House Rates Control Act, 1947. Section 3 exempts premises let to banks, PSUs, and companies with "
            "paid-up share capital >= ₹1 Crore. Section 24 provides summary eviction for Leave and License with double fee "
            "damages for overstay. Section 55 mandates written registered agreements under penalty of imprisonment."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2464",
        "ministry": "Government of Maharashtra, Law and Judiciary Department",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
    },
    {
        "id": "IND-KA-KRA-1999",
        "law_title": "The Karnataka Rent Act, 1999",
        "short_title": "Karnataka Rent Act, 1999",
        "act_or_rule_type": "State Act",
        "act_number": "Karnataka Act No. 34 of 2001",
        "jurisdiction": "State of Karnataka",
        "enactment_date": "2001-11-22",
        "effective_date": "2001-12-31",
        "effective_from": "2001-12-31",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Assented to 22 November 2001, commenced 31 December 2001 vide Notification No. RD 39 LRE 2001. "
            "Repealed Karnataka Rent Control Act, 1961. Section 2(3)(e) exempts premises whose monthly rent exceeds "
            "₹3,500 in Part A Schedule I areas (Bengaluru, etc.) or ₹2,000 elsewhere, and commercial premises > 14 sq meters. "
            "Exempt properties fall back to Transfer of Property Act, 1882."
        ),
        "official_source_url": "http://dpal.karnataka.gov.in",
        "ministry": "Government of Karnataka, Department of Parliamentary Affairs and Legislation",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
    },
    {
        "id": "IND-TN-TNRRRLTA-2017",
        "law_title": "The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017",
        "short_title": "TNRRRLT Act, 2017",
        "act_or_rule_type": "State Act",
        "act_number": "Tamil Nadu Act No. 42 of 2017",
        "jurisdiction": "State of Tamil Nadu",
        "enactment_date": "2017-08-04",
        "effective_date": "2019-02-22",
        "effective_from": "2019-02-22",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Assented to 4 August 2017, commenced 22 February 2019 vide G.O. Ms. No. 35, Housing and Urban Development. "
            "CRITICAL REPEAL FINDING: Completely repealed the old Tamil Nadu Buildings (Lease and Rent Control) Act, 1960. "
            "Replaced legacy rent control with modern tenancy framework: compulsory registration of agreement within 90 days (s. 4), "
            "security deposit capped at max 3 months' rent for residential (s. 11), double rent compensation for overstay (s. 22)."
        ),
        "official_source_url": "https://tenancy.tn.gov.in",
        "ministry": "Government of Tamil Nadu, Housing and Urban Development Department",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
    }
]

PROVISIONS = [
    # =========================================================================
    # TRANSFER OF PROPERTY ACT, 1882 (ss. 105 - 117) - Central Fallback
    # =========================================================================
    {
        "id": "IND-FED-TPA-1882-SEC-105",
        "parent_doc_id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "section_or_rule_number": "Section 105",
        "section_or_rule_title": "Lease defined",
        "chapter_or_part": "Chapter V: Of Leases of Immovable Property",
        "exact_text": (
            "A lease of immovable property is a transfer of a right to enjoy such property, made for a certain time, express or implied, "
            "or in perpetuity, in consideration of a price paid or promised, or of money, a share of crops, service or any other thing "
            "of value, to be rendered periodically or on specified occasions to the transferor by the transferee, who accepts the transfer on such terms.\n"
            "Lessor, lessee, premium and rent defined.—The transferor is called the lessor, the transferee is called the lessee, "
            "the price is called the premium, and the money, share, service or other thing to be so rendered is called the rent."
        ),
        "effective_date": "1882-07-01",
        "enactment_date": "1882-02-17",
        "legal_status": "In Force",
        "legal_status_notes": "Central statutory definition of lease, lessor, lessee, premium (deposit), and rent.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["lease defined", "lessor", "lessee", "premium", "rent"],
        "cross_references": ["Section 106", "Section 107", "Section 108"]
    },
    {
        "id": "IND-FED-TPA-1882-SEC-106",
        "parent_doc_id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "section_or_rule_number": "Section 106",
        "section_or_rule_title": "Duration of certain leases in absence of written contract or local usage",
        "chapter_or_part": "Chapter V: Of Leases of Immovable Property",
        "exact_text": (
            "(1) In the absence of a contract or local law or usage to the contrary, a lease of immovable property for agricultural "
            "or manufacturing purposes shall be deemed to be a lease from year to year, terminable, on the part of either lessor or lessee, "
            "by six months' notice; and a lease of immovable property for any other purpose shall be deemed to be a lease from month to month, "
            "terminable, on the part of either lessor or lessee, by fifteen days' notice.\n"
            "(2) Notwithstanding anything contained in any other law for the time being in force, the period mentioned in sub-section (1) "
            "shall commence from the date of receipt of notice.\n"
            "(3) A notice under sub-section (1) shall not be deemed to be invalid merely because the period mentioned therein falls short of "
            "the period specified under that sub-section, where a suit or proceeding is filed after the expiry of the period mentioned in that sub-section.\n"
            "(4) Every notice under sub-section (1) must be in writing, signed by or on behalf of the person giving it, and either be sent by "
            "post to the party who is intended to be bound by it or be tendered or delivered personally to such party, or to one of his family "
            "or servants at his residence, or (if such tender or delivery is not practicable) affixed to a conspicuous part of the property."
        ),
        "effective_date": "1882-07-01",
        "enactment_date": "1882-02-17",
        "legal_status": "In Force",
        "legal_status_notes": (
            "FOUNDATIONAL NOTICE REQUIREMENT: For non-rent-control residential/commercial tenancies, notice to quit requires "
            "15 DAYS WRITTEN NOTICE running from date of receipt (as amended by Act 3 of 2003)."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["duration of lease", "month to month", "fifteen days notice", "six months notice", "notice to quit", "receipt of notice"],
        "cross_references": ["Section 105", "Section 111", "IND-FED-LIM-1963-ART-067"]
    },
    {
        "id": "IND-FED-TPA-1882-SEC-107",
        "parent_doc_id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "section_or_rule_number": "Section 107",
        "section_or_rule_title": "Leases how made",
        "chapter_or_part": "Chapter V: Of Leases of Immovable Property",
        "exact_text": (
            "A lease of immovable property from year to year, or for any term exceeding one year or reserving a yearly rent, "
            "can be made only by a registered instrument.\n"
            "All other leases of immovable property may be made either by a registered instrument or by oral agreement accompanied by delivery of possession.\n"
            "Where a lease of immovable property is made by a registered instrument, such instrument or, where there are more instruments than one, "
            "each instrument shall be executed by both the lessor and the lessee:\n"
            "Provided that the State Government may from time to time, by notification in the Official Gazette, direct that leases of immovable property, "
            "other than leases from year to year, or for any term exceeding one year, or reserving a yearly rent, or any class of such leases, "
            "may be made by unregistered instrument or by oral agreement without delivery of possession."
        ),
        "effective_date": "1882-07-01",
        "enactment_date": "1882-02-17",
        "legal_status": "In Force",
        "legal_status_notes": "Leases exceeding 11 months (i.e. exceeding 1 year) COMPULSORILY REQUIRE REGISTRATION. Hence the ubiquitous 11-month rent agreement practice in India.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["leases how made", "registered instrument", "exceeding one year", "eleven month lease", "oral agreement"],
        "cross_references": ["Section 105", "Section 106"]
    },
    {
        "id": "IND-FED-TPA-1882-SEC-108",
        "parent_doc_id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "section_or_rule_number": "Section 108",
        "section_or_rule_title": "Rights and liabilities of lessor and lessee",
        "chapter_or_part": "Chapter V: Of Leases of Immovable Property",
        "exact_text": (
            "In the absence of a contract or local usage to the contrary, the lessor and the lessee of immovable property, as against one another, respectively, possess the rights and are subject to the liabilities mentioned in the rules next following, or such of them as are applicable to the property leased:—\n"
            "(A) Rights and Liabilities of the Lessor:\n"
            "(a) The lessor is bound to disclose to the lessee any material defect in the property, with reference to its intended use, of which the former is and the latter is not aware, and which the latter could not with ordinary care discover;\n"
            "(b) the lessor is bound on the lessee's request to put him in possession of the property;\n"
            "(c) the lessor shall be deemed to contract with the lessee that, if the latter pays the rent reserved by the lease and performs the contracts binding on the lessee, he may hold the property during the time limited by the lease without interruption (covenant for quiet enjoyment).\n"
            "(B) Rights and Liabilities of the Lessee:\n"
            "(f) if the lessor neglects to make, within a reasonable time after notice, any repairs which he is bound to make to the property, the lessee may make the same himself, and deduct the expense of such repairs with interest from the rent, or otherwise recover it from the lessor;\n"
            "(l) the lessee is bound to pay or tender, at the proper time and place, the premium or rent to the lessor or his agent in this behalf;\n"
            "(m) the lessee is bound to keep, and on the termination of the lease to restore, the property in as good condition as it was in at the time when he was put in possession, subject only to the changes caused by reasonable wear and tear or irresistible force...;\n"
            "(p) he must not, without the lessor's consent, erect on the property any permanent structure, except for agricultural purposes;\n"
            "(q) on the determination of the lease, the lessee is bound to put the lessor into possession of the property."
        ),
        "effective_date": "1882-07-01",
        "enactment_date": "1882-02-17",
        "legal_status": "In Force",
        "legal_status_notes": "Statutory baseline for quiet enjoyment, repairs deduction, reasonable wear and tear, and redelivery of possession.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["quiet enjoyment", "repairs deduction", "material defect disclosure", "payment of rent", "reasonable wear and tear", "restoration of possession"],
        "cross_references": ["Section 105", "Section 111"]
    },
    {
        "id": "IND-FED-TPA-1882-SEC-111",
        "parent_doc_id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "section_or_rule_number": "Section 111",
        "section_or_rule_title": "Determination of lease",
        "chapter_or_part": "Chapter V: Of Leases of Immovable Property",
        "exact_text": (
            "A lease of immovable property determines—\n"
            "(a) by efflux of the time limited thereby;\n"
            "(b) where such time is limited conditionally on the happening of some event—by the happening of such event;\n"
            "(c) where the interest of the lessor in the property terminates on, or his power to dispose of the same extends only to, the happening of any event—by the happening of such event;\n"
            "(d) in case the interests of the lessee and the lessor in the whole of the property become vested at the same time in one person in the same right (merger);\n"
            "(e) by express surrender; that is to say, in case the lessee yields up his interest under the lease to the lessor, by mutual agreement between them;\n"
            "(f) by implied surrender;\n"
            "(g) by forfeiture; that is to say, (1) in case the lessee breaks an express condition which provides that, on breach thereof, the lessor may re-enter; or (2) in case the lessee renounces his character as such by setting up a title in a third person or by claiming title in himself; or (3) the lessee is adjudicated an insolvent and the lease provides that the lessor may re-enter on the happening of such event; and in any of these cases the lessor or his transferee gives notice in writing to the lessee of his intention to determine the lease;\n"
            "(h) on the expiration of a notice to determine the lease, or to quit, or of intention to quit, the property leased, duly given by one party to the other."
        ),
        "effective_date": "1882-07-01",
        "enactment_date": "1882-02-17",
        "legal_status": "In Force",
        "legal_status_notes": "Statutory modes of terminating a lease: expiry of term, forfeiture, surrender, notice to quit.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["determination of lease", "efflux of time", "surrender", "forfeiture", "notice to quit", "expiration of lease"],
        "cross_references": ["Section 106", "Section 114", "Section 116"]
    },
    {
        "id": "IND-FED-TPA-1882-SEC-114",
        "parent_doc_id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "section_or_rule_number": "Section 114",
        "section_or_rule_title": "Relief against forfeiture for non-payment of rent",
        "chapter_or_part": "Chapter V: Of Leases of Immovable Property",
        "exact_text": (
            "Where a lease of immovable property has determined by forfeiture for non-payment of rent, and the lessor sues to eject the lessee, "
            "if, at the hearing of the suit, the lessee pays or tenders to the lessor the rent in arrear, together with interest thereon and his "
            "full costs of the suit, or gives such security as the court thinks sufficient for making such payment within fifteen days, "
            "the court may, in lieu of making a decree for ejectment, pass an order relieving the lessee against the forfeiture; and thereupon "
            "the lessee shall hold the property leased as if the forfeiture had not occurred."
        ),
        "effective_date": "1882-07-01",
        "enactment_date": "1882-02-17",
        "legal_status": "In Force",
        "legal_status_notes": "Equitable statutory relief: tenant can avoid eviction by paying rent arrears + interest + costs at hearing.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["relief against forfeiture", "non-payment of rent", "tender of arrears", "fifteen days security", "ejectment avoided"],
        "cross_references": ["Section 111", "Section 114A"]
    },
    {
        "id": "IND-FED-TPA-1882-SEC-116",
        "parent_doc_id": "IND-FED-TPA-1882",
        "law_title": "The Transfer of Property Act, 1882",
        "short_title": "Transfer of Property Act, 1882 (ss. 105-117)",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India - Central Fallback for Non-Rent Control Tenancies)",
        "section_or_rule_number": "Section 116",
        "section_or_rule_title": "Effect of holding over",
        "chapter_or_part": "Chapter V: Of Leases of Immovable Property",
        "exact_text": (
            "If a lessee or under-lessee of property remains in possession thereof after the determination of the lease granted to the lessee, "
            "and the lessor or his legal representative accepts rent from the lessee or under-lessee, or otherwise assents to his continuing "
            "in possession, the lease is, in the absence of an agreement to the contrary, renewed from year to year, or from month to month, "
            "according to the purpose for which the property is leased, as specified in section 106."
        ),
        "effective_date": "1882-07-01",
        "enactment_date": "1882-02-17",
        "legal_status": "In Force",
        "legal_status_notes": "HOLDING OVER PRINCIPLE: If landlord accepts rent after lease expiry without a new written agreement, a statutory month-to-month tenancy is created.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2338",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["holding over", "tenancy at will", "acceptance of rent", "renewal month to month", "post-lease possession"],
        "cross_references": ["Section 106", "Section 111"]
    },

    # =========================================================================
    # DELHI RENT CONTROL ACT, 1958 (Act No. 59 of 1958)
    # =========================================================================
    {
        "id": "IND-DL-DRCA-1958-SEC-003",
        "parent_doc_id": "IND-DL-DRCA-1958",
        "law_title": "The Delhi Rent Control Act, 1958",
        "short_title": "Delhi Rent Control Act, 1958",
        "act_or_rule_type": "Central Act for Union Territory",
        "jurisdiction": "National Capital Territory of Delhi",
        "section_or_rule_number": "Section 3",
        "section_or_rule_title": "Act not to apply to certain premises (The ₹3,500 Threshold)",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "Nothing in this Act shall apply—\n"
            "(a) to any premises belonging to the Government;\n"
            "(b) to any tenancy or other like relationship created by a grant from the Government in respect of the premises taken on lease, or requisitioned, by the Government: Provided that where any premises belonging to Government have been or are lawfully let by any person to virtue of an agreement with the Government or otherwise, then, the nature and extent of the rights and obligations of such person, so far as may be, shall be governed by this Act;\n"
            "(c) to any premises, whether residential or not, whose monthly rent exceeds three thousand and five hundred rupees; or\n"
            "(d) to any premises constructed on or after the commencement of the Delhi Rent Control (Amendment) Act, 1988, for a period of ten years from the date of completion of such construction."
        ),
        "effective_date": "1959-02-09",
        "enactment_date": "1958-12-31",
        "legal_status": "In Force",
        "legal_status_notes": (
            "CRITICAL RAG RULE FOR DELHI: Under Section 3(c) (inserted w.e.f. 1 December 1988), if the monthly rent exceeds ₹3,500, "
            "the Delhi Rent Control Act DOES NOT APPLY. Because modern rentals in Delhi almost universally exceed ₹3,500/month, "
            "tenants and landlords in Delhi fall under the Transfer of Property Act, 1882 (ss. 105-117) and normal civil suits, "
            "NOT the Rent Controller."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1531",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["exemption", "three thousand five hundred rupees", "monthly rent ceiling", "outside rent control", "Delhi rent threshold"],
        "cross_references": ["IND-FED-TPA-1882-SEC-105", "IND-FED-TPA-1882-SEC-106"]
    },
    {
        "id": "IND-DL-DRCA-1958-SEC-014",
        "parent_doc_id": "IND-DL-DRCA-1958",
        "law_title": "The Delhi Rent Control Act, 1958",
        "short_title": "Delhi Rent Control Act, 1958",
        "act_or_rule_type": "Central Act for Union Territory",
        "jurisdiction": "National Capital Territory of Delhi",
        "section_or_rule_number": "Section 14",
        "section_or_rule_title": "Protection of tenant against eviction",
        "chapter_or_part": "Chapter III: Control of Eviction of Tenants",
        "exact_text": (
            "(1) Notwithstanding anything to the contrary contained in any other law or contract, no order or decree for the recovery "
            "of possession of any premises shall be made by any court or Controller in favour of the landlord against a tenant: "
            "Provided that the Controller may, on an application made to him in the prescribed manner, make an order for the recovery of "
            "possession of the premises on one or more of the following grounds only, namely:—\n"
            "(a) that the tenant has neither paid nor tendered the whole of the arrears of the rent legally recoverable from him within two months of the date on which a notice of demand for the arrears of rent has been served on him by the landlord in the manner provided in section 106 of the Transfer of Property Act, 1882;\n"
            "(b) that the tenant has, on or after the 9th day of June, 1952, sub-let, assigned or otherwise parted with the possession of the whole or any part of the premises without obtaining the consent in writing of the landlord;\n"
            "(c) that the tenant has used the premises for a purpose other than that for which they were let...;\n"
            "(e) that the premises let for residential purposes are required bona fide by the landlord for occupation as a residence for himself or for any member of his family dependent on him, if he is the owner thereof, or for any person for whose benefit the premises are held and that the landlord or such person has no other reasonably suitable residential accommodation."
        ),
        "effective_date": "1959-02-09",
        "enactment_date": "1958-12-31",
        "legal_status": "In Force",
        "legal_status_notes": "Statutory protection against eviction for rent <= ₹3,500/month. Notice of demand gives 2 months to pay arrears.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/1531",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["protection against eviction", "non-payment of rent", "notice of demand", "two months cure period", "bona fide requirement", "subletting"],
        "cross_references": ["Section 3", "Section 25B"]
    },

    # =========================================================================
    # MAHARASHTRA RENT CONTROL ACT, 1999 (Maharashtra Act No. XVIII of 2000)
    # =========================================================================
    {
        "id": "IND-MH-MRCA-1999-SEC-003",
        "parent_doc_id": "IND-MH-MRCA-1999",
        "law_title": "The Maharashtra Rent Control Act, 1999",
        "short_title": "Maharashtra Rent Control Act, 1999",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Maharashtra",
        "section_or_rule_number": "Section 3",
        "section_or_rule_title": "Exemption from Act",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "(1) This Act shall not apply—\n"
            "(a) to any premises belonging to the Government or a local authority or apply as against the Government to any tenancy, licence or other like relationship created by a grant from a Government in respect of premises taken on lease or requisitioned by the Government; but it shall apply in respect of premises let, or given on licence, to the Government or a local authority or taken on behalf of the Government on such lease by or in the name of a person holding a specified office;\n"
            "(b) to any premises let or sub-let to banks, or any Public Sector Undertakings or any Corporation established by or under any Central or State Act, or foreign missions, international agencies, multinational companies, and private limited companies and public limited companies having a paid up share capital of rupees one crore or more.\n"
            "Explanation.—For the purpose of this clause, the expression 'bank' means— (i) any bank included in the Second Schedule to the Reserve Bank of India Act, 1934; (ii) any corresponding new bank...;\n"
            "(2) The State Government may, by notification in the Official Gazette, direct that this Act shall not apply to premises used for public purposes of a charitable nature or to any class of premises used for such purposes."
        ),
        "effective_date": "2000-03-31",
        "enactment_date": "2000-03-10",
        "legal_status": "In Force",
        "legal_status_notes": (
            "CRITICAL EXEMPTION RULE FOR MAHARASHTRA: Section 3(1)(b) excludes banks, PSUs, multinational corporations, "
            "and companies with paid-up capital of ₹1 Crore or more. Such corporate tenancies fall under TPA 1882."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2464",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["exemption", "banks", "PSUs", "corporate tenancy", "one crore share capital", "multinational companies"],
        "cross_references": ["IND-FED-TPA-1882-SEC-105", "Section 24", "Section 55"]
    },
    {
        "id": "IND-MH-MRCA-1999-SEC-024",
        "parent_doc_id": "IND-MH-MRCA-1999",
        "law_title": "The Maharashtra Rent Control Act, 1999",
        "short_title": "Maharashtra Rent Control Act, 1999",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Maharashtra",
        "section_or_rule_number": "Section 24",
        "section_or_rule_title": "Landlord's right to recover possession of premises given on licence on expiry",
        "chapter_or_part": "Chapter VII: Summary Disposal of Certain Applications",
        "exact_text": (
            "(1) Notwithstanding anything contained in this Act, a licensee in possession or occupation of premises given to him "
            "on licence for residence shall deliver possession of such premises to the landlord on expiry of the period of licence; "
            "and on the failure of the licensee to so deliver the possession of the licensed premises, a landlord shall be entitled "
            "to recover possession of such premises from a licensee, on the expiry of the period of licence, by making an application "
            "to the Competent Authority, and the Competent Authority, on being satisfied that the period of licence has expired, "
            "shall pass an order for eviction of a licensee.\n"
            "(2) Any licensee who does not deliver possession of the premises to the landlord on expiry of the period of licence and "
            "continues to be in possession of the licensed premises till he is dispossessed by the Competent Authority shall be liable "
            "to pay damages at double the rate of the licence fee or charge of the premises fixed under the agreement of licence.\n"
            "(3) The Competent Authority shall not entertain any claim of whatever nature from any other person who is not a licensee "
            "according to the agreement of licence.\n"
            "Explanation.—For the purposes of this section,—\n"
            "(a) the expression 'landlord' includes a successor-in-interest who becomes the landlord of the premises by reason of death of such landlord or otherwise;\n"
            "(b) an agreement of licence in writing shall be conclusive evidence of the fact stated therein."
        ),
        "effective_date": "2000-03-31",
        "enactment_date": "2000-03-10",
        "legal_status": "In Force",
        "legal_status_notes": (
            "CRITICAL LEAVE & LICENSE RECOVERY: Fast-track summary eviction before the Competent Authority. "
            "Licensee overstaying after expiry must pay DOUBLE THE LICENSE FEE as statutory damages."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2464",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["leave and license", "summary eviction", "Competent Authority", "double license fee", "damages for overstay", "written agreement conclusive evidence"],
        "cross_references": ["Section 55"]
    },
    {
        "id": "IND-MH-MRCA-1999-SEC-055",
        "parent_doc_id": "IND-MH-MRCA-1999",
        "law_title": "The Maharashtra Rent Control Act, 1999",
        "short_title": "Maharashtra Rent Control Act, 1999",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Maharashtra",
        "section_or_rule_number": "Section 55",
        "section_or_rule_title": "Tenancy agreement to be compulsorily registered",
        "chapter_or_part": "Chapter IX: Miscellaneous",
        "exact_text": (
            "(1) Notwithstanding anything contained in this Act or any other law for the time being in force, any agreement for a licence "
            "or letting of any premises, entered into between the landlord and the tenant or the licensee, as the case may be, after the "
            "commencement of this Act, shall be in writing and shall be registered under the Registration Act, 1908.\n"
            "(2) The responsibility of getting such agreement registered shall be on the landlord and in the absence of the written registered "
            "agreement, the contention of the tenant about the terms and conditions, subject to which a premises have been given on licence or "
            "let to him by the landlord, shall prevail, unless proved otherwise.\n"
            "(3) Any landlord who contravenes the provisions of this section shall, on conviction, be punished with imprisonment which may "
            "extend to three months or with fine not exceeding rupees five thousand or with both."
        ),
        "effective_date": "2000-03-31",
        "enactment_date": "2000-03-10",
        "legal_status": "In Force",
        "legal_status_notes": (
            "CRUCIAL STATUTORY MANDATE: Every rental/leave and license agreement in Maharashtra MUST be in writing and registered. "
            "Landlord is legally responsible for registration; failure flips the burden of proof (tenant's word prevails) and "
            "subjects landlord to criminal conviction (up to 3 months imprisonment or ₹5,000 fine)."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/2464",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["compulsory registration", "leave and license registration", "landlord responsibility", "tenant contention prevails", "criminal penalty", "three months imprisonment"],
        "cross_references": ["Section 24"]
    },

    # =========================================================================
    # KARNATAKA RENT ACT, 1999 (Karnataka Act No. 34 of 2001)
    # =========================================================================
    {
        "id": "IND-KA-KRA-1999-SEC-002",
        "parent_doc_id": "IND-KA-KRA-1999",
        "law_title": "The Karnataka Rent Act, 1999",
        "short_title": "Karnataka Rent Act, 1999",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Karnataka",
        "section_or_rule_number": "Section 2",
        "section_or_rule_title": "Application of the Act (The ₹3,500 Threshold and Exemptions)",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "(1) Chapters I to III and Chapters V to VIII of this Act shall apply to areas specified in the First Schedule.\n"
            "(2) Chapters I and IV shall apply to areas specified in the Second Schedule.\n"
            "(3) Nothing contained in this Act shall apply—\n"
            "(a) to any premises belonging to the State Government or the Central Government or a local authority or a Muzrai or religious or charitable institution or a wakf;\n"
            "(b) to any building belonging to a co-operative society...;\n"
            "(c) to any premises let to a bank, or any Public Sector Undertaking or any Corporation established by or under any Central or State Act, or foreign missions, international agencies, multinational companies and private limited companies and public limited companies having a paid up share capital of rupees one crore or more;\n"
            "(e) to any premises, deemed rent on the date of commencement of this Act or the standard rent of which exceeds—\n"
            "  (i) three thousand five hundred rupees per month in any area referred to in Part A of the First Schedule; and\n"
            "  (ii) two thousand rupees per month in any other area;\n"
            "(g) to any premises being a commercial building having a plinth area of more than fourteen square meters."
        ),
        "effective_date": "2001-12-31",
        "enactment_date": "2001-11-22",
        "legal_status": "In Force",
        "legal_status_notes": (
            "CRITICAL KARNATAKA RENT THRESHOLD: Section 2(3)(e) excludes premises with monthly rent > ₹3,500 in Bengaluru "
            "and other Part A cities (> ₹2,000 elsewhere), and commercial premises > 14 sq meters. "
            "Such tenancies fall under the Transfer of Property Act, 1882."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "http://dpal.karnataka.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["Karnataka rent threshold", "three thousand five hundred rupees", "Bengaluru rent exemption", "commercial 14 sq meters", "banks and corporate exemption"],
        "cross_references": ["IND-FED-TPA-1882-SEC-105", "Section 4", "Section 27"]
    },
    {
        "id": "IND-KA-KRA-1999-SEC-004",
        "parent_doc_id": "IND-KA-KRA-1999",
        "law_title": "The Karnataka Rent Act, 1999",
        "short_title": "Karnataka Rent Act, 1999",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Karnataka",
        "section_or_rule_number": "Section 4",
        "section_or_rule_title": "Registration of tenancy agreement",
        "chapter_or_part": "Chapter II: Lease of Buildings",
        "exact_text": (
            "(1) Notwithstanding anything contained in section 107 of the Transfer of Property Act, 1882, no person shall, "
            "after the commencement of this Act, let or take on rent any premises except by an agreement in writing.\n"
            "(2) Every agreement referred to in sub-section (1) shall be registered with the Controller within such period and in such manner "
            "and on payment of such fee as may be prescribed.\n"
            "(3) Where an agreement has been entered into before the commencement of this Act, the landlord and tenant shall, within six months "
            "from such commencement, enter into an agreement in writing and get it registered with the Controller."
        ),
        "effective_date": "2001-12-31",
        "enactment_date": "2001-11-22",
        "legal_status": "In Force",
        "legal_status_notes": "Mandates written agreement and registration with Rent Controller.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "http://dpal.karnataka.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["tenancy agreement", "compulsory written agreement", "registration with Controller"],
        "cross_references": ["Section 2", "Section 27"]
    },
    {
        "id": "IND-KA-KRA-1999-SEC-027",
        "parent_doc_id": "IND-KA-KRA-1999",
        "law_title": "The Karnataka Rent Act, 1999",
        "short_title": "Karnataka Rent Act, 1999",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Karnataka",
        "section_or_rule_number": "Section 27",
        "section_or_rule_title": "Protection of tenants against eviction",
        "chapter_or_part": "Chapter VI: Regulation of Eviction",
        "exact_text": (
            "(1) Notwithstanding anything to the contrary contained in any other law or contract, no order or decree for the recovery "
            "of possession of any premises shall be made by any Court, or other authority in favour of the landlord against the tenant: "
            "Provided that the Court may, on an application made to it in the prescribed manner, make an order for the recovery of possession "
            "of the premises on one or more of the following grounds only, namely:—\n"
            "(a) that the tenant has neither paid nor tendered the whole of the arrears of the rent and other charges legally recoverable from him within two months of the date on which a notice of demand for payment of the arrears of rent and other charges has been served on him by the landlord in the manner provided in section 106 of the Transfer of Property Act, 1882;\n"
            "(b) that the tenant has sub-let the whole or any part of the premises without the consent in writing of the landlord;\n"
            "(r) that the premises are required, whether in the same form or after reconstruction or re-building, by the landlord for occupation for himself or for any member of his family if he is the owner thereof, or for any person for whose benefit the premises are held and that the landlord or such person has no other reasonably suitable accommodation."
        ),
        "effective_date": "2001-12-31",
        "enactment_date": "2001-11-22",
        "legal_status": "In Force",
        "legal_status_notes": "Statutory grounds of eviction for premises under rent control. 2 months notice for rent arrears.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "http://dpal.karnataka.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["protection against eviction", "arrears of rent", "notice of demand", "two months cure period", "bona fide requirement"],
        "cross_references": ["Section 2", "Section 31"]
    },

    # =========================================================================
    # TAMIL NADU REGULATION OF RIGHTS AND RESPONSIBILITIES OF LANDLORDS AND TENANTS ACT, 2017
    # =========================================================================
    {
        "id": "IND-TN-TNRRRLTA-2017-SEC-004",
        "parent_doc_id": "IND-TN-TNRRRLTA-2017",
        "law_title": "The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017",
        "short_title": "TNRRRLT Act, 2017",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Tamil Nadu",
        "section_or_rule_number": "Section 4",
        "section_or_rule_title": "Tenancy Agreement (Compulsory Registration on Tenancy Portal)",
        "chapter_or_part": "Chapter II: Tenancy",
        "exact_text": (
            "(1) Notwithstanding anything contained in section 107 of the Transfer of Property Act, 1882, no person shall, "
            "after the commencement of this Act, let or take on rent any premises except by an agreement in writing, "
            "which shall be informed to the Rent Authority by the landlord and tenant jointly, in the form specified in the First Schedule.\n"
            "(2) Where, in relation to a tenancy created before the commencement of this Act,—\n"
            "(a) an agreement in writing was already entered into, it shall be informed to the Rent Authority within a period of ninety days from the date of commencement of this Act;\n"
            "(b) no agreement in writing was entered into, the landlord and the tenant shall, within a period of ninety days from the date of commencement of this Act, enter into an agreement in writing and inform the Rent Authority:\n"
            "Provided that if the landlord and the tenant fail to agree upon the terms of tenancy within ninety days, they shall be entitled to terminate the tenancy.\n"
            "(3) Every agreement referred to in sub-section (1) or sub-section (2) shall be registered by the Rent Authority within thirty days from the date of receipt of the tenancy agreement and a registration number shall be allotted to the parties."
        ),
        "effective_date": "2019-02-22",
        "enactment_date": "2017-08-04",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enforced vide G.O. Ms. No. 35 w.e.f. 22 February 2019. ALL tenancies in Tamil Nadu must be created by written agreement "
            "and registered on the official Tenancy Portal (tenancy.tn.gov.in) with the Rent Authority."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://tenancy.tn.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["tenancy agreement", "written agreement", "Rent Authority", "registration within ninety days", "tenancy portal", "registration number"],
        "cross_references": ["Section 5", "Section 11", "Section 21"]
    },
    {
        "id": "IND-TN-TNRRRLTA-2017-SEC-009",
        "parent_doc_id": "IND-TN-TNRRRLTA-2017",
        "law_title": "The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017",
        "short_title": "TNRRRLT Act, 2017",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Tamil Nadu",
        "section_or_rule_number": "Section 9",
        "section_or_rule_title": "Revision of rent",
        "chapter_or_part": "Chapter II: Tenancy",
        "exact_text": (
            "(1) Revision of rent between the landlord and the tenant shall be as per the terms of the tenancy agreement.\n"
            "(2) Save as agreed in the tenancy agreement, the landlord shall give a notice in writing three months before the revised rent "
            "becomes due.\n"
            "(3) If a tenant who has been given notice of an intended increase of rent under sub-section (2) fails to give the landlord notice of "
            "termination of the tenancy before the date from which the increase is to take effect, he shall be deemed to have accepted the increase."
        ),
        "effective_date": "2019-02-22",
        "enactment_date": "2017-08-04",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced w.e.f. 22 February 2019. 3 months written notice required for revising rent.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://tenancy.tn.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["revision of rent", "three months notice", "deemed acceptance"],
        "cross_references": ["Section 4", "Section 11"]
    },
    {
        "id": "IND-TN-TNRRRLTA-2017-SEC-011",
        "parent_doc_id": "IND-TN-TNRRRLTA-2017",
        "law_title": "The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017",
        "short_title": "TNRRRLT Act, 2017",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Tamil Nadu",
        "section_or_rule_number": "Section 11",
        "section_or_rule_title": "Security deposit (Statutory Cap)",
        "chapter_or_part": "Chapter II: Tenancy",
        "exact_text": (
            "(1) Save as otherwise agreed in the tenancy agreement, the security deposit to be paid by the tenant in advance shall be—\n"
            "(a) not exceeding three months' rent, in case of residential premises; and\n"
            "(b) not exceeding one month's rent, in case of non-residential premises.\n"
            "(2) The security deposit shall be refunded to the tenant within one month of delivery of vacant possession of the premises: "
            "Provided that the landlord shall be entitled to deduct from the security deposit such amount as may be necessary to meet "
            "the arrears of rent and other charges or damages to the premises caused by the tenant."
        ),
        "effective_date": "2019-02-22",
        "enactment_date": "2017-08-04",
        "legal_status": "In Force",
        "legal_status_notes": (
            "CRITICAL SECURITY DEPOSIT PROTECTION: Limits security deposit advance in Tamil Nadu to a MAXIMUM OF 3 MONTHS' RENT "
            "for residential tenancies (and 1 month for commercial), and mandates refund within 1 month of vacating."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://tenancy.tn.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["security deposit cap", "three months rent limit", "one month for commercial", "refund within one month", "deposit deductions"],
        "cross_references": ["Section 4", "Section 9", "IND-FED-LIM-1963-ART-022"]
    },
    {
        "id": "IND-TN-TNRRRLTA-2017-SEC-021",
        "parent_doc_id": "IND-TN-TNRRRLTA-2017",
        "law_title": "The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017",
        "short_title": "TNRRRLT Act, 2017",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Tamil Nadu",
        "section_or_rule_number": "Section 21",
        "section_or_rule_title": "Repossession of the premises by the landlord",
        "chapter_or_part": "Chapter V: Repossession of the Premises by the Landlord",
        "exact_text": (
            "(1) The Rent Court may, on an application made to it in the prescribed form, make an order for the recovery of possession "
            "of the premises on one or more of the following grounds, namely:—\n"
            "(a) that the landlord and tenant have failed to agree into an agreement under sub-section (2) of section 4;\n"
            "(b) that the tenant has not paid the agreed rent payable in accordance with the terms of the tenancy agreement for two consecutive months;\n"
            "(c) that the tenant has parted with the possession of whole or any part of the premises without obtaining the written consent of the landlord;\n"
            "(e) that the tenant has given notice to vacate the premises and in consequence of that notice the landlord has contracted to sell or let the premises or has taken other steps as a result of which he would be seriously prejudiced if he does not obtain possession of the premises;\n"
            "(g) that the premises are required by the landlord for occupation by himself or any member of his family or for any person for whose benefit the premises were held."
        ),
        "effective_date": "2019-02-22",
        "enactment_date": "2017-08-04",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced w.e.f. 22 February 2019. Primary repossession grounds before Rent Court (failure to enter written agreement, 2 months unpaid rent, bona fide requirement).",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://tenancy.tn.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["repossession", "Rent Court", "two consecutive months unpaid rent", "failure to register agreement", "bona fide occupation"],
        "cross_references": ["Section 4", "Section 22"]
    },
    {
        "id": "IND-TN-TNRRRLTA-2017-SEC-022",
        "parent_doc_id": "IND-TN-TNRRRLTA-2017",
        "law_title": "The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017",
        "short_title": "TNRRRLT Act, 2017",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Tamil Nadu",
        "section_or_rule_number": "Section 22",
        "section_or_rule_title": "Compensation for failure to vacate (Holding Over Penalty)",
        "chapter_or_part": "Chapter V: Repossession of the Premises by the Landlord",
        "exact_text": (
            "Where a tenant fails to vacate the premises upon the expiration of the period of tenancy or upon the termination of the tenancy "
            "by a notice to quit or pursuant to an order of the Rent Court, the tenant shall be liable to pay to the landlord compensation—\n"
            "(a) of double the monthly rent for the first two months; and\n"
            "(b) of four times the monthly rent thereafter,\n"
            "for the period of delay in handing over vacant possession of the premises to the landlord."
        ),
        "effective_date": "2019-02-22",
        "enactment_date": "2017-08-04",
        "legal_status": "In Force",
        "legal_status_notes": (
            "STATUTORY HOLDING OVER PENALTY: Severe monetary penalty for tenants overstaying in Tamil Nadu: "
            "DOUBLE rent for the first 2 months, and FOUR TIMES rent for every subsequent month."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://tenancy.tn.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["compensation for failure to vacate", "double monthly rent", "four times monthly rent", "holding over penalty", "overstay"],
        "cross_references": ["Section 4", "Section 21"]
    },
    {
        "id": "IND-TN-TNRRRLTA-2017-SEC-047",
        "parent_doc_id": "IND-TN-TNRRRLTA-2017",
        "law_title": "The Tamil Nadu Regulation of Rights and Responsibilities of Landlords and Tenants Act, 2017",
        "short_title": "TNRRRLT Act, 2017",
        "act_or_rule_type": "State Act",
        "jurisdiction": "State of Tamil Nadu",
        "section_or_rule_number": "Section 47",
        "section_or_rule_title": "Repeal and savings",
        "chapter_or_part": "Chapter VIII: Miscellaneous",
        "exact_text": (
            "(1) The Tamil Nadu Buildings (Lease and Rent Control) Act, 1960 is hereby repealed.\n"
            "(2) Notwithstanding such repeal and subject to the provisions of this Act, all cases and other proceedings under the said Act "
            "pending, at the commencement of this Act, shall be continued and disposed of by the Controller or the Appellate Authority, "
            "as the case may be, in accordance with the provisions of the said Act, as if that Act had not been repealed."
        ),
        "effective_date": "2019-02-22",
        "enactment_date": "2017-08-04",
        "legal_status": "In Force",
        "legal_status_notes": "EXPRESS REPEAL: The Tamil Nadu Buildings (Lease and Rent Control) Act, 1960 stands repealed w.e.f. 22 February 2019.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://tenancy.tn.gov.in",
        "retrieval_date": "2026-11-09",
        "scope_category": "Rent Law",
        "key_topics": ["repeal and savings", "Tamil Nadu Buildings Act 1960 repealed"],
        "cross_references": ["Section 1"]
    }
]

for _p in PROVISIONS:
    _p.setdefault("effective_from", _p.get("effective_date"))
    _p.setdefault("repealed_on", None)

