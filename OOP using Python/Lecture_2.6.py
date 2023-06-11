# Implementing method in class: Instance Method
class Employee:
    def __init__(self, id=0, name=None, salary=0, department=None):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department

    def tax(self):
        tax = self.salary * 0.2
        return tax

    def salaryPerDay(self):
        return self.salary/30

e1 = Employee(47935, "Mokarbeen", 50000, "IT")

print("ID: ", e1.id)
print("Name: ", e1.name)
print("Salary: ", e1.salary)
print("Department: ", e1.department)
print()
print("Calculated tax: ", e1.tax())
print("Salary of one day: ", e1.salaryPerDay())




