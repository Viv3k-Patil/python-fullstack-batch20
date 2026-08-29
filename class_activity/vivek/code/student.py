class Student:

    department_name = "Some department"

    # constructor
    def __init__(self, name, age, course):    # constructor — runs automatically when object is created
        self.name = name
        self.age = age
        self.course = course

    # actions
    def display(self):
        print(f"""
            name: {self.name}
            age: {self.age}
            course: {self.course}
            """)

    def call_action(self):
        print("they called me")


s1 = Student("Priya", 20, "Python Full Stack")
s1.display()
s1.call_action()

s2 = Student("Rahul", 22, "Data Science")
s2.display()
s2.call_action()













# Creating objects (instances) of the Student class
# s1 = Student("Priya", 20, "Python Full Stack")
# s2 = Student("Rahul", 22, "Data Science")

# print(f"""
#     name: {s1.name}
#     age: {s1.age}
#     course: {s1.course}
# """)


# print(f"""
#     name: {s2.name}
#     age: {s2.age}
#     course: {s2.course}
# """)