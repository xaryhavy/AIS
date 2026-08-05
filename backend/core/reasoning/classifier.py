"""
AIS Reasoning Engine
Classifier Module

Responsibility:
- Read Business Context
- Classify the business problem
- Identify the root problem
- Record matched reasoning patterns

The classifier DOES NOT:
- Update Business Context
- Calculate confidence
- Recommend actions
- Store memory
"""


def classify_problem(business_context):
    """
    Reads the business context and returns a classification result.
    """

    challenge = business_context.get("challenge", "").lower()

    result = {
        "problem_category": "General Business",
        "root_problem": "Unknown",
        "matched_patterns": []
    }

    # -------------------------
    # Sales & Marketing
    # -------------------------

    marketing_keywords = [
        "sales",
        "sale",
        "marketing",
        "facebook",
        "instagram",
        "tiktok",
        "ads",
        "advert",
        "customers",
        "conversion"
    ]

    for keyword in marketing_keywords:
        if keyword in challenge:
            result["matched_patterns"].append(keyword)

    if result["matched_patterns"]:

        result["problem_category"] = "Marketing"

        result["root_problem"] = "Sales performance issue"

        return result

    # -------------------------
    # Human Resources
    # -------------------------

    hr_keywords = [
        "employee",
        "employees",
        "staff",
        "worker",
        "workers",
        "resign",
        "retention",
        "hiring"
    ]

    for keyword in hr_keywords:
        if keyword in challenge:
            result["matched_patterns"].append(keyword)

    if result["matched_patterns"]:

        result["problem_category"] = "Human Resources"

        result["root_problem"] = "Employee retention issue"

        return result

    # -------------------------
    # Finance
    # -------------------------

    finance_keywords = [
        "cash",
        "finance",
        "money",
        "profit",
        "revenue",
        "expenses",
        "debt",
        "income"
    ]

    for keyword in finance_keywords:
        if keyword in challenge:
            result["matched_patterns"].append(keyword)

    if result["matched_patterns"]:

        result["problem_category"] = "Finance"

        result["root_problem"] = "Cash Flow Management Issue"

        return result

    # -------------------------
    # Customer Experience
    # -------------------------

    customer_keywords = [
        "customer",
        "complaint",
        "review",
        "refund",
        "experience",
        "support"
    ]

    for keyword in customer_keywords:
        if keyword in challenge:
            result["matched_patterns"].append(keyword)

    if result["matched_patterns"]:

        result["problem_category"] = "Customer Experience"

        result["root_problem"] = "Customer Satisfaction Issue"

        return result

    return result