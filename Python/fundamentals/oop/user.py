class User :

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit (self, amount):
        self.account_balance+= amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance-= amount
        return self
    
    def display_user_balance(self):
        print (f"User : {self.name}, Balance : {self.account_balance}")

    def transfer_money (self, user, amount):
        self.account_balance-= amount
        user.account_balance+= amount
        print("--------------------------------------------------------------------")
        print(f"{self.name} just sent {amount}$ to {user.name}")
        print("--------------------------------------------------------------------")
        return self
    
#Main
user1 = User ("Walter White", "walter_white@gmail.com")
user2 = User ("Keyser Soze", "keyser_soze@yahoo.fr")
user3 = User ("Monkey-D Luffy", "luffy@aol.com")

user1.make_deposit(1500).make_deposit(250).make_deposit(300).make_withdrawal(375).display_user_balance()

user2.make_deposit(250).make_deposit(575).make_withdrawal(100).make_withdrawal(350).display_user_balance()

user3.make_deposit(700).make_withdrawal(250).make_withdrawal(300).make_withdrawal(150).display_user_balance()

user1.transfer_money(user3, 500).display_user_balance()
user3.display_user_balance()



