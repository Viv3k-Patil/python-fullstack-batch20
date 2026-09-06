class NotSufficientBalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __repr__(self):
        return f"""
            balance: ${self.balance}
        """

    def withdraw(self, amount):
        if self.balance < amount:
            raise NotSufficientBalanceException()
            
        self.balance -= amount
        print(f"amount {amount} has been deducted from your acount. Balance {self.balance}")


vaibhav = BankAccount(5000)

try:
    print(vaibhav)
    vaibhav.withdraw(200)
    print(vaibhav)
    vaibhav.withdraw(10000)
    print(vaibhav)
except NotSufficientBalanceException as e:
    print(e)
    print("Try UPI or you can proceed with negative balance")