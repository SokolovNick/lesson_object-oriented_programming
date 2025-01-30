class Account:
    def __init__(self, owner_id, balance=0):
        self.owner_id = owner_id
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} was added to your account. Your balance is now {self.balance}")
        else:
            print("You didn't deposit the funds")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} was withdrawn from your account. Your balance is now {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

