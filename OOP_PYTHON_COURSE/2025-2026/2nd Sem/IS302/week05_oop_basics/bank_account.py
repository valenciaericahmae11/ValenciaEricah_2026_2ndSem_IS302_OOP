class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name_EIV = account_name
        self.balance_EIV = balance

    def deposit(self, amount):
        self.balance_EIV += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance_EIV:
            self.balance_EIV -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Balance:", self.balance_EIV)


account = BankAccount("Juan", 5000)
account.deposit(1000)
account.withdraw(2000)
account.display_balance()

