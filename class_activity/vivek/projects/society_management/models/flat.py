from models.resident import Resident
from models.vehicle import Vehicle


class MaintenanceBill:
    """Has real behavior (paid/unpaid tracking) -> deserves a class,
    kept alongside Flat since a bill has no meaning without one."""

    def __init__(self, month: str, amount_due: float):
        self.month = month
        self.amount_due = amount_due
        self.amount_paid = 0.0

    def pay(self, amount: float):
        self.amount_paid += amount

    @property
    def is_paid(self) -> bool:
        return self.amount_paid >= self.amount_due


class Flat:
    def __init__(self, flat_no: str, size_sqft: float):
        self.flat_no = flat_no
        self.size_sqft = size_sqft
        self.residents: list[Resident] = []
        self.vehicles: list[Vehicle] = []
        self.has_parking = False
        self.bills: dict[str, MaintenanceBill] = {}

    def add_resident(self, resident: Resident):
        self.residents.append(resident)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def __repr__(self):
        return f"Flat({self.flat_no})"
