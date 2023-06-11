# Banking Account
# Parent class
class Account:
    def __init__(self, name=None, balance=0) -> None:
        self.name = name
        self.balance = balance

# Child class
class SavingsAccount(Account):
    def __init__(self, name=None, balance=0, interestRate=0) -> None:
        super().__init__(name, balance)
        self.interestRate = interestRate


user1 = SavingsAccount("Mokarbeen", 5000, 5)
print(user1.name)
print(user1.balance)
print(user1.interestRate)
