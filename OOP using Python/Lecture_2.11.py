# Practice Problem: 2
class Student:
    # Initializer
    def __init__(self, name=None, phy=0, chem=0, math=0):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.math = math

    # Methods
    def totalMarks(self):
        return self.phy + self.chem + self.math

    def percentage(self):
        return self.totalMarks() / 3

s1 = Student("Mokarbeen", 40, 40, 40)
print(s1.name)
print("Total marks: ", s1.totalMarks())
print("Percentage: ", s1.percentage())