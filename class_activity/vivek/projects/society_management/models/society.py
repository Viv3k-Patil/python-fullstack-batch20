from datetime import date

from models.building import Building


class Society:
    """
    Note: Society is kept as a plain data container here — it holds state
    (buildings, parking counts, amenities, requests), but the *behavior*
    for parking/maintenance/amenities now lives in the services/ layer
    instead of as methods on this class. This is a common real-world split:
    models = state, services = operations on that state.
    """

    def __init__(self, name: str, total_parking_spots: int):
        self.name = name
        self.buildings: dict[str, Building] = {}
        self.total_parking_spots = total_parking_spots
        self.occupied_parking_spots = 0
        # name -> {"allow_multiple": bool, "bookings": [dates]}
        self.amenities: dict[str, dict] = {}
        self.requests: list = []

    def add_building(self, building: Building):
        self.buildings[building.name] = building

    def all_flats(self):
        for building in self.buildings.values():
            yield from building.flats.values()

    def __repr__(self):
        return f"Society({self.name})"
