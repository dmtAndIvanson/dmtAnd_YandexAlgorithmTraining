# Create class 'Client'.
# Make make 5 methods: DEPOSIT, WITHDRAW, BALANCE, TRANSFER, INCOME.
# Make 2 properties for each client: name, money.

class CLIENT():
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def DEPOSIT(self, sum):
        self.money += sum

    def WITHDRAW(self, sum):
        self.money -= sum

    def BALANCE(self):
        return self.money

    def TRANSFER(self):

"""I can't understand how to run commands for python program, if they are written in text."""
