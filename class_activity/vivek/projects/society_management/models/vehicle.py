from dataclasses import dataclass
from enum import Enum, auto


class VehicleType(Enum):
    TWO_WHEELER = auto()
    FOUR_WHEELER = auto()


@dataclass
class Vehicle:
    number_plate: str
    vehicle_type: VehicleType
