LAW_DATABASE = {
    "landlord_deposit": {
        "keywords": ["deposit", "landlord", "rent", "tenant", "eviction", "security deposit"],
        "title": "Landlord / Tenant Dispute",
        "laws": [
            "Transfer of Property Act, 1882 - Sections 105-108",
            "Rent Control Act (State-specific, e.g., Delhi Rent Control Act, 1958)",
            "Model Tenancy Act, 2021"
        ],
        "rights": [
            "Right to receive security deposit back within reasonable time after vacating",
            "Right to proper notice before eviction (usually 1-3 months)",
            "Right to essential services (water, electricity) cannot be cut off illegally",
            "Right to peaceful enjoyment of the rented premises"
        ],
        "remedies": [
            "Send a legal notice to the landlord",
            "File complaint with Rent Controller / Rent Authority",
            "Approach Consumer Forum if a rental agency is involved",
            "File a civil suit for recovery of deposit"
        ],
        "forum": "Rent Controller / Civil Court"
    },
    "consumer_complaint": {
        "keywords": ["product", "defective", "refund", "consumer", "shop", "online order", "cheated"],
        "title": "Consumer Complaint",
        "laws": [
            "Consumer Protection Act, 2019",
            "Consumer Protection (E-Commerce) Rules, 2020",
            "Indian Contract Act, 1872"
        ],
        "rights": [
            "Right to safety, information, choice, and redressal",
            "Right to refund/replacement for defective goods",
            "Right to compensation for unfair trade practices",
            "Right to file complaint within 2 years of cause of action"
        ],
        "remedies": [
            "File complaint with District Consumer Disputes Redressal Commission",
            "Approach National Consumer Helpline (1915)",
            "File online at e-daakhil.nic.in",
            "Send legal notice to seller/manufacturer"
        ],
        "forum": "District Consumer Commission"
    },
    "wages_unpaid": {
        "keywords": ["salary", "wages", "employer", "not paid", "unpaid", "work", "boss"],
        "title": "Unpaid Wages / Salary",
        "laws": [
            "Payment of Wages Act, 1936",
            "Minimum Wages Act, 1948",
            "Code on Wages, 2019",
            "Industrial Disputes Act, 1947"
        ],
        "rights": [
            "Right to receive wages within prescribed time (7th or 10th of month)",
            "Right to minimum wages as notified by government",
            "Right to approach Labour Commissioner for unpaid wages",
            "Right against wrongful deduction from wages"
        ],
        "remedies": [
            "File complaint with Labour Commissioner",
            "Send legal notice to employer",
            "File case in Labour Court",
            "Approach Shram Suvidha Portal (shramsuvidha.gov.in)"
        ],
        "forum": "Labour Commissioner / Labour Court"
    },
    "domestic_violence": {
        "keywords": ["domestic", "violence", "husband", "wife", "abuse", "dowry", "family"],
        "title": "Domestic Violence",
        "laws": [
            "Protection of Women from Domestic Violence Act, 2005",
            "Section 498A Indian Penal Code",
            "Dowry Prohibition Act, 1961"
        ],
        "rights": [
            "Right to protection order, residence order, monetary relief",
            "Right to free legal aid under Legal Services Authorities Act, 1987",
            "Right to file complaint at any police station (Zero FIR)",
            "Right to shelter home and medical assistance"
        ],
        "remedies": [
            "Call Women Helpline: 181 or Police: 112",
            "File complaint before Magistrate under DV Act",
            "Approach Protection Officer in your district",
            "Contact District Legal Services Authority (DLSA) for free lawyer"
        ],
        "forum": "Magistrate Court / Protection Officer"
    },
    "rti": {
        "keywords": ["rti", "information", "government", "department", "public authority"],
        "title": "Right to Information",
        "laws": ["Right to Information Act, 2005"],
        "rights": [
            "Right to seek information from any public authority",
            "Right to receive response within 30 days",
            "Right to appeal if information denied"
        ],
        "remedies": [
            "File RTI application with Rs. 10 fee",
            "File First Appeal with Appellate Authority",
            "File Second Appeal with Information Commission",
            "File online at rtionline.gov.in"
        ],
        "forum": "State / Central Information Commission"
    },
    "police_complaint": {
        "keywords": ["police", "fir", "complaint", "not registering", "station"],
        "title": "Police Complaint / FIR",
        "laws": [
            "Section 154 CrPC (now Section 173 BNSS)",
            "Section 156(3) CrPC (Magistrate direction to police)",
            "Lalita Kumari v. State of UP (2013) - Mandatory FIR"
        ],
        "rights": [
            "Right to have FIR registered for cognizable offence",
            "Right to Zero FIR at any police station",
            "Right to free copy of FIR",
            "Right to approach Superintendent of Police if station refuses"
        ],
        "remedies": [
            "Written complaint to SHO",
            "Complaint to Superintendent of Police",
            "Application under Section 156(3) to Magistrate",
            "Online complaint at state police portal"
        ],
        "forum": "Police Station / Magistrate"
    },
    "cyber_crime": {
        "keywords": ["cyber", "online fraud", "hacking", "otp", "upi", "phishing", "scam"],
        "title": "Cyber Crime / Online Fraud",
        "laws": [
            "Information Technology Act, 2000",
            "Section 66C, 66D IT Act (Identity theft, cheating)",
            "Bharatiya Nyaya Sanhita, 2023"
        ],
        "rights": [
            "Right to report cyber crime online",
            "Right to get money back if reported within 24 hours (golden hour)",
            "Right to free legal aid"
        ],
        "remedies": [
            "Report immediately at cybercrime.gov.in",
            "Call Cyber Crime Helpline: 1930",
            "File FIR at local cyber cell",
            "Inform your bank to freeze transaction"
        ],
        "forum": "Cyber Crime Cell"
    }
}

LEGAL_AID_CLINICS = [
    {"state": "Delhi", "name": "Delhi State Legal Services Authority", "phone": "011-23388040", "address": "Patiala House Courts, New Delhi"},
    {"state": "Maharashtra", "name": "Maharashtra State Legal Services Authority", "phone": "022-22620222", "address": "Mumbai High Court, Mumbai"},
    {"state": "Karnataka", "name": "Karnataka State Legal Services Authority", "phone": "080-22112521", "address": "High Court Building, Bengaluru"},
    {"state": "Tamil Nadu", "name": "Tamil Nadu State Legal Services Authority", "phone": "044-25340654", "address": "High Court Campus, Chennai"},
    {"state": "West Bengal", "name": "West Bengal State Legal Services Authority", "phone": "033-22486250", "address": "Calcutta High Court, Kolkata"},
    {"state": "Uttar Pradesh", "name": "UP State Legal Services Authority", "phone": "0522-2627570", "address": "High Court, Allahabad"},
    {"state": "Kerala", "name": "Kerala State Legal Services Authority", "phone": "0471-2563522", "address": "High Court, Ernakulam"},
    {"state": "Gujarat", "name": "Gujarat State Legal Services Authority", "phone": "079-26576262", "address": "High Court, Ahmedabad"},
    {"state": "Rajasthan", "name": "Rajasthan State Legal Services Authority", "phone": "0141-2227484", "address": "High Court, Jodhpur"},
    {"state": "Punjab", "name": "Punjab State Legal Services Authority", "phone": "0172-2746061", "address": "High Court, Chandigarh"},
]

NATIONAL_HELPLINES = [
    {"name": "National Legal Aid Helpline", "number": "15100"},
    {"name": "Women Helpline", "number": "181"},
    {"name": "Police Emergency", "number": "112"},
    {"name": "Cyber Crime Helpline", "number": "1930"},
    {"name": "Consumer Helpline", "number": "1915"},
    {"name": "Child Helpline", "number": "1098"},
]

def match_problem(user_text: str):
    text = user_text.lower()
    scores = {}
    for key, data in LAW_DATABASE.items():
        score = sum(1 for kw in data["keywords"] if kw in text)
        if score > 0:
            scores[key] = score
    if not scores:
        return None
    best = max(scores, key=scores.get)
    return {**LAW_DATABASE[best], "category": best}