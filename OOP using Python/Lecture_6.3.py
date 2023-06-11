# Part-of Model
# Owned Class
class Engine:
    def __init__(self, capacity=0):
        self.capacity = capacity

    def printDetails(self):
        print("Engine Capacity: ", self.capacity)

class Door:
    def __init__(self, doors=0):
        self.doors = doors

    def printDetails(self):
        print("Number of door in car: ", self.doors)

class Tire:
    def __init__(self, tires=0):
        self.tires = tires

    def printDetails(self):
        print("Number of tires in car:", self.tires)

# Owner Class
class Car:
    def __init__(self, color='', capacity=0, doors=0, tires=0):
        self.color = color
        self.capacity = Engine(capacity)
        self.doors = Door(doors)
        self.tires = Tire(tires)

    def printDetails(self):
        print("Color of car: ", self.color)
        self.capacity.printDetails()
        self.doors.printDetails()
        self.tires.printDetails()


car = Car("Red", 1000, 4, 4)
car.printDetails()

del car
