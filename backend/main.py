from agents.orchestrator import run_orchestrator

print("===================================")
print("          AIS")
print("Business Intelligence Assistant")
print("===================================")

business_context = run_orchestrator()

print()
print("Returned Context")
print(business_context)