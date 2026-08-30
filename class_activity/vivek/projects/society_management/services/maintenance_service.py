"""
maintenance_service.py

Covers TWO related but distinct things, both under "maintenance":
1. Monthly maintenance BILLS (money owed by each flat)
2. Maintenance REQUESTS / complaints (plumbing, electrical issues etc.)

Worker/Plumber/Electrician live here rather than in models/ because they're
only ever used through this service — this is the one place inheritance +
polymorphism is genuinely justified (different workers resolve requests
differently, but calling code doesn't need to know which type it has).
"""

from abc import ABC, abstractmethod

from models.society import Society
from models.flat import MaintenanceBill


# ---------- Monthly maintenance bills ----------

def generate_monthly_bills(society: Society, month: str, rate_per_sqft: float = 3):
    for flat in society.all_flats():
        flat.bills[month] = MaintenanceBill(month, flat.size_sqft * rate_per_sqft)


def pay_bill(bill: MaintenanceBill, amount: float):
    bill.pay(amount)


# ---------- Maintenance requests / complaints ----------

class Worker(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def resolve(self, description: str) -> str:
        ...


class Plumber(Worker):
    def resolve(self, description: str) -> str:
        return f"{self.name} (plumber) fixed: {description}"


class Electrician(Worker):
    def resolve(self, description: str) -> str:
        return f"{self.name} (electrician) fixed: {description}"


class MaintenanceRequest:
    def __init__(self, flat_no: str, description: str):
        self.flat_no = flat_no
        self.description = description
        self.status = "OPEN"
        self.resolution_note = None


def raise_request(society: Society, flat_no: str, description: str) -> MaintenanceRequest:
    request = MaintenanceRequest(flat_no, description)
    society.requests.append(request)
    return request


def resolve_request(request: MaintenanceRequest, worker: Worker):
    request.resolution_note = worker.resolve(request.description)
    request.status = "RESOLVED"
