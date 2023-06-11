# Encapsulation: Getters & Setters
class User:
    def __init__(self, name=None, password=None):
        self.__name = name
        self.__password = password

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name
    

usr = User("Mokarbeen", "12345")
print("Name: ", usr.getName())
usr.setName("Mokarbeen Ansari")
print("Name: ", usr.getName())