# Abstract Base Class
# Parent class: Shape
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

# Child 1: Rectangle
class Rectangle(Shape):
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

# Child 2: Circle
class Circle(Shape):
    def __init__(self, r=0):
        self.r = r

    def getArea(self):
        return 3.14 * self.r**2

obj1 = Rectangle(10, 20)
obj2 = Circle(10)

print("Area of object 1: ", obj1.getArea())
print("Area of object 2: ", obj2.getArea())