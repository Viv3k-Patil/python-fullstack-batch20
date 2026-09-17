from class_activity.vivek.projects.phase7_full_project.exceptions import InsufficientBalanceError


class Account:
    """Parent class for all account types."""

    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner  # Account HAS-A User (composition)
        self._balance = balance
        self.transactions = []  # Account HAS-A list of Transactions

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientBalanceError("Insufficient balance")
        self._balance -= amount

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "owner_phone": self.owner.phone,
            "balance": self._balance,
            "type": type(self).__name__,
        }


class SavingsAccount(Account):
    """SavingsAccount IS-A Account, earns interest, no overdraft."""

    def __init__(self, account_number, owner, balance=0.0, interest_rate=0.04):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate


class CurrentAccount(Account):
    """CurrentAccount IS-A Account, allows overdraft, no interest."""

    def __init__(self, account_number, owner, balance=0.0, overdraft_limit=5000):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):  # overrides parent - different rule!
        if amount > self._balance + self.overdraft_limit:
            raise InsufficientBalanceError("Exceeds overdraft limit")
        self._balance -= amount
