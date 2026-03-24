class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}")

    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")


# Example Usage
account1 = BankAccount("123456789", 1000)

account1.check_balance()
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()
