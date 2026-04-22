# ================== MODELS ==================
class Account:
    def __init__(self, balance=0):
        self.balance = balance


# ================== UTILS ==================
class Statement:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, message):
        self.transactions.append(message)

    def show_statement(self):
        if not self.transactions:
            print("No transactions yet.")
        else:
            print("\nTransaction History:")
            for t in self.transactions:
                print(t)


# ================== SERVICES ==================
class ATMService:
    def __init__(self):
        self.account = Account(1000)  # Starting balance
        self.statement = Statement()

    def check_balance(self):
        print(f"Current Balance: ₹{self.account.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return
        self.account.balance += amount
        self.statement.add_transaction(f"Deposited ₹{amount}")
        print("Deposit successful.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount!")
        elif amount > self.account.balance:
            print("Insufficient balance!")
        else:
            self.account.balance -= amount
            self.statement.add_transaction(f"Withdrew ₹{amount}")
            print("Withdrawal successful.")

    def show_statement(self):
        self.statement.show_statement()


# ================== MAIN ==================
def main():
    atm = ATMService()

    while True:   # Infinite loop (required)
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(amount)
            except:
                print("Invalid input!")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(amount)
            except:
                print("Invalid input!")

        elif choice == '4':
            atm.show_statement()

        elif choice == '5':
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()