from agents.discovery_agent import run_discovery
from agents.analysis_agent import run_analysis


def run_orchestrator():

    print()
    print("========== ORCHESTRATOR ==========")
    print("Starting AIS workflow...")
    print()

    # ==============================
    # Step 1: Discovery Agent
    # ==============================
    business_context = run_discovery()

    print()
    print("Discovery completed.")

    # ==============================
    # Step 2: Orchestrator Intelligence
    # ==============================
    challenge = business_context["challenge"].lower()

    if "sales" in challenge or "sale" in challenge or "tiktok" in challenge:
        workflow = "Sales & Marketing"

    elif "employee" in challenge or "staff" in challenge:
        workflow = "Human Resources"

    elif "cash" in challenge or "finance" in challenge:
        workflow = "Finance"

    elif "customer" in challenge:
        workflow = "Customer Experience"

    else:
        workflow = "General Business"

    # Update Business Context
    business_context["workflow"] = workflow

    print(f"Selected Workflow: {workflow}")

    print()
    print("Passing Business Context to Analysis Agent...")

    # ==============================
    # Step 3: Analysis Agent
    # ==============================
    business_context = run_analysis(business_context)

    print()

    # ==============================
    # Step 4: Orchestrator Decision
    # ==============================
    if business_context["analysis_status"] == "Incomplete":

        print("Analysis confidence below benchmark.")
        print()

        print("Missing Information:")
        for item in business_context["missing_information"]:
            print("-", item)

        print()

        print("Information Required:")
        for item in business_context["required_information"]:
            print("-", item)

        print()
        print("Returning to Discovery Agent for more information...")

    else:

        print("Analysis confidence acceptable.")
        print()

        print("Routing to:")
        print(business_context["recommended_specialist"])

    print()
    print("Analysis completed.")
    print("Returning Business Context to main.py...")

    return business_context