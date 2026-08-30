from datetime import date

from models.society import Society


def add_amenity(society: Society, name: str, allow_multiple: bool = True):
    """
    allow_multiple=True  -> amenity like a Gym: always bookable, no slot limit.
    allow_multiple=False -> amenity like a Clubhouse Hall: only one booking per day.
    """
    society.amenities[name] = {"allow_multiple": allow_multiple, "bookings": []}


def book_amenity(society: Society, name: str, day: date) -> bool:
    amenity = society.amenities[name]
    if not amenity["allow_multiple"] and day in amenity["bookings"]:
        return False
    amenity["bookings"].append(day)
    return True


def list_amenities(society: Society) -> list[str]:
    return list(society.amenities.keys())
