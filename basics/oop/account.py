class Account():

    def __init__(self, balance, filepath):
        self.file = filepath
        self.balance = balance
        with open(self.file, 'w') as file:
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
        with open(self.file, 'w') as file:
            file.write(str(self.balance))


account = Account(1000, "balance.txt")
print(account)
account.deposit(2050)
print(account)