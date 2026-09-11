

from abc import abstractmethod, ABC

class Shape(ABC):

    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass

class Rectangle(Shape):
    def area(self):
        print("ares of rectangle")

    def perimeter(self):
        print("perimiter of rectangle")

class Circle(Shape):
    pass

Rectangle().area()