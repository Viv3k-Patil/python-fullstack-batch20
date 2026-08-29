from society import Society
from building import Building
from flat import Flat

my_society = Society("Green Valley")

my_society.add_building(Building("tower-a"))
my_society.add_building(Building("tower-b"))

flat101 = Flat("101", "900sqft")
flat102 = Flat("102", "900sqft")
my_society.get_building("tower-a").add_flat(flat101)
my_society.get_building("tower-a").add_flat(flat102)

my_society.get_building("tower-b").add_flat(flat101)
my_society.get_building("tower-b").add_flat(flat102)

print()