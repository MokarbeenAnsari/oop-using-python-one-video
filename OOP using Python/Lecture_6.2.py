# Has-A Model
class Country:
    def __init__(self, name="", population=""):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Country name: ", self.name)
        print("Population: ", self.population)


class Person:
    def __init__(self, name="", country=""):
        self.name = name
        self.country = country

    def printDetails(self):
        print("Person name: ", self.name)
        self.country.printDetails()


c = Country("India", "100 Cr")
c.printDetails()

p = Person("Mokarbeen Ansari", c)
p.printDetails()

del p
c.printDetails()