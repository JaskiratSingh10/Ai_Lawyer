"""
Consumer Protection statutory data module:
- Consumer Protection Act, 2019 (Act No. 35 of 2019)
- Consumer Protection (E-Commerce) Rules, 2020 (G.S.R. 462(E))
- Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021 (G.S.R. 912(E))
- Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020 (G.S.R. 449(E))
"""

DOCUMENTS = [
    {
        "id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "act_number": "Act No. 35 of 2019",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "2019-08-09",
        "effective_date": "2020-07-20",
        "effective_from": "2020-07-20",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enacted by Parliament on 9 August 2019. Major provisions (Chapters I, II, IV, VI, VII, VIII) "
            "brought into force on 20 July 2020 vide S.O. 2351(E) dated 15 July 2020. Central Consumer "
            "Protection Authority (CCPA) provisions (Sections 10, 20-27) brought into force on 24 July 2020 "
            "vide S.O. 2421(E) dated 23 July 2020. Section 107 expressly repealed the Consumer Protection Act, 1986. "
            "Pecuniary jurisdiction under sections 34, 47, and 58 modified by G.S.R. 912(E) effective 30 December 2021."
        ),
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "ministry": "Ministry of Consumer Affairs, Food and Public Distribution",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
    },
    {
        "id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "act_number": "G.S.R. 462(E)",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "2020-07-23",
        "effective_date": "2020-07-23",
        "effective_from": "2020-07-23",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Notified by Central Government vide G.S.R. 462(E) on 23 July 2020 in exercise of powers under "
            "Section 101(1)(zg) read with Section 94 of the Consumer Protection Act, 2019. In force from publication date."
        ),
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "ministry": "Ministry of Consumer Affairs, Food and Public Distribution",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
    },
    {
        "id": "IND-FED-CPJDR-2021",
        "law_title": "The Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021",
        "short_title": "Commission Jurisdiction Rules, 2021",
        "act_or_rule_type": "Central Rule",
        "act_number": "G.S.R. 912(E)",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "2021-12-30",
        "effective_date": "2021-12-30",
        "effective_from": "2021-12-30",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": (
            "Notified vide G.S.R. 912(E) on 30 December 2021 in exercise of powers conferred by sub-clause (i) "
            "of clause (a) of sub-section (1) of section 34, sub-clause (i) of clause (a) of sub-section (1) of "
            "section 47, and sub-clause (i) of clause (a) of sub-section (1) of section 58 read with section 101(2) "
            "of the Consumer Protection Act, 2019. Revises pecuniary thresholds: District up to 50 Lakhs; State from "
            "50 Lakhs to 2 Crores; National exceeding 2 Crores."
        ),
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "ministry": "Ministry of Consumer Affairs, Food and Public Distribution",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
    },
    {
        "id": "IND-FED-CPCDRC-2020",
        "law_title": "The Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020",
        "short_title": "Consumer Disputes Redressal Commissions Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "act_number": "G.S.R. 449(E)",
        "jurisdiction": "Central (Union of India)",
        "enactment_date": "2020-07-15",
        "effective_date": "2020-07-20",
        "effective_from": "2020-07-20",
        "repealed_on": None,
        "legal_status": "In Force",
        "legal_status_notes": "Notified vide G.S.R. 449(E) dated 15 July 2020 w.e.f. 20 July 2020. Governs complaint filing fees and commission procedures.",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "ministry": "Ministry of Consumer Affairs, Food and Public Distribution",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
    }
]

PROVISIONS = [
    # CPA 2019 - Short title & commencement
    {
        "id": "IND-FED-CPA-2019-SEC-001",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 1",
        "section_or_rule_title": "Short title, extent, commencement and application",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "(1) This Act may be called the Consumer Protection Act, 2019.\n"
            "(2) It extends to the whole of India.\n"
            "(3) It shall come into force on such date as the Central Government may, by notification, appoint "
            "and different dates may be appointed for different provisions of this Act and any reference in any such "
            "provision to the commencement of this Act shall be construed as a reference to the coming into force of that provision.\n"
            "(4) Save as otherwise expressly provided by the Central Government, by notification, this Act shall apply to all goods and services."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E) dated 15 July 2020.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["short title", "extent", "commencement", "application", "all goods and services"],
        "cross_references": ["S.O. 2351(E)", "S.O. 2421(E)"]
    },
    # CPA 2019 - Definitions
    {
        "id": "IND-FED-CPA-2019-SEC-002",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 2",
        "section_or_rule_title": "Definitions (Selected Operative Clauses for Consumer Disputes)",
        "chapter_or_part": "Chapter I: Preliminary",
        "exact_text": (
            "In this Act, unless the context otherwise requires,—\n"
            "(1) 'advertisement' means any audio or visual publicity, representation, endorsement or pronouncement made by means of light, sound, smoke, gas, print, electronic media, internet or website and includes any notice, circular, label, wrapper, invoice or such other documents;\n"
            "(5) 'complainant' means—\n"
            "  (i) a consumer; or\n"
            "  (ii) any voluntary consumer association registered under any law for the time being in force; or\n"
            "  (iii) the Central Government or any State Government; or\n"
            "  (iv) the Central Authority; or\n"
            "  (v) one or more consumers, where there are numerous consumers having the same interest; or\n"
            "  (vi) in case of death of a consumer, his legal heir or legal representative; or\n"
            "  (vii) in case of a consumer being a minor, his parent or legal guardian;\n"
            "(6) 'complaint' means any allegation in writing, made by a complainant for obtaining any relief provided by or under this Act, that—\n"
            "  (i) an unfair contract or unfair trade practice or a restrictive trade practice has been adopted by any trader or service provider;\n"
            "  (ii) the goods bought by him or agreed to be bought by him suffer from one or more defects;\n"
            "  (iii) the services hired or availed of or agreed to be hired or availed of by him suffer from any deficiency;\n"
            "  (iv) a trader or a service provider, as the case may be, has charged for the goods or for the services mentioned in the complaint, a price in excess of the price— (a) fixed by or under any law for the time being in force; or (b) displayed on the goods or any package containing such goods; or (c) displayed on the price list exhibited by him by or under any law for the time being in force; or (d) agreed between the parties;\n"
            "  (v) goods, which will be hazardous to life and safety when used, are being offered for sale to the public...;\n"
            "  (vi) services which are hazardous or likely to be hazardous to life and safety of the public when used, are being offered by a person who provides any service...;\n"
            "  (vii) a claim for product liability lies against the product manufacturer, product seller or product service provider, as the case may be;\n"
            "(7) 'consumer' means any person who—\n"
            "  (i) buys any goods for a consideration which has been paid or promised or partly paid and partly promised, or under any system of deferred payment and includes any user of such goods other than the person who buys such goods for consideration paid or promised or partly paid or partly promised, or under any system of deferred payment, when such use is made with the approval of such person, but does not include a person who obtains such goods for resale or for any commercial purpose; or\n"
            "  (ii) hires or avails of any service for a consideration which has been paid or promised or partly paid and partly promised, or under any system of deferred payment and includes any beneficiary of such service other than the person who hires or avails of the services for consideration paid or promised, or partly paid and partly promised, or under any system of deferred payment, when such services are availed of with the approval of the first mentioned person, but does not include a person who avails of such service for any commercial purpose.\n"
            "  Explanation.—For the purposes of this clause,—\n"
            "  (a) the expression 'commercial purpose' does not include use by a person of goods bought and used by him exclusively for the purpose of earning his livelihood, by means of self-employment;\n"
            "  (b) the expressions 'buys any goods' and 'hires or avails any services' includes offline or online transactions through electronic means or by teleshopping or direct selling or multi-level marketing;\n"
            "(10) 'defect' means any fault, imperfection or shortcoming in the quality, quantity, potency, purity or standard which is required to be maintained by or under any law for the time being in force or under any contract, express or implied, or as is claimed by the trader in any manner whatsoever in relation to any goods or product;\n"
            "(11) 'deficiency' means any fault, imperfection, shortcoming or inadequacy in the quality, nature and manner of performance which is required to be maintained by or under any law for the time being in force or has been undertaken to be performed by a person in pursuance of a contract or otherwise in relation to any service and includes—\n"
            "  (i) any act of negligence or omission or commission by such person which causes loss or injury to the consumer; and\n"
            "  (ii) deliberate withholding of relevant information by such person to the consumer;\n"
            "(16) 'e-commerce' means buying or selling of digital or physical goods or services including digital products over digital or electronic network;\n"
            "(17) 'electronic service provider' means a person who provides technologies or processes to enable a product seller to engage in advertising or selling goods or services to a consumer and includes any online marketplace or online auction sites;\n"
            "(34) 'product liability' means the responsibility of a product manufacturer or product seller, of any product or service, to compensate for any harm caused to a consumer by such defective product manufactured or sold or by deficiency in services relating thereto;\n"
            "(41) 'service' means service of any description which is made available to potential users and includes, but not limited to, the provision of facilities in connection with banking, financing, insurance, transport, processing, supply of electrical or other energy, telecom, boarding or lodging or both, housing construction, entertainment, amusement or the purveying of news or other information, but does not include the rendering of any service free of charge or under a contract of personal service;\n"
            "(46) 'unfair contract' means a contract between a manufacturer or trader or service provider on one hand, and a consumer on the other, having such terms which cause significant change in the rights of such consumer, including the following, namely:—\n"
            "  (i) requiring manifestly excessive security deposits to be given by a consumer for the performance of contractual obligations;\n"
            "  (ii) imposing any penalty on the consumer, for the breach of contract thereof which is wholly disproportionate to the loss occurred;\n"
            "  (iii) refusing to accept early repayment of debts on payment of applicable penalty;\n"
            "  (iv) entitling a party to the contract to terminate such contract unilaterally, without reasonable cause;\n"
            "  (v) permitting or has the effect of permitting one party to assign the contract to the detriment of the other party who is a consumer, without his consent; or\n"
            "  (vi) imposing on the consumer any unreasonable charge, obligation or condition which puts such consumer to disadvantage;\n"
            "(47) 'unfair trade practice' means a trade practice which, for the purpose of promoting the sale, use or supply of any goods or for the provision of any service, adopts any unfair method or unfair or deceptive practice including any of the following practices, namely:—\n"
            "  (i) making any statement, whether orally or in writing or by visible representation including by means of electronic record, which—\n"
            "    (a) falsely represents that the goods are of a particular standard, quality, quantity, grade, composition, style or model;\n"
            "    (b) falsely represents that the services are of a particular standard, quality or grade;\n"
            "    (c) falsely represents any rebuilt, second-hand, renovated, reconditioned or old goods as new goods;\n"
            "    (d) represents that the goods or services have sponsorship, approval, performance, characteristics, accessories, uses or benefits which such goods or services do not have;\n"
            "    (g) gives to the public any warranty or guarantee of the performance, efficacy or length of life of a product or of any goods that is not based on an adequate or proper test thereof;\n"
            "    (j) gives false or misleading facts disparaging the goods, services or trade of another person;\n"
            "  (ii) permitting the publication of any advertisement, whether in any newspaper or otherwise, including by way of electronic record, for the sale or supply at a bargain price of goods or services that are not intended to be offered for sale or supply at the bargain price...;\n"
            "  (iv) permitting the sale or supply of goods intended to be used, or of a kind likely to be used, by consumers, knowing or having reason to believe that the goods do not comply with the standards prescribed by competent authority...;\n"
            "  (vi) not issuing bill or cash memo or receipt for the goods sold or services rendered in such manner as may be prescribed;\n"
            "  (vii) refusing, after selling goods or rendering services, to take back or withdraw defective goods or to discontinue deficient services and to refund the consideration thereof within the period stipulated in the bill or cash memo or receipt or in the absence of such stipulation, within a period of thirty days;\n"
            "  (viii) disclosing to any other person any personal information given in confidence by the consumer unless such disclosure is made in accordance with the provisions of any law for the time being in force."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E) dated 15 July 2020.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["consumer definition", "defect", "deficiency", "service", "unfair trade practice", "unfair contract", "e-commerce", "product liability"],
        "cross_references": ["Section 34", "Section 35", "Section 39", "Section 83"]
    },
    # CPA 2019 - Section 34 (District Commission Jurisdiction)
    {
        "id": "IND-FED-CPA-2019-SEC-034",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 34",
        "section_or_rule_title": "Jurisdiction of District Commission",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) Subject to the other provisions of this Act, the District Commission shall have jurisdiction to entertain complaints "
            "where the value of the goods or services paid as consideration does not exceed one crore rupees:\n"
            "Provided that where the Central Government deems it necessary so to do, it may prescribe such other value, as it deems fit.\n"
            "(2) A complaint shall be instituted in a District Commission within the local limits of whose jurisdiction,—\n"
            "(a) the opposite party or each of the opposite parties, where there are more than one, at the time of the institution of the complaint, ordinarily resides or carries on business or has a branch office or personally works for gain; or\n"
            "(b) any of the opposite parties, where there are more than one, at the time of the institution of the complaint, actually and voluntarily resides, or carries on business or has a branch office, or personally works for gain, provided that in such case the permission of the District Commission is given; or\n"
            "(c) the cause of action, wholly or in part, arises; or\n"
            "(d) the complainant resides or personally works for gain.\n"
            "(3) The Central Government may, by notification, make rules providing for the manner in which the complaints may be filed electronically, "
            "the manner of payment of fees and the manner of payment of amount of pre-deposit."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enforced vide S.O. 2351(E) dated 15 July 2020. IMPORTANT: Pursuant to the proviso to sub-section (1), "
            "the Central Government notified the Consumer Protection (Jurisdiction of the District Commission, the State Commission "
            "and the National Commission) Rules, 2021 (G.S.R. 912(E) dated 30 Dec 2021). Under Rule 3 thereof, the pecuniary jurisdiction "
            "of the District Commission was revised downwards from 'does not exceed one crore rupees' to 'does not exceed fifty lakh rupees'."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["pecuniary jurisdiction", "territorial jurisdiction", "District Commission", "residence of complainant", "electronic filing"],
        "cross_references": ["IND-FED-CPJDR-2021-RULE-003", "Section 35", "Section 47", "Section 58"]
    },
    # CPA 2019 - Section 35
    {
        "id": "IND-FED-CPA-2019-SEC-035",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 35",
        "section_or_rule_title": "Manner in which complaint shall be made",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) A complaint, in relation to any goods sold or delivered or agreed to be sold or delivered or any service provided or agreed to be provided, may be filed with a District Commission by—\n"
            "(a) the consumer,— (i) to whom such goods are sold or delivered or agreed to be sold or delivered or such service is provided or agreed to be provided; or (ii) who alleges unfair trade practice in respect of such goods or service;\n"
            "(b) any recognised consumer association, whether the consumer to whom the goods sold or delivered or agreed to be sold or delivered or service provided or agreed to be provided, or in respect of whom unfair trade practice has been alleged, is a member of such association or not;\n"
            "(c) one or more consumers, where there are numerous consumers having the same interest, with the permission of the District Commission, on behalf of, or for the benefit of, all consumers so interested; or\n"
            "(d) the Central Government, the Central Authority or the State Government, as the case may be:\n"
            "Provided that the complaint under this sub-section may be filed electronically in such manner as may be prescribed.\n"
            "(2) Every complaint filed under sub-section (1) shall be accompanied with such fee and in such manner as may be prescribed.\n"
            "(3) Each District Commission shall maintain a consumer mediation cell for the purpose of settlement of disputes under this Act."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Allows e-filing via e-Daakhil portal.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["filing complaint", "standing", "e-daakhil", "class complaint", "fees"],
        "cross_references": ["Section 34", "Section 36", "Section 38"]
    },
    # CPA 2019 - Section 36
    {
        "id": "IND-FED-CPA-2019-SEC-036",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 36",
        "section_or_rule_title": "Proceedings before District Commission",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) Every proceeding before the District Commission shall be conducted by the President of that Commission and atleast one member thereof, sitting together:\n"
            "Provided that where a member, for any reason, is unable to conduct a proceeding till it is completed, the President and the other member shall continue the proceeding from the stage at which it was last heard by the previous member.\n"
            "(2) On receipt of an application made under sub-section (1) of section 35, the District Commission may, by order, admit the complaint, or reject the same:\n"
            "Provided that the admissibility of the complaint shall ordinarily be decided within twenty-one days from the date on which the complaint was filed.\n"
            "(3) No complaint shall be rejected under sub-section (2) without giving the complainant an opportunity of being heard.\n"
            "(4) Where the District Commission admits the complaint, it may proceed with such complaint in accordance with the provisions of this Act."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Deemed admission after 21 days if not rejected.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["admission of complaint", "twenty-one days timeline", "opportunity of hearing"],
        "cross_references": ["Section 35", "Section 38"]
    },
    # CPA 2019 - Section 38
    {
        "id": "IND-FED-CPA-2019-SEC-038",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 38",
        "section_or_rule_title": "Procedure on admission of complaint",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) The District Commission shall, on admission of a complaint, or in respect of which reference is made under sub-section (1) of section 37, within twenty-one days from the date of admission, refer a copy of the admitted complaint to the opposite party, directing him to give his version of the case within a period of thirty days or such extended period not exceeding fifteen days as may be granted by it.\n"
            "(2) Where the opposite party on receipt of a complaint referred to him under sub-section (1)—\n"
            "(a) denies or disputes the allegations contained in the complaint; or\n"
            "(b) omits or fails to take any action to represent his case within the time given by the District Commission, it shall proceed to settle the consumer dispute—\n"
            "  (i) on the basis of evidence brought to its notice by the complainant and the opposite party, where the opposite party denies or disputes the allegations; or\n"
            "  (ii) decide the consumer dispute ex parte on the basis of evidence brought to its notice by the complainant, where the opposite party omits or fails to take any action to represent his case within the time given by the Commission.\n"
            "(3) Where the complaint relates to any goods which suffer from any defect which cannot be determined without proper analysis or test of the goods, the District Commission shall obtain a sample of the goods from the complainant and seal it and authenticate it... and refer such sample to such appropriate laboratory... with a direction to make analysis or test... and report its findings.\n"
            "(6) Every complaint shall be heard by the District Commission on the basis of affidavit and documentary evidence, and in no case oral examination or cross-examination shall be permitted unless the District Commission, for reasons to be recorded in writing, deems it necessary."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Strict 30+15 days timeline for written response.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["procedure", "written version", "30 days limit", "15 days extension", "ex parte", "laboratory testing", "affidavit evidence"],
        "cross_references": ["Section 36", "Section 39"]
    },
    # CPA 2019 - Section 39 (Findings and Remedies)
    {
        "id": "IND-FED-CPA-2019-SEC-039",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 39",
        "section_or_rule_title": "Findings of District Commission (Remedies)",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) Where the District Commission is satisfied that the goods complained against suffer from any of the defects specified in the complaint or that any of the allegations contained in the complaint about the services or any unfair trade practices, or claims for product liability are proved, it shall issue an order to the opposite party directing him to do one or more of the following things, namely:—\n"
            "(a) to remove the defect pointed out by the appropriate laboratory from the goods in question;\n"
            "(b) to replace the goods with new goods of similar description which shall be free from any defect;\n"
            "(c) to return to the complainant the price, or, as the case may be, the charges paid by the complainant along with such interest on such price or charges as may be decided by it;\n"
            "(d) to pay such amount as may be awarded by it as compensation to the consumer for any loss or injury suffered by the consumer due to the negligence of the opposite party: Provided that the District Commission shall have the power to grant punitive damages in such circumstances as it deems fit;\n"
            "(e) to pay such amount as may be awarded by it as compensation in a product liability action under Chapter VI;\n"
            "(f) to remove the defects in goods or deficiencies in the services in question;\n"
            "(g) to discontinue the unfair trade practice or restrictive trade practice and not to repeat them;\n"
            "(h) not to offer the hazardous or unsafe goods for sale;\n"
            "(i) to withdraw the hazardous goods from being offered for sale;\n"
            "(j) to cease manufacture of hazardous goods and to desist from offering services which are hazardous in nature;\n"
            "(k) to pay such sum as may be determined by it where it is of the opinion that loss or injury has been suffered by a large number of consumers who are not identifiable conveniently: Provided that the minimum amount of sum so payable shall not be less than twenty-five per cent. of the value of such defective goods sold or services provided, as the case may be, to such consumers...;\n"
            "(l) to issue corrective advertisement to neutralise the effect of misleading advertisement at the cost of the opposite party responsible for issuing such misleading advertisement;\n"
            "(m) to provide for adequate costs to parties; and\n"
            "(n) to cease and desist from issuing any misleading advertisement."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Primary statutory source for consumer remedies (refund, replacement, compensation, punitive damages).",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["remedies", "refund", "replacement", "compensation", "punitive damages", "costs", "corrective advertisement", "cease and desist"],
        "cross_references": ["Section 34", "Section 38", "Section 40", "Section 84", "Section 85"]
    },
    # CPA 2019 - Section 40 (Review)
    {
        "id": "IND-FED-CPA-2019-SEC-040",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 40",
        "section_or_rule_title": "Review by District Commission in certain cases",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "The District Commission shall have the power to review any of the order passed by it if there is an error "
            "apparent on the face of the record, either of its own motion or on an application made by any of the parties within "
            "thirty days of such order."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). New power introduced in 2019 Act (not present in 1986 Act).",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["review", "error apparent on face of record", "thirty days limit"],
        "cross_references": ["Section 39", "Section 41"]
    },
    # CPA 2019 - Section 41 (Appeal to State Commission)
    {
        "id": "IND-FED-CPA-2019-SEC-041",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 41",
        "section_or_rule_title": "Appeal to State Commission",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "Any person aggrieved by an order made by the District Commission may prefer an appeal against such order to the "
            "State Commission on the grounds of facts or law within a period of forty-five days from the date of the order, "
            "in such form and manner, as may be prescribed:\n"
            "Provided that the State Commission may entertain an appeal after the expiry of the said period of forty-five days "
            "if it is satisfied that there was sufficient cause for not filing it within that period:\n"
            "Provided further that no appeal by a person, who is required to pay any amount in terms of an order of the District Commission, "
            "shall be entertained by the State Commission unless the appellant has deposited fifty per cent. of that amount in the manner as may be prescribed."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). 45 days limitation period; mandatory 50% pre-deposit requirement.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["appeal", "State Commission", "forty-five days limit", "pre-deposit 50 percent", "sufficient cause"],
        "cross_references": ["Section 39", "Section 47"]
    },
    # CPA 2019 - Section 47 (State Commission Jurisdiction)
    {
        "id": "IND-FED-CPA-2019-SEC-047",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 47",
        "section_or_rule_title": "Jurisdiction of State Commission",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) Subject to the other provisions of this Act, the State Commission shall have jurisdiction—\n"
            "(a) to entertain—\n"
            "  (i) complaints where the value of the goods or services paid as consideration, exceeds rupees one crore, but does not exceed rupees ten crore:\n"
            "  Provided that where the Central Government deems it necessary so to do, it may prescribe such other value, as it deems fit;\n"
            "  (ii) complaints against unfair contracts, where the value of goods or services paid as consideration does not exceed ten crore rupees;\n"
            "  (iii) appeals against the orders of any District Commission within the State; and\n"
            "(b) to call for the records and pass appropriate orders in any consumer dispute which is pending before or has been decided by any District Commission in the State, where it appears to the State Commission that such District Commission has exercised a jurisdiction not vested in it by law, or has failed to exercise a jurisdiction so vested or has acted in exercise of its jurisdiction illegally or with material irregularity."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enforced vide S.O. 2351(E). IMPORTANT: Pursuant to proviso to sub-clause (i) of clause (a) of sub-section (1), "
            "the Central Government notified the Consumer Protection (Jurisdiction of the District Commission, the State Commission "
            "and the National Commission) Rules, 2021 (G.S.R. 912(E)). Under Rule 4 thereof, the State Commission's original pecuniary "
            "jurisdiction is revised to complaints where consideration paid 'exceeds fifty lakh rupees but does not exceed two crore rupees'."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["State Commission jurisdiction", "pecuniary limit", "unfair contracts", "appellate jurisdiction", "revisional jurisdiction"],
        "cross_references": ["IND-FED-CPJDR-2021-RULE-004", "Section 34", "Section 41", "Section 51", "Section 58"]
    },
    # CPA 2019 - Section 51 (Appeal to National Commission)
    {
        "id": "IND-FED-CPA-2019-SEC-051",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 51",
        "section_or_rule_title": "Appeal to National Commission",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) Any person aggrieved by an order made by the State Commission in exercise of its powers conferred by sub-clause (i) "
            "or (ii) of clause (a) of sub-section (1) of section 47 may prefer an appeal against such order to the National Commission within "
            "a period of thirty days from the date of the order in such form and manner as may be prescribed:\n"
            "Provided that the National Commission may entertain an appeal after the expiry of the said period of thirty days if it is satisfied "
            "that there was sufficient cause for not filing it within that period:\n"
            "Provided further that no appeal by a person, who is required to pay any amount in terms of an order of the State Commission, "
            "shall be entertained by the National Commission unless the appellant has deposited fifty per cent. of that amount in the manner as may be prescribed."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). 30 days limitation; 50% pre-deposit mandatory.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["appeal", "National Commission", "thirty days limit", "pre-deposit 50 percent"],
        "cross_references": ["Section 47", "Section 58", "Section 67"]
    },
    # CPA 2019 - Section 58 (National Commission Jurisdiction)
    {
        "id": "IND-FED-CPA-2019-SEC-058",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 58",
        "section_or_rule_title": "Jurisdiction of National Commission",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) Subject to the other provisions of this Act, the National Commission shall have jurisdiction—\n"
            "(a) to entertain—\n"
            "  (i) complaints where the value of the goods or services paid as consideration exceeds rupees ten crore: "
            "  Provided that where the Central Government deems it necessary so to do, it may prescribe such other value, as it deems fit;\n"
            "  (ii) complaints against unfair contracts, where the value of goods or services paid as consideration exceeds ten crore rupees;\n"
            "  (iii) appeals against the orders of any State Commission; and\n"
            "  (iv) appeals against the orders of the Central Authority; and\n"
            "(b) to call for the records and pass appropriate orders in any consumer dispute which is pending before or has been decided by any State Commission where it appears to the National Commission that such State Commission has exercised a jurisdiction not vested in it by law, or has failed to exercise a jurisdiction so vested, or has acted in the exercise of its jurisdiction illegally or with material irregularity."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enforced vide S.O. 2351(E). IMPORTANT: Pursuant to proviso to sub-clause (i) of clause (a) of sub-section (1), "
            "the Central Government notified the Consumer Protection (Jurisdiction of the District Commission, the State Commission "
            "and the National Commission) Rules, 2021 (G.S.R. 912(E)). Under Rule 5 thereof, the National Commission's original pecuniary "
            "jurisdiction is revised to complaints where consideration paid 'exceeds two crore rupees'."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["National Commission jurisdiction", "pecuniary limit", "exceeds two crore rupees", "appellate jurisdiction", "revisional jurisdiction"],
        "cross_references": ["IND-FED-CPJDR-2021-RULE-005", "Section 47", "Section 51", "Section 67"]
    },
    # CPA 2019 - Section 69 (Limitation Period)
    {
        "id": "IND-FED-CPA-2019-SEC-069",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 69",
        "section_or_rule_title": "Limitation period",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) The District Commission, the State Commission or the National Commission shall not admit a complaint unless it is filed within two years from the date on which the cause of action has arisen.\n"
            "(2) Notwithstanding anything contained in sub-section (1), a complaint may be entertained after the period specified in sub-section (1), if the complainant satisfies the District Commission, the State Commission or the National Commission, as the case may be, that he had sufficient cause for not filing the complaint within such period:\n"
            "Provided that no such complaint shall be entertained unless the District Commission or the State Commission or the National Commission, as the case may be, records its reasons for condoning such delay."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Special limitation of 2 years overrides general Limitation Act 1963 by virtue of Section 29(2) thereof.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["limitation period", "two years", "cause of action", "condonation of delay", "sufficient cause"],
        "cross_references": ["IND-FED-LIM-1963-SEC-029", "Section 35", "Section 47", "Section 58"]
    },
    # CPA 2019 - Section 71 (Enforcement of Orders)
    {
        "id": "IND-FED-CPA-2019-SEC-071",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 71",
        "section_or_rule_title": "Enforcement of orders of District Commission, State Commission and National Commission",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "Every order made by a District Commission, State Commission or the National Commission shall be enforced by it in the same manner as if it were a decree of a civil court made by a court in a suit being heard by it and it shall be lawful for the District Commission, State Commission or the National Commission to send, in the event of its inability to execute it, such order to the court within the local limits of whose jurisdiction,—\n"
            "(a) in the case of an order against a company, the registered office of the company is situated; or\n"
            "(b) in the case of an order against any other person, place where the person concerned voluntarily resides or carries on business or personally works for gain, is situated,\n"
            "and thereupon, the court to which the order is so sent, shall execute the order as if it were a decree of that court."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Orders enforceable as civil court decrees.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["enforcement of orders", "decree of civil court", "execution", "jurisdiction of civil court"],
        "cross_references": ["Section 39", "Section 72"]
    },
    # CPA 2019 - Section 72 (Penalty for non-compliance)
    {
        "id": "IND-FED-CPA-2019-SEC-072",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 72",
        "section_or_rule_title": "Penalty for non-compliance of order",
        "chapter_or_part": "Chapter IV: Consumer Disputes Redressal Commission",
        "exact_text": (
            "(1) Whoever fails to comply with any order made by the District Commission or the State Commission or the National Commission, as the case may be, shall be punishable with imprisonment for a term which shall not be less than one month, but which may extend to three years, or with fine, which shall not be less than twenty-five thousand rupees, but which may extend to one lakh rupees, or with both.\n"
            "(2) Notwithstanding anything contained in the Code of Criminal Procedure, 1973, the District Commission, the State Commission or the National Commission, as the case may be, shall have the power of a Judicial Magistrate of the first class for the trial of offences under sub-section (1), and on conferment of such powers, the District Commission or the State Commission or the National Commission, as the case may be, shall be deemed to be a Judicial Magistrate of the first class for the purposes of the Code of Criminal Procedure, 1973.\n"
            "(3) Save as otherwise provided, the offences under sub-section (1) may be tried summarily by the District Commission or the State Commission or the National Commission, as the case may be."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Grants criminal judicial magistrate powers to commissions.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["penalty", "non-compliance", "imprisonment", "fine", "Judicial Magistrate of First Class", "summary trial"],
        "cross_references": ["Section 71"]
    },
    # CPA 2019 - Product Liability Sections (ss. 82-87)
    {
        "id": "IND-FED-CPA-2019-SEC-083",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 83",
        "section_or_rule_title": "Product liability action",
        "chapter_or_part": "Chapter VI: Product Liability",
        "exact_text": (
            "A product liability action may be brought by a complainant before a District Commission or State Commission or National Commission, as the case may be, for claiming compensation for the harm caused to him on account of a defective product made or sold or by deficiency in services relating to such product."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Introduces statutory product liability in India.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["product liability", "compensation for harm", "defective product", "deficiency in service"],
        "cross_references": ["Section 84", "Section 85", "Section 86", "Section 87"]
    },
    {
        "id": "IND-FED-CPA-2019-SEC-084",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 84",
        "section_or_rule_title": "Liability of product manufacturer",
        "chapter_or_part": "Chapter VI: Product Liability",
        "exact_text": (
            "(1) A product manufacturer shall be liable in a product liability action, if—\n"
            "(a) the product contains a manufacturing defect; or\n"
            "(b) the product is defective in design; or\n"
            "(c) there is a deviation from manufacturing specifications; or\n"
            "(d) the product does not conform to the express warranty; or\n"
            "(e) the product fails to contain adequate instructions of correct usage to prevent any harm or any warning regarding improper or incorrect usage.\n"
            "(2) A product manufacturer shall be liable in a product liability action even if he proves that he was not negligent or fraudulent in making the express warranty of a product."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Strict liability regime irrespective of absence of negligence.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["manufacturer liability", "manufacturing defect", "design defect", "express warranty", "warnings", "strict liability"],
        "cross_references": ["Section 83", "Section 87"]
    },
    {
        "id": "IND-FED-CPA-2019-SEC-085",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 85",
        "section_or_rule_title": "Liability of product service provider",
        "chapter_or_part": "Chapter VI: Product Liability",
        "exact_text": (
            "A product service provider shall be liable in a product liability action, if—\n"
            "(a) the service provided by him was faulty or imperfect or deficient or inadequate in quality, nature or manner of performance which is required to be provided by or under any law for the time being in force, or pursuant to any contract or otherwise; or\n"
            "(b) there was an act of omission or commission or negligence or conscious withholding any information which caused harm; or\n"
            "(c) the service provider did not issue adequate instructions or warnings to prevent any harm; or\n"
            "(d) the service did not conform to express warranty or the terms and conditions of the contract."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E).",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["service provider liability", "deficient service", "omission", "negligence", "breach of contract warranty"],
        "cross_references": ["Section 83", "Section 87"]
    },
    {
        "id": "IND-FED-CPA-2019-SEC-086",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 86",
        "section_or_rule_title": "Liability of product seller",
        "chapter_or_part": "Chapter VI: Product Liability",
        "exact_text": (
            "A product seller who is not a product manufacturer shall be liable in a product liability action, if—\n"
            "(a) he has exercised substantial control over the designing, testing, manufacturing, packaging or labelling of a product that caused harm; or\n"
            "(b) he has altered or modified the product and such alteration or modification was the substantial factor in causing the harm; or\n"
            "(c) he has made an express warranty with respect to the product independent of any express warranty made by a product manufacturer and such product failed to conform to the express warranty made by the product seller, which caused the harm; or\n"
            "(d) the product has been sold by him and the identity of product manufacturer of such product is not known, or if known, the service of notice or process or warrant cannot be effected on him or he is not subject to the law which is in force in India or the order, if any, passed or to be passed cannot be enforced against him; or\n"
            "(e) he failed to exercise reasonable care in assembling, inspecting or maintaining such product or he did not pass on the warnings or instructions of the product manufacturer regarding the dangers involved or how to avoid such dangers, relating to the product while selling such product and such failure was the proximate cause of the harm."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Covers sellers and e-commerce platforms where manufacturer is unknown or unserviceable.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["seller liability", "substantial control", "unknown manufacturer", "failure of care", "e-commerce seller liability"],
        "cross_references": ["Section 83", "Section 87"]
    },
    {
        "id": "IND-FED-CPA-2019-SEC-087",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 87",
        "section_or_rule_title": "Exceptions to product liability action",
        "chapter_or_part": "Chapter VI: Product Liability",
        "exact_text": (
            "(1) A product liability action shall not lie against the product seller for harm caused by a product, if, at the time of doing the act, the product was misused, altered, or modified.\n"
            "(2) In any product liability action, the product manufacturer shall not be liable, if—\n"
            "(a) the product was purchased by an employer for use at the workplace and the product manufacturer had provided warnings or instructions to such employer, that would have avoided such harm...;\n"
            "(b) the product was sold as a component or material to be used in another product and necessary warnings were given...;\n"
            "(c) the product was one which was legally meant to be used or dispensed only by or under the supervision of an expert...;\n"
            "(d) the complainant, while using such product, was under the influence of alcohol or any prescription drug which had not been prescribed by a medical practitioner."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Defences available to manufacturers and sellers.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["exceptions", "product liability defences", "misuse", "alteration", "intoxication"],
        "cross_references": ["Section 84", "Section 86"]
    },
    # CPA 2019 - Section 107 (Repeal and Savings)
    {
        "id": "IND-FED-CPA-2019-SEC-107",
        "parent_doc_id": "IND-FED-CPA-2019",
        "law_title": "The Consumer Protection Act, 2019",
        "short_title": "Consumer Protection Act, 2019",
        "act_or_rule_type": "Central Act",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Section 107",
        "section_or_rule_title": "Repeal and savings",
        "chapter_or_part": "Chapter VIII: Miscellaneous",
        "exact_text": (
            "(1) The Consumer Protection Act, 1986 is hereby repealed.\n"
            "(2) Notwithstanding such repeal, anything done or any action taken or purported to have been done or taken under the Act hereby repealed shall, in so far as it is not inconsistent with the provisions of this Act, be deemed to have been done or taken under the corresponding provisions of this Act.\n"
            "(3) The mention of particular matters in sub-section (2) shall not be held to prejudice or affect the general application of section 6 of the General Clauses Act, 1897 with regard to the effect of repeal."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2019-08-09",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide S.O. 2351(E). Formally repealed Consumer Protection Act, 1986.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://www.indiacode.nic.in/handle/123456789/15256",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["repeal", "savings", "Consumer Protection Act 1986", "General Clauses Act 1897"],
        "cross_references": ["Section 1"]
    },

    # -------------------------------------------------------------
    # Consumer Protection (E-Commerce) Rules, 2020 (G.S.R. 462(E))
    # -------------------------------------------------------------
    {
        "id": "IND-FED-CPECR-2020-RULE-001",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 1",
        "section_or_rule_title": "Short title and commencement",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) These rules may be called the Consumer Protection (E-Commerce) Rules, 2020.\n"
            "(2) They shall come into force on the date of their publication in the Official Gazette."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Published in Gazette of India Extraordinary, Part II, Sec 3(i) vide G.S.R. 462(E) on 23 July 2020.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["short title", "commencement", "e-commerce rules"],
        "cross_references": ["IND-FED-CPA-2019-SEC-094", "IND-FED-CPA-2019-SEC-101"]
    },
    {
        "id": "IND-FED-CPECR-2020-RULE-002",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 2",
        "section_or_rule_title": "Scope and applicability",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) Save as otherwise expressly provided by the Central Government by notification, these rules shall apply to—\n"
            "(a) all goods and services bought or sold over digital or electronic network including digital products;\n"
            "(b) all models of e-commerce, including marketplace and inventory models of e-commerce;\n"
            "(c) all e-commerce retail, including multi-channel single brand retailers and single brand retailers in single or multiple formats; and\n"
            "(d) all forms of unfair trade practices across all models of e-commerce:\n"
            "Provided that these rules shall not apply to any activity of a natural person carried out in a personal capacity not being part of any professional or commercial activity undertaken on a regular or systematic basis.\n"
            "(2) Notwithstanding anything contained in sub-rule (1), these rules shall apply to an e-commerce entity which is not established in India, but systematically offers goods or services to consumers in India."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Applies extra-territorially to overseas e-commerce entities offering goods/services to consumers in India.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["scope", "applicability", "marketplace model", "inventory model", "overseas entities", "personal capacity exemption"],
        "cross_references": ["Rule 3", "Rule 4"]
    },
    {
        "id": "IND-FED-CPECR-2020-RULE-003",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 3",
        "section_or_rule_title": "Definitions",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) In these rules, unless the context otherwise requires,—\n"
            "(a) 'Act' means the Consumer Protection Act, 2019 (35 of 2019);\n"
            "(b) 'e-commerce entity' means any person who owns, operates or manages digital or electronic facility or platform for electronic commerce, but does not include a seller offering his goods or services for sale on a marketplace e-commerce entity;\n"
            "(c) 'grievance' includes any complaints to an e-commerce entity regarding any violation of the provisions of the Act and rules made thereunder;\n"
            "(d) 'GSTIN' means Goods and Services Tax Identification Number as defined in the Central Goods and Services Tax Act, 2017;\n"
            "(e) 'information' shall have the same meaning as assigned to it in clause (v) of sub-section (1) of section 2 of the Information Technology Act, 2000;\n"
            "(f) 'inventory e-commerce entity' means an e-commerce entity which owns the inventory of goods or services and sells such goods or services directly to the consumers and shall include single brand retailers and multi-channel single brand retailers;\n"
            "(g) 'marketplace e-commerce entity' means an e-commerce entity which provides an information technology platform on a digital or electronic network to facilitate transactions between buyers and sellers;\n"
            "(h) 'seller' means the product seller as defined in clause (37) of section 2 of the Act and includes a service provider;\n"
            "(i) 'user' means any person who accesses or avails any computer resource of an e-commerce entity."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Defines core operational entities in digital commerce.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["definitions", "e-commerce entity", "marketplace entity", "inventory entity", "seller", "user"],
        "cross_references": ["Rule 4", "Rule 5", "Rule 6", "Rule 7"]
    },
    {
        "id": "IND-FED-CPECR-2020-RULE-004",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 4",
        "section_or_rule_title": "Duties of e-commerce entities",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) Every e-commerce entity shall—\n"
            "(a) be a company incorporated under the Companies Act, 1956 or under the Companies Act, 2013 or a foreign company covered under clause (42) of section 2 of the Companies Act, 2013 or an office, branch or agency outside India owned or controlled by a person resident in India as provided in sub-clause (iii) of clause (v) of section 2 of the Foreign Exchange Management Act, 1999, and appoint a nodal person of contact or an alternate senior designated functionary who is a resident in India, to ensure compliance with the provisions of the Act or the rules made thereunder;\n"
            "(b) provide the following information in a clear and accessible manner on its platform, displayed prominently to its users, namely:—\n"
            "  (i) legal name of the e-commerce entity;\n"
            "  (ii) principal geographic address of its headquarters and all branches;\n"
            "  (iii) name and details of its website; and\n"
            "  (iv) contact details including email address, and mobile, landline and fax numbers of customer care as well as of grievance officer;\n"
            "(c) establish an adequate grievance redressal mechanism having regard to the number of grievances ordinarily received by such entity from India, and shall appoint a grievance officer for consumer grievance redressal, and shall display the name, contact details, and designation of such officer on its platform;\n"
            "(d) ensure that the grievance officer referred to in clause (c) acknowledges the receipt of any consumer complaint within forty-eight hours and redresses the complaint within one month from the date of receipt of the complaint;\n"
            "(e) where an e-commerce entity offers imported goods or services for sale, it shall mention the name and details of any importer from whom the goods or services have been purchased, or such seller who may be an importer;\n"
            "(f) every e-commerce entity shall endeavour on a best effort basis to become a partner in the convergence process of the National Consumer Helpline of the Central Government;\n"
            "(g) no e-commerce entity shall impose cancellation charges on consumers cancelling after confirming purchase unless similar charges are also borne by the e-commerce entity, if they cancel the purchase order unilaterally for any reason;\n"
            "(h) every e-commerce entity shall only record the consent of a consumer for the purchase of any good or service offered on its platform where such consent is expressed through an explicit and affirmative action, and no such entity shall record such consent automatically, including in the form of pre-ticked checkboxes;\n"
            "(i) every e-commerce entity shall effect all refunds for return of goods or services requested by consumers in accordance with the specifications prescribed by the Reserve Bank of India or any other competent authority under any law for the time being in force, within a reasonable period of time, or as prescribed under a given law;\n"
            "(j) no e-commerce entity shall— (a) manipulate the price of the goods or services offered on its platform in such a manner as to gain unreasonable profit by imposing on consumers any unjustified price having regard to the prevailing market conditions, the essential nature of the good or service, maintenance or other charges; (b) discriminate between consumers of the same class or make any arbitrary classification of consumers affecting their rights under the Act."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide G.S.R. 462(E). Mandates 48-hour acknowledgment, 1-month resolution, ban on pre-ticked boxes, refund compliance.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["duties of e-commerce", "nodal contact person", "grievance officer", "forty-eight hours acknowledgment", "one month redressal", "no pre-ticked boxes", "cancellation charges", "refunds", "price manipulation ban"],
        "cross_references": ["Rule 2", "Rule 5", "Rule 7"]
    },
    {
        "id": "IND-FED-CPECR-2020-RULE-005",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 5",
        "section_or_rule_title": "Liabilities of marketplace e-commerce entities",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) A marketplace e-commerce entity which seeks to avail the exemption from liability under sub-section (1) of section 79 of the Information Technology Act, 2000 shall comply with sub-sections (2) and (3) of that section, including the Information Technology (Intermediaries Guidelines) Rules, 2011.\n"
            "(2) Every marketplace e-commerce entity shall require an undertaking from its sellers to ensure that descriptions, images, and other content pertaining to goods or services on their platform are accurate and correspond directly with the appearance, nature, quality, purpose and other general features of such good or service.\n"
            "(3) Every marketplace e-commerce entity shall provide in a clear and accessible manner, displayed prominently to its users at the appropriate place on its platform:—\n"
            "(a) details about the sellers offering goods and services, including the name of their business, whether registered or not, their geographic address, customer care number, any rating or other aggregated feedback about such seller, and any other information necessary for enabling consumers to make informed decisions at the pre-purchase stage;\n"
            "(b) a ticket code for each complaint lodged through which the consumer may track the status of their complaint;\n"
            "(c) information relating to return, refund, exchange, warranty and guarantee, delivery and shipment, modes of payment, and grievance redressal mechanism, and any other similar information which may be required by consumers to make informed decisions;\n"
            "(d) information on available payment methods, the security of that payment methods, any fees or charges payable by users, the procedure to cancel regular payments under such methods, charge-back options, if any, and the contact information of the relevant payment service provider;\n"
            "(e) all information provided to it by sellers under sub-rule (5) of rule 6.\n"
            "(4) Every marketplace e-commerce entity shall explain the main parameters which, individually or collectively, are most significant in determining the ranking of goods or sellers on its platform and the relative importance of those parameters through easily understandable language.\n"
            "(5) Every marketplace e-commerce entity shall include in its terms and conditions a description of any differentiated treatment which it gives or might give between goods or services or sellers of the same category."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide G.S.R. 462(E). Imposes mandatory disclosures and ranking transparency on platforms.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["marketplace liability", "intermediary safe harbour", "ticket code", "ranking parameters", "differentiated treatment", "seller transparency"],
        "cross_references": ["Rule 4", "Rule 6"]
    },
    {
        "id": "IND-FED-CPECR-2020-RULE-006",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 6",
        "section_or_rule_title": "Duties of sellers on marketplace",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) No seller offering goods or services through a marketplace e-commerce entity shall adopt any unfair trade practice whether in the course of the business on its platform or otherwise.\n"
            "(2) No seller offering goods or services through a marketplace e-commerce entity shall falsely represent itself as a consumer and post reviews about goods or services or misrepresent the quality or the features of any goods or services.\n"
            "(3) No seller offering goods or services through a marketplace e-commerce entity shall refuse to take back goods, or withdraw or discontinue services purchased or agreed to be purchased, or refuse to refund consideration paid for goods or services, if such goods or services are defective, deficient or spurious, or if the goods or services are not of the characteristics or features as advertised or as agreed to, or if such goods or services are delivered late from the stated delivery schedule: Provided that in the case of late delivery, this sub-rule shall not apply if such late delivery was due to force majeure.\n"
            "(4) Any seller offering goods or services through a marketplace e-commerce entity shall—\n"
            "(a) have a prior written contract with the respective e-commerce entity in order to undertake or solicit sale or offer its goods or services on the platform;\n"
            "(b) appoint a grievance officer for consumer grievance redressal and ensure that the grievance officer acknowledges the receipt of any consumer complaint within forty-eight hours and redresses the complaint within one month from the date of receipt of the complaint;\n"
            "(c) ensure that the advertisements for marketing of goods or services are consistent with the actual characteristics, access and usage conditions of such goods or services;\n"
            "(d) provide to the marketplace e-commerce entity its legal name, principal geographic address, website address, contact details, GSTIN, PAN, and country of origin of goods."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide G.S.R. 462(E). Prohibits fake reviews and mandates refund for defective/late goods.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["duties of sellers", "fake reviews ban", "mandatory refund", "defective goods", "late delivery", "country of origin"],
        "cross_references": ["Rule 4", "Rule 5"]
    },
    {
        "id": "IND-FED-CPECR-2020-RULE-007",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 7",
        "section_or_rule_title": "Duties and liabilities of inventory e-commerce entities",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) Every inventory e-commerce entity which dishes out direct sales to consumers shall provide in a clear and accessible manner displayed prominently on its platform:—\n"
            "(a) accurate information relating to return, refund, exchange, warranty and guarantee, delivery and shipment, cost of return shipping, modes of payment, security of payment methods, and grievance redressal mechanism;\n"
            "(b) total price in single figure along with the breakup price for the good or service, showing all the compulsory and optional charges, and the applicable tax code;\n"
            "(c) all mandatory notices and information provided by applicable law, and the country of origin of the goods and services offered for sale.\n"
            "(2) No inventory e-commerce entity shall falsely represent itself as a consumer and post reviews about goods and services or misrepresent the quality or the features of any goods or services.\n"
            "(3) Every inventory e-commerce entity shall ensure that the advertisements for marketing of goods or services are consistent with the actual characteristics, access and usage conditions of such goods or services.\n"
            "(4) No inventory e-commerce entity shall refuse to take back goods, or withdraw or discontinue services purchased or agreed to be purchased, or refuse to refund consideration paid for goods or services, if such goods or services are defective, deficient, spurious, or if the goods or services are not of the characteristics or features as advertised or as agreed to, or if such goods or services are delivered late from the stated delivery schedule: Provided that in the case of late delivery, this sub-rule shall not apply if such late delivery was due to force majeure.\n"
            "(5) Every inventory e-commerce entity shall explicitly specify the expiry date of the goods offered for sale to consumers on its platform."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide G.S.R. 462(E). Holds inventory models strictly liable for defects, false reviews, and refunds.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["inventory e-commerce", "single figure price breakup", "mandatory refund", "expiry date display", "country of origin"],
        "cross_references": ["Rule 4", "Rule 6"]
    },
    {
        "id": "IND-FED-CPECR-2020-RULE-008",
        "parent_doc_id": "IND-FED-CPECR-2020",
        "law_title": "The Consumer Protection (E-Commerce) Rules, 2020",
        "short_title": "Consumer Protection (E-Commerce) Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 8",
        "section_or_rule_title": "Contravention of rules",
        "chapter_or_part": "Rules",
        "exact_text": (
            "The provisions of the Consumer Protection Act, 2019 (35 of 2019) shall apply for any contravention of the provisions of these rules."
        ),
        "effective_date": "2020-07-23",
        "enactment_date": "2020-07-23",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide G.S.R. 462(E). Directs penalties under CPA 2019.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["contravention", "penal action", "enforcement"],
        "cross_references": ["IND-FED-CPA-2019-SEC-072", "IND-FED-CPA-2019-SEC-088"]
    },

    # -----------------------------------------------------------------------------------------------------------------
    # Consumer Protection (Jurisdiction of District, State, and National Commission) Rules, 2021 (G.S.R. 912(E))
    # -----------------------------------------------------------------------------------------------------------------
    {
        "id": "IND-FED-CPJDR-2021-RULE-001",
        "parent_doc_id": "IND-FED-CPJDR-2021",
        "law_title": "The Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021",
        "short_title": "Commission Jurisdiction Rules, 2021",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 1",
        "section_or_rule_title": "Short title and commencement",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) These rules may be called the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021.\n"
            "(2) They shall come into force on the date of their publication in the Official Gazette."
        ),
        "effective_date": "2021-12-30",
        "enactment_date": "2021-12-30",
        "legal_status": "In Force",
        "legal_status_notes": "Published in Gazette of India Extraordinary, Part II, Sec 3(i) vide G.S.R. 912(E) on 30 December 2021.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["short title", "commencement", "jurisdiction rules"],
        "cross_references": ["IND-FED-CPA-2019-SEC-034", "IND-FED-CPA-2019-SEC-047", "IND-FED-CPA-2019-SEC-058"]
    },
    {
        "id": "IND-FED-CPJDR-2021-RULE-002",
        "parent_doc_id": "IND-FED-CPJDR-2021",
        "law_title": "The Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021",
        "short_title": "Commission Jurisdiction Rules, 2021",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 2",
        "section_or_rule_title": "Definitions",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) In these rules, unless the context otherwise requires,—\n"
            "(a) 'Act' means the Consumer Protection Act, 2019 (35 of 2019);\n"
            "(b) words and expressions used herein and not defined, but defined in the Act shall have the meanings respectively assigned to them in the Act."
        ),
        "effective_date": "2021-12-30",
        "enactment_date": "2021-12-30",
        "legal_status": "In Force",
        "legal_status_notes": "Enforced vide G.S.R. 912(E).",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["definitions", "Act"],
        "cross_references": ["IND-FED-CPA-2019-SEC-002"]
    },
    {
        "id": "IND-FED-CPJDR-2021-RULE-003",
        "parent_doc_id": "IND-FED-CPJDR-2021",
        "law_title": "The Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021",
        "short_title": "Commission Jurisdiction Rules, 2021",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 3",
        "section_or_rule_title": "Jurisdiction of District Commission",
        "chapter_or_part": "Rules",
        "exact_text": (
            "Subject to the other provisions of the Act, the District Commission shall have jurisdiction to entertain complaints "
            "where the value of the goods or services paid as consideration does not exceed fifty lakh rupees."
        ),
        "effective_date": "2021-12-30",
        "enactment_date": "2021-12-30",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enforced vide G.S.R. 912(E) on 30 December 2021. Operates under Section 34(1) proviso of CPA 2019. "
            "Replaced the statutory threshold of ₹1 Crore with ₹50 Lakhs (fifty lakh rupees)."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["District Commission", "pecuniary jurisdiction", "fifty lakh rupees", "consideration paid"],
        "cross_references": ["IND-FED-CPA-2019-SEC-034", "Rule 4", "Rule 5"]
    },
    {
        "id": "IND-FED-CPJDR-2021-RULE-004",
        "parent_doc_id": "IND-FED-CPJDR-2021",
        "law_title": "The Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021",
        "short_title": "Commission Jurisdiction Rules, 2021",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 4",
        "section_or_rule_title": "Jurisdiction of State Commission",
        "chapter_or_part": "Rules",
        "exact_text": (
            "Subject to the other provisions of the Act, the State Commission shall have jurisdiction to entertain complaints "
            "where the value of the goods or services paid as consideration exceeds fifty lakh rupees but does not exceed two crore rupees."
        ),
        "effective_date": "2021-12-30",
        "enactment_date": "2021-12-30",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enforced vide G.S.R. 912(E) on 30 December 2021. Operates under Section 47(1)(a)(i) proviso of CPA 2019. "
            "Replaced the statutory band of ₹1 Crore to ₹10 Crores with ₹50 Lakhs to ₹2 Crores."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["State Commission", "pecuniary jurisdiction", "exceeds fifty lakh rupees", "up to two crore rupees"],
        "cross_references": ["IND-FED-CPA-2019-SEC-047", "Rule 3", "Rule 5"]
    },
    {
        "id": "IND-FED-CPJDR-2021-RULE-005",
        "parent_doc_id": "IND-FED-CPJDR-2021",
        "law_title": "The Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules, 2021",
        "short_title": "Commission Jurisdiction Rules, 2021",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 5",
        "section_or_rule_title": "Jurisdiction of National Commission",
        "chapter_or_part": "Rules",
        "exact_text": (
            "Subject to the other provisions of the Act, the National Commission shall have jurisdiction to entertain complaints "
            "where the value of the goods or services paid as consideration exceeds two crore rupees."
        ),
        "effective_date": "2021-12-30",
        "enactment_date": "2021-12-30",
        "legal_status": "In Force",
        "legal_status_notes": (
            "Enforced vide G.S.R. 912(E) on 30 December 2021. Operates under Section 58(1)(a)(i) proviso of CPA 2019. "
            "Replaced the statutory threshold of 'exceeds ten crore rupees' with 'exceeds two crore rupees'."
        ),
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["National Commission", "pecuniary jurisdiction", "exceeds two crore rupees"],
        "cross_references": ["IND-FED-CPA-2019-SEC-058", "Rule 3", "Rule 4"]
    },

    # -----------------------------------------------------------------------------------------------------------------
    # Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020 (Fee Structure)
    # -----------------------------------------------------------------------------------------------------------------
    {
        "id": "IND-FED-CPCDRC-2020-RULE-007",
        "parent_doc_id": "IND-FED-CPCDRC-2020",
        "law_title": "The Consumer Protection (Consumer Disputes Redressal Commissions) Rules, 2020",
        "short_title": "Consumer Disputes Redressal Commissions Rules, 2020",
        "act_or_rule_type": "Central Rule",
        "jurisdiction": "Central (Union of India)",
        "section_or_rule_number": "Rule 7",
        "section_or_rule_title": "Fee for making complaints",
        "chapter_or_part": "Rules",
        "exact_text": (
            "(1) Every complaint filed under sub-section (1) of section 35 or sub-clause (i) of clause (a) of sub-section (1) of section 47 or sub-clause (i) of clause (a) of sub-section (1) of section 58 shall be accompanied by a fee as specified in the Table below, in the form of crossed Demand Draft drawn on a nationalised bank or through electronic mode on the portal:\n"
            "TABLE OF FEES (Rule 7):\n"
            "District Commission:\n"
            "1. Value of goods/services paid up to ₹5,00,000 (Five Lakh): Nil (No fee)\n"
            "2. Value exceeding ₹5,00,000 up to ₹10,00,000: ₹200\n"
            "3. Value exceeding ₹10,00,000 up to ₹20,00,000: ₹400\n"
            "4. Value exceeding ₹20,00,000 up to ₹50,00,000: ₹1,000\n"
            "State Commission:\n"
            "5. Value exceeding ₹50,00,000 up to ₹1,00,00,000: ₹2,000\n"
            "6. Value exceeding ₹1,00,00,000 up to ₹2,00,00,000: ₹2,500\n"
            "National Commission:\n"
            "7. Value exceeding ₹2,00,00,000 up to ₹10,00,00,000: ₹5,000\n"
            "8. Value exceeding ₹10,00,00,000: ₹7,500\n"
            "(2) The fees specified in sub-rule (1) shall be deposited in the Consumer Welfare Fund or in the name of the Registrar of the concerned Commission."
        ),
        "effective_date": "2020-07-20",
        "enactment_date": "2020-07-15",
        "legal_status": "In Force",
        "legal_status_notes": "Notified vide G.S.R. 449(E) dated 15 July 2020 w.e.f. 20 July 2020. Free filing for claims up to ₹5 Lakhs.",
        "version_as_of_date": "2026-11-09",
        "official_source_url": "https://consumeraffairs.gov.in/acts-and-rules/consumer-protection",
        "retrieval_date": "2026-11-09",
        "scope_category": "Consumer Protection",
        "key_topics": ["filing fee", "demand draft", "electronic fee", "zero fee up to five lakhs", "fee slab"],
        "cross_references": ["IND-FED-CPA-2019-SEC-035"]
    }
]

for _p in PROVISIONS:
    _p.setdefault("effective_from", _p.get("effective_date"))
    _p.setdefault("repealed_on", None)

