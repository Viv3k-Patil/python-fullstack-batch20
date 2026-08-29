
class Flat:
    # data
    # flatno, size, residents[], vehicles, has_parking
    # bills
    def __init__(self, flat_no, size):
        self.flat_no = flat_no
        self.size = size
        self.residents = []
        self.vehicles = []
        self.has_parking = False
        self.bill = []
        

    # behaviors
    # add residents, add vehicles