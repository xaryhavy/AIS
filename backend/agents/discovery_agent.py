def run_discovery():

    print("Discovery Agent Started")

    name = input("What is your name? ").strip()

    business = input("What is your business name? ").strip()

    challenge = input("What is your biggest business challenge today? ").strip()
    return {
        "owner": name,
        "business": business,
        "challenge": challenge
    }