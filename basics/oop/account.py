import os

class Account():

    def __init__(self, balance, filename):
        self.filepath = os.path.dirname(os.path.abspath(__file__)) + "/" + filename
        self.balance = balance
        with open(self.filepath, 'w') as file:
            file.write(str(balance))

    def __str__(self):
        return str(self.balance)


    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self.commit()
        else:
            print("You can't withdraw a negative amount.")


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.commit()
        else:
            print("You can't deposit a negative amount.")


    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, balance, transferFee, filename):
        super().__init__(balance, filename)
        self.fee = transferFee

    def transfer(self, amount):
        if self.balance > (amount + self.fee):
            self.balance -= (amount + self.fee)
            self.commit()
        else:
            print("Insufficient funds.")

account = Account(1500, "balance.txt")
print(account)
account.deposit(700)
account.withdraw(350)
print(account)

checking = Checking(2000, 10, "balance2.txt")
checking.transfer(1000)
print(checking)