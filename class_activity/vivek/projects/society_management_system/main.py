from society import Society
from building import Building
from flat import Flat
from resident import Resident
from vehicle import Vehicle, VehicleType

my_society = Society("Green Valley")

my_society.add_building(Building("tower-a"))
my_society.add_building(Building("tower-b"))

flat101 = Flat("101", "900sqft")
flat101.add_resident(Resident("Mr. Parikshiti","1234567890"))
flat101.add_vehicle(Vehicle("26BH1234E", VehicleType.FOUR_WHEELER))


flat102 = Flat("102", "900sqft")
my_society.get_building("tower-a").add_flat(flat101)
my_society.get_building("tower-a").add_flat(flat102)

my_society.get_building("tower-b").add_flat(flat101)
my_society.get_building("tower-b").add_flat(flat102)

print()