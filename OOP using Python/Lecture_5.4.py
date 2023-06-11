# Operator Overloading
class Comp:
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def __add__(self, other):
        tmp = Comp(self.real + other.real, self.img + other.img)
        return tmp

    def __sub__(self, other):
        pass

    def show(self):
        print(f"({self.real},{self.img})")

num1 = Comp(2,3)
num2 = Comp(1,2)

num3 = num1 + num2
num3.show()