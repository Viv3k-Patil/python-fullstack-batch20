from resident import Resident
from vehicle import Vehicle

class MaintainanceBill:

    def __init__(self, month: str, amount_due: float):
        self.month = month
        self.amount_due = amount_due
        self.amount_paid = 0.0

    def pay(self, amount: float):
        self.amount_paid += amount

    def is_paid(self)->bool:
        return self.amount_paid >= self.amount_due



class Flat:
    # data
    # flatno, size, residents[], vehicles, has_parking
    # bills
    def __init__(self, flat_no, size):
        self.flat_no: str = flat_no
        self.size: str = size
        self.residents: list = []
        self.vehicles: list = []
        self.has_parking: bool = False
        self.bills: dict[str, MaintainanceBill] = {}
        

    # behaviors
    # add residents, add vehicles
    def add_resident(self, resident: Resident):
        self.residents.append(resident)
        

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def __repr__(self):
        return f"flat({self.flat_no})"