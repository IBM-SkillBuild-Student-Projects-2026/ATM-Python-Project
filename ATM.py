balance = 1000
while True:
    print("\n---ATM MENU---")
    print("1. Check your Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        print("Your Balance is:", balance)
    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount deposited successfully")
    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount > balance:
            print("Insufficient Funds!")
        else:
            balance = balance - amount
            print("Please collect cash.")
    elif choice == 4:
        print("Thank you for using this ATM")
        break
    else:
        print("invalid choice Try again")
