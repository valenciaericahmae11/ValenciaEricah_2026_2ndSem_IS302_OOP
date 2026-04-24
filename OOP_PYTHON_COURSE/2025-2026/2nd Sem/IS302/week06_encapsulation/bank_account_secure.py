class BankAccount_EIV:
    def __init__(self_EIV, balance_EIV):
        self_EIV.__balance_EIV = balance_EIV

    def deposit_EIV(self_EIV, amount_EIV):
        self_EIV.__balance_EIV += amount_EIV

    def withdraw_EIV(self_EIV, amount_EIV):
        if amount_EIV <= self_EIV.__balance_EIV:
            self_EIV.__balance_EIV -= amount_EIV
        else:
            print("Insufficient funds")

    def get_balance_EIV(self_EIV):
        return self_EIV.__balance_EIV

account_EIV = BankAccount_EIV(5000)
account_EIV.deposit_EIV(1000)
account_EIV.withdraw_EIV(2000)
print("Balance:", account_EIV.get_balance_EIV())
