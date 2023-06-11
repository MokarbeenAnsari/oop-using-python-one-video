# Banking Account
# Parent Class
class Account:
    def __init__(self, name=None, balance=0) -> None:
        self.name = name
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount=0):
        self.balance += amount

    def withdraw(self, amount=0):
        self.balance -= amount

# Child Class
class SavingAccount(Account):
    def __init__(self, name=None, balance=0, interestRate=0) -> None:
        super().__init__(name, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


user1 = SavingAccount("Mokarbeen", 5000, 5)
print(user1.getBalance())
user1.deposit(1000)
print(user1.getBalance())
user1.withdraw(500)
print(user1.getBalance())
print(user1.interestAmount())
