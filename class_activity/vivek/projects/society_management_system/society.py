from building import Building


class Society:

    # data
    # name, buildings, parking_spots,
    # amenities, requests
    def __init__(self, name):
        self.name = name
        self.buildings = {}
        self.total_parking_spots = 100
        self.occupied_parking_spots = 0
        self.amenities = {}
        self.requests = []

    # behaviors
    # add_building, get_all_flats
    def add_building(self, building):
        self.buildings[building.name] = building
        print("New building has been added")

    def get_building(self, building_name):
        return self.buildings[building_name]

    def get_all_flats(self):
        all_flats = []
        for each_building in self.buildings.values():
            for each_flat in each_building.flats.value():
                all_flats.append(each_flat)


