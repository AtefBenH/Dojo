from user import User

user1 = User ("Walter White", "walter_white@gmail.com")
user2 = User ("Keyser Soze", "keyser_soze@yahoo.fr")
user3 = User ("Monkey-D Luffy", "luffy@aol.com")

user1.account['Checking'].deposit(500)
user1.account['Savings'].deposit(1500)
user1.display_user_balance()
# user1.make_deposit(1500).make_deposit(250).make_deposit(300).make_withdrawal(375).display_user_balance()

# user2.make_deposit(250).make_deposit(575).make_withdrawal(100).make_withdrawal(350).display_user_balance()

# user3.make_deposit(700).make_withdrawal(250).make_withdrawal(300).make_withdrawal(150).display_user_balance()

# user1.transfer_money(user3, 500).display_user_balance()
# user3.display_user_balance()