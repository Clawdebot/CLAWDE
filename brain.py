import random

def think():
    print("Brain is thinking...")

    decision = random.choice(["post", "reply", "rest"])

    print(f"Decision: {decision}")
    return decision
  
