# Practice Problem - 3 : Student Class
class Student:
    def __init__(self, name, rollNumber):
        self.__name = name
        self.__rollNumber = rollNumber

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber


s1 = Student("Mokarbeen", "ABC123")
print("Name: ", s1.getName())
print("Roll Number: ", s1.getRollNumber())
s1.setRollNumber("XYZ123")
print("Roll Number: ", s1.getRollNumber())