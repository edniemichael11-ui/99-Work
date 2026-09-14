import random
actions = 0

while True:
    print("\nAvailable actions")
    print("1. say Hello")
    print("2. Display a random number 1 to 100")
    print("3. Show how many menu actions have been completed")
    print("q. Quit")
    
    action = input("Action: ").strip().lower()
    
    if action == "1":
        print("Hello")
        actions += 1
    elif action == "2":
        num1 = random.randint(1, 100)
        print(num1)
        actions += 1
    elif action == "3":
        print(f"Actions: {actions}")
        actions += 1
    elif action == "q":
        print("Exiting menu")
        break
    else:
        print("Invalid Entry")
