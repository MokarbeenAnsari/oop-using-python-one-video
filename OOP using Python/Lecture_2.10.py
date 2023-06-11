# Practice Problem - 1
class Point:
    # Initializer
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    #Method
    def squareSum(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

p1 = Point()
print("Square Sum: ", p1.squareSum())