from society import Society
from flat import Flat

def assign_parking(society: Society, flat: Flat):
    """
    return bool if parking successfully assigned.
    """
    if society.occupied_parking_spots >= society.total_parking_spots:
        return False

    if flat.has_parking == True:
        return False

    flat.has_parking = True
    society.occupied_parking_spots += 1
    return True 

def release_parking(society: Society, flat: Flat):
    if flat.has_parking:
        flat.has_parking = False
        society.occupied_parking_spots -= 1

def available_spots(society: Society):
    return society.total_parking_spots - society.occupied_parking_spots