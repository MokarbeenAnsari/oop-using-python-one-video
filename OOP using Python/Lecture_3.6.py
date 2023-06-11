# Practice Problem - 4 : Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculateArea(self):
        return self.__length * self.__width
    
    def calculatePerimeter(self):
        return 2 * ( self.__length + self.__width)


r1 = Rectangle(12, 2)
print("Area: ", r1.calculateArea())
print("Perimeter: ", r1.calculatePerimeter())