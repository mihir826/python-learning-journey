# The correct PIN for the account
correct_pin = "1234"

# The starting balance for the account
balance = 50000.0  

is_locked = True

for i in range(3):
    input_PIN = input("Enter the pin: ") 
    if input_PIN == correct_pin:
        print("Welcome!")
        is_locked = False
        break
    else:
        print("Wrong PIN. Try again.")

if not is_locked:
    while not is_locked:
        print("""
--- M-ATM Menu ---
1. Check Balance
2. Deposit
3. Withdraw
4. Exit""")
        choice = input("Enter your choice (1 - 4): ")
        if choice == "1":
            print(f"Your current balance is: {balance}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance = balance + amount
            print(f"Deposit successful. New balance is: {balance}")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance = balance - amount
                print(f"Withdrawal successful. New balance is: {balance}")
        elif choice == "4":
            print("Thank you for using M-ATM. Goodbye!")
            is_locked = True 
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
else:
    print("Too many failed attempts. Your card is locked.")

























