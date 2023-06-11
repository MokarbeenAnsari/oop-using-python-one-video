# Inheritance
# Parent Class
class Vehicle:
    def __init__(self, brand, model, color) -> None:
        self.brand = brand
        self.model = model
        self.color = color

    def printDetail(self):
        print("Manufacturer: ", self.brand)
        print("Model: ", self.model)
        print("Color: ", self.color)

#Child Class
class Car(Vehicle):
    def __init__(self, brand, model, color, doors) -> None:
        Vehicle.__init__(self, brand, model, color)
        self.doors = doors

    def printCarDetails(self):
        self.printDetail()
        print("Number of doors: ", self.doors)

    
vehicle1 = Vehicle("Honda", 2021, "White")
vehicle1.printDetail()
print()
car1 = Car("TATA", 2022, "Black", 4)
car1.printCarDetails()


