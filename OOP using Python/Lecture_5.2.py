# Shape 1: Rectangle
class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width


# Shape 2: Circle
class Circle:
    def __init__(self, r=0):
        self.r = r

    def getArea(self):
        return 3.14 * self.r**2 


obj1 = Rectangle(70, 50)
print("Area of object 1: ", obj1.getArea())

obj2 = Circle(30)
print("Area of object 2: ", obj2.getArea())

