accounts = {}

def create_account():
    name = input("What's your name? ")
    if name in accounts:
        print("Oops! You already have an account.")
    else:
        accounts[name] = 0
        print(f"Yay! Account created. Your balance is {accounts[name]}.")

def deposit():
    name = input("Enter your account name: ")
    if name in accounts:
        amount = float(input("How much do you want to deposit? "))
        accounts[name] += amount
        print(f"Deposited! Your new balance is {accounts[name]}.")
    else:
        print("Hmm, account not found!")

def withdraw():
    name = input("Enter your account name: ")
    if name in accounts:
        amount = float(input("How much do you want to withdraw? "))
        if amount <= accounts[name]:
            accounts[name] -= amount
            print(f"Withdrawn! Your new balance is {accounts[name]}.")
        else:
            print("Not enough money!")
    else:
        print("Hmm, account not found!")

def check_balance():
    name = input("Enter your account name: ")
    if name in accounts:
        print(f"Your balance is {accounts[name]}.")
    else:
        print("Hmm, account not found!")

while True:
    print("\n=== My Simple Bank ===")
    print("1. Make new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Exit")
    choice = input("Pick a number: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        print("Thanks for using my bank! Bye!")
        break
    else:
        print("Oops, try again!")