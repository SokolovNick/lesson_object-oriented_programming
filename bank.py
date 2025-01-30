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

    def check_balance(self):
        print(f"Your balance is {self.balance}")


account_1 = Account(1000000001, 1000)

account_1.check_balance()
account_1.withdraw(700)
account_1.withdraw(500)
account_1.deposit(10000)
