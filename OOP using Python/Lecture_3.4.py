# Encapsulation Incorporation
class Employee:
    __companyName = "XYZ"

    def __init__(self, id=0, name=None, salary=0, department=None):
        self.__id = id
        self.__name = name
        self.__salary = salary
        self.__department = department

    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getDepartment(self):
        return self.__department

    def tax(self):
        tax = self.__salary * 0.2
        return tax

    def salaryPerDay(self):
        return self.__salary/30

    @classmethod
    def getCompanyName(cls):
        return cls.__companyName

e1 = Employee(47935, "Mokarbeen", 50000, "IT")

print("ID: ", e1.getID())
print("Name: ", e1.getName())
print("Salary: ", e1.getSalary())
print("Department: ", e1.getDepartment())
print()
print("Calculated tax: ", e1.tax())
print("Salary of one day: ", e1.salaryPerDay())
print()
print("Company name: ", Employee.getCompanyName())





