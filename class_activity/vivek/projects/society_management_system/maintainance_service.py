from society import Society
from flat import MaintainanceBill
from abc import ABC, abstractmethod

# monthly maintance bills

def generate_monthly_bills(society: Society, month: str, rate: float = 1):
    for each_flat in society.get_all_flats():
        each_flat.bills[month] = MaintainanceBill(month, each_flat.size * rate)

def pay(bill: MaintainanceBill, amount:float):
    bill.pay(amount)


class Worker(ABC):
    def __init__(self, name:str):
        self.name = name

    @abstractmethod
    def resolve(self, description: str):
        pass

class Plumber(Worker):
    def resolve(self, description:str):
        return f"{self.name} (plumber) fixed: {description}"

class Electritian(Worker):
    def resolve(self, description:str):
        return f"{self.name} (electrician) fixed: {description}"


class MaintenanceRequest:
    def __int__(self, flat_no: str, description: str):
        self.flat_no = flat_no
        self.description = description
        self.status = "OPEN"
        self.resolution_note = None


def raise_request(society: Society, flat_no: str, description: str):
    request = MaintenanceRequest(flat_no, description)
    society.requests.append(request)
    return request

def resolve_request(request: MaintenanceRequest, worker: Worker):
    request.resolution_note = worker.resolve(request.description)
    request.status = "RESOLVED"