class Account:
    def __init__(self, account_number, name, balance:float):
        self.account_number = account_number
        self.name = name
        self.balance=balance

    def __repr__(self):
        return f"""
            account number: {self.account_number}
            name: {self.name}
            balance: {self.balance}
        """

    def deposit(self, amount):
        self.balance += amount
        print(
            f"Deposited {amount}. "
            f"New balance: {self.balance}"
        )

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False

        self.balance -= amount
        print(
            f"Withdrew {amount}. "
            f"New balance: {self.balance}"
        )
        return True

    def show_balance(self):
        print(
            f"{self.name}'s balance: "
            f"{self.balance}"
        )

suraj_acc = Account("123456789", "suraj", 1500)

suraj_acc.show_balance()
suraj_acc.deposit(15000)
suraj_acc.withdraw(50000)
print(suraj_acc)
