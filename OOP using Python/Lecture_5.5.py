# Duck Typing in Python
class Dog:
    def speak(self):
        print("Woof woof")


class Cat:
    def speak(self):
        print("Meow meow")


animal = Dog()
animal.speak()

animal=Cat()
animal.speak()