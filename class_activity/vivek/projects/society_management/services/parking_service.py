from models.society import Society
from models.flat import Flat


def assign_parking(society: Society, flat: Flat) -> bool:
    """Returns True if a spot was available and assigned, False otherwise."""
    if society.occupied_parking_spots >= society.total_parking_spots:
        return False
    flat.has_parking = True
    society.occupied_parking_spots += 1
    return True


def release_parking(society: Society, flat: Flat):
    if flat.has_parking:
        flat.has_parking = False
        society.occupied_parking_spots -= 1


def available_spots(society: Society) -> int:
    return society.total_parking_spots - society.occupied_parking_spots
