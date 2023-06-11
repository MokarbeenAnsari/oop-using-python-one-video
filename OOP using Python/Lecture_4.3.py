# Inheritance
# Parent Class
class Vehicle:
    fuelCap = 10

    def __init__(self, brand, model, color) -> None:
        self.brand = brand
        self.model = model
        self.color = color

    def printDetail(self):
        print("Manufacturer: ", self.brand)
        print("Model: ", self.model)
        print("Color: ", self.color)

    def printFuelCap(self):
        print("Fuel Cap of Vehicle: ", self.fuelCap)

#Child Class
class Car(Vehicle):
    fuelCap = 5

    def __init__(self, brand, model, color, doors) -> None:
        super().__init__(brand, model, color)
        self.doors = doors

    def printCarDetails(self):
        self.printDetail()
        print("Number of doors: ", self.doors)

    def printFuelCap(self):
       print("Fuel Cap of Vehicle: ", super().fuelCap)
       print("Fuel Cap of Car: ", self.fuelCap)

vehicle1 = Vehicle("Honda", 2021, "White")
vehicle1.printDetail()
vehicle1.printFuelCap()
print()
car1 = Car("TATA", 2022, "Black", 4)
car1.printCarDetails()
car1.printFuelCap()



