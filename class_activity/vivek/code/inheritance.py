class Person:                    # PARENT class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# suraj = Person("Suraj", 20)
# suraj.display_info()

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_course(self):
        print(f"student choose: {self.course}")


vaibhav = Student("Vaibhav", 21, "Python fullstack")
vaibhav.display_info()
vaibhav.display_course()

# class Trainer(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)

