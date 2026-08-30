from society import Society
from datetime import date

# add amenity
def add_amenity(society: Society, name: str):
    """
    this adds a new amenity in your society
    """
    society.amenities[name] = []

# book amenity
def book_amenity(society: Society, name: str, day: date, allow_multiple: bool = True):
    """
    books amenity
    allow_multiple = True -- gym
    allow_multiple = False -- clubhouse/townhall
    """
    bookings = society.amenities[name]
    if not allow_multiple and day in bookings:
        return False
    bookings.append(day)
    return True

