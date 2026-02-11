messages = ["Hi", "Welcome to the platform", "OK"]

for message in messages:
    length = len(message)
    print(f"Message: '{message}'")
    print(f"Length: {length}")
    
    if length > 10:
        print("Status: ⚠ Longer than 10 characters")
    else:
        print("Status: ✅ Within limit")
    
    print("-" * 30)
