# employee dev tester manager
# warrier archer wizard 


class Animal:
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):              # OVERRIDING the parent's method
        print("Woof! 🐕")

class Cat(Animal):
    def make_sound(self):              # OVERRIDING the parent's method
        print("Meow! 🐈")
        super().make_sound()

Cat().make_sound()





# class Employee:
#     def __init__(self):
#         print("Employee constructor called")


# class Tester(Employee):
#     def __init__(self):
#         print("Tester constructor called")
#         super().__init__()


# class Developer(Employee):
#     def __init__(self):
#             print("Developer constructor called")
#             super().__init__()

# class Manager(Employee):
#     def __init__(self):
#             print("Manager constructor called")
#             super().__init__()

# Manager()
# Tester()
# Developer()






# class A:
#     def show(self):
#         print("A's show method")


# class B(A):
#     pass

# class C(A):
#     pass
#     # def show(self):
#     #     print("C's show method")

# class D(B, C):  
#     pass   # D inherits from BOTH B and C
#     # def show(self):
#     #     print("D's show method")

# d = D()
# d.show()             # Which show() runs? Let's check the MRO!

# print(D.mro())       # shows the exact order Python searches in