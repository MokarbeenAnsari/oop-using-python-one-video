# Implementing properties of class: Class variable.

class Employee:
    id = 47936
    name = "Ansari"
    salary = 50000
    department = "IT"

e1 = Employee()

# e1.id = 47935
# e1.name = "Mokarbeen"
# e1.salary = 100000
# e1.department = "IT"
e1.manager = "Rahul"


print("ID: ", e1.id)
print("Name: ", e1.name)
print("Salary: ", e1.salary)
print("Department: ", e1.department)
print("Manager: ", e1.manager)