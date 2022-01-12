class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self, account_balance):
        print(self, account_balance)

messi = User("Lionel Messi", "goat@messi.com")
drogba = User("Didier Drogba", "diddy@ivycoast.com")
gary = User("Gary Neville", "garynev@dojo.com")