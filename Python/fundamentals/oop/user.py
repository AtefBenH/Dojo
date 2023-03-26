class User :

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit (self, amount):
        self.account_balance+= amount

    def make_withdrawal(self, amount):
        self.account_balance-= amount
    
    def display_user_balance(self):
        print (f"User : {self.name}, Balance : {self.account_balance}")

    def transfer_money (self, user, amount):
        self.account_balance-= amount
        user.account_balance+= amount
    
#Main
user1 = User ("Walter White", "walter_white@gmail.com")
user2 = User ("Keyser Soze", "keyser_soze@yahoo.fr")
user3 = User ("Monkey-D Luffy", "luffy@aol.com")

user1.make_deposit(200)
user1.make_deposit(150)
user1.make_deposit(300)
user1.make_withdrawal(175)
user1.display_user_balance()

user2.make_deposit(250)
user2.make_deposit(175)
user2.make_withdrawal(100)
user2.make_withdrawal(50)
user2.display_user_balance()

user3.make_deposit(300)
user3.make_withdrawal(150)
user3.make_withdrawal(200)
user3.make_withdrawal(50)
user3.display_user_balance()

user1.transfer_money(user3, 200)
user1.display_user_balance()
user3.display_user_balance()



