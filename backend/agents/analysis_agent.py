def run_analysis(business_context):

    print()
    print("========== ANALYSIS AGENT ==========")
    print("Analysing business context...")

    challenge = business_context["challenge"].lower()

    # ==================================
    # Default values
    # ==================================
    business_context["problem_category"] = "General Business"
    business_context["root_problem"] = "Unknown"
    business_context["confidence"] = 30
    business_context["analysis_status"] = "Incomplete"
    business_context["missing_information"] = []
    business_context["required_information"] = []
    business_context["recommended_specialist"] = "General Business Agent"

    # ==================================
    # SALES / MARKETING
    # ==================================
    if "sales" in challenge or "sale" in challenge or "tiktok" in challenge:

        business_context["problem_category"] = "Marketing"
        business_context["root_problem"] = "Sales performance issue"
        business_context["confidence"] = 55
        business_context["recommended_specialist"] = "Marketing Strategy Agent"

        business_context["missing_information"] = [
            "Monthly sales",
            "TikTok views",
            "Conversion rate"
        ]

        business_context["required_information"] = [
            "Traffic source",
            "Customer behaviour",
            "Marketing strategy"
        ]

    # ==================================
    # HUMAN RESOURCES
    # ==================================
    elif "employee" in challenge or "staff" in challenge:

        business_context["problem_category"] = "Human Resources"
        business_context["root_problem"] = "Employee retention issue"
        business_context["confidence"] = 80
        business_context["recommended_specialist"] = "HR Strategy Agent"

    # ==================================
    # FINANCE
    # ==================================
    elif "cash" in challenge or "finance" in challenge:

        business_context["problem_category"] = "Finance"
        business_context["root_problem"] = "Cash flow management issue"
        business_context["confidence"] = 85
        business_context["recommended_specialist"] = "Finance Strategy Agent"

    # ==================================
    # CUSTOMER EXPERIENCE
    # ==================================
    elif "customer" in challenge:

        business_context["problem_category"] = "Customer Experience"
        business_context["root_problem"] = "Customer satisfaction issue"
        business_context["confidence"] = 80
        business_context["recommended_specialist"] = "Customer Success Agent"

    # ==================================
    # FINAL DECISION
    # ==================================
    if business_context["confidence"] >= 70:
        business_context["analysis_status"] = "Ready"
    else:
        business_context["analysis_status"] = "Incomplete"

    # ==================================
    # SOURCE ATTRIBUTION
    # ==================================
    business_context["last_updated_by"] = "Analysis Agent"

    print("Analysis complete.")

    return business_context