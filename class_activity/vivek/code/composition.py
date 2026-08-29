

class Car:

    def __init__(self):
        self.engine = None
        self.wheels = []

    def display_info(self):
        print(f"""
            engine: {self.engine}
            wheels: {self.wheels}
        """)

class Engine:
    pass

class Wheel:
    pass

honda = Car()

honda_engine = Engine()

honda.engine = honda_engine
honda.wheels.append(Wheel())

honda.display_info()

# shrikantnaykude3@gmail.com
