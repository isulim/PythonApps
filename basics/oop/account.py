class Account():

    def __init__(self, filepath):
        self.file = filepath
        with open(self.file, 'r') as file:
            self.balance = float(file.read())


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


account = Account("balance.txt")
print(account)
account.deposit(2050)
print(account)