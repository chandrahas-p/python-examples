class ATM:
    def __init__(self, user_pin, balance=0):
        self.__pin = user_pin
        self.__balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.__pin

    def check_balance(self):
        print(f"Your current balance is: ₹{self.__balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount:.2f} successfully.")
            self.check_balance()
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount:.2f} successfully.")
            self.check_balance()


def run_atm():
    atm = ATM(user_pin="1234", balance=1000)

    print("Welcome to the ATM!")
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if atm.verify_pin(pin):
            while True:
                print("\nOptions:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
                choice = input("Select an option (1-4): ")

                if choice == '1':
                    atm.check_balance()
                elif choice == '2':
                    amount = float(input("Enter amount to deposit: ₹"))
                    atm.deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: ₹"))
                    atm.withdraw(amount)
                elif choice == '4':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid option. Please choose 1-4.")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempts left.")
    else:
        print("Too many incorrect attempts. Access denied.")


run_atm()
