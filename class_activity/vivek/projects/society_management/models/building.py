from models.flat import Flat


class Building:
    def __init__(self, name: str):
        self.name = name
        self.flats: dict[str, Flat] = {}

    def add_flat(self, flat: Flat):
        self.flats[flat.flat_no] = flat

    def get_flat(self, flat_no: str) -> Flat:
        return self.flats[flat_no]

    def __repr__(self):
        return f"Building({self.name})"
