# Implementing properties of class: Instance & Class variable.

class Employee:
    def __init__(self, id=0, name=None, salary=0, department=None):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

e1 = Employee(47935, "Mokarbeen", "50000", "IT")
e2 = Employee(47936, "Mustkim", "20000", "Medical")

print("ID: ", e1.id)
print("Name: ", e1.name)
print("Salary: ", e1.salary)
print("Department: ", e1.department)
print()
print("ID: ", e2.id)
print("Name: ", e2.name)
print("Salary: ", e2.salary)
print("Department: ", e2.department)