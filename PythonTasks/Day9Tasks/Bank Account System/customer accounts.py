"""4. Bank Account System (Class, Object, Constructor)
A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance."""

class BankAccount:
    def __init__(self, acc, balance):
        self.acc = acc
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print("Account Number:", self.acc)
        print("Balance:", self.balance)


b = BankAccount(12345, 5000)
b.deposit(1000)
b.withdraw(2000)
b.display()
