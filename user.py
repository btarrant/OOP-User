class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


messi = User("Lionel Messi")
drogba = User("Didier Drogba")
gary = User("Gary Neville")

messi.make_deposit(100)
messi.make_deposit(200)
messi.make_deposit(50)
messi.make_withdrawal(45)
messi.display_user_balance()

drogba.make_deposit(300)
drogba.make_deposit(1000)
drogba.make_withdrawal(30)
drogba.make_withdrawal(68)
drogba.display_user_balance()

gary.make_deposit(8550)
gary.make_withdrawal(275)
gary.make_withdrawal(43)
gary.make_withdrawal(20)
gary.display_user_balance()

gary.transfer_money(40, messi)