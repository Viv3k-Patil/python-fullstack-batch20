from flat import Flat

class Building:

    # data name, flats
    def __init__(self, name):
        self.name = name
        self.flats = {}

    # add_flat, get_flat
    def add_flat(self, flat):
        self.flats[flat.flat_no] = flat

    # get_flat
    def get_flat(self, flat_no):
        return self.flats[flat_no]