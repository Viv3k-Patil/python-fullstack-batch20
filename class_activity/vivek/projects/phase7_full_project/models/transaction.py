from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    account_number: str
    action: str          # "DEPOSIT", "WITHDRAW", "TRANSFER_OUT", "TRANSFER_IN"
    amount: float
    timestamp: str = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.timestamp} | Account: {self.account_number} | {self.action}: ₹{self.amount}"
