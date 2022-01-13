class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

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

messi.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(45).display_user_balance()

drogba.make_deposit(300).make_deposit(1000).make_withdrawal(30).make_withdrawal(68).display_user_balance()

gary.make_deposit(8550).make_withdrawal(275).make_withdrawal(43).make_withdrawal(20).display_user_balance()

gary.transfer_money(40, messi)