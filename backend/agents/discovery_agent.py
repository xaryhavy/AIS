def run_discovery():

    print("Discovery Agent Started")

    name = input("What is your name? ")

    business = input("What is your business name? ")

    challenge = input("What is your biggest business challenge today? ")

    return {
        "owner": name,
        "business": business,
        "challenge": challenge
    }