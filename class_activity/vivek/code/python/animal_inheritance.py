
class Human:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def display(self):
        print(f"I'm Human {self.height} {self.weight}")

    def evolution(self):
        print("Im chimpanzee!!")

class Male(Human):
    def __init__(self, height, weight, name):
        super().__init__(height, weight)
        self.gender = "male"
        self.name = name

Male("6'", "85kg", "name")

        