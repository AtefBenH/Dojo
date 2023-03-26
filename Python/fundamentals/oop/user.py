from bank_account import BankAccount
class User :

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
                "Checking" : BankAccount(0, 0.1),
                "Savings" : BankAccount(0, 0.5)
                }

    # def make_deposit (self, amount):
    #     self.account.deposit(amount)
    #     return self

    # def make_withdrawal(self, amount):
    #     self.account.withdraw ()
    #     return self
    
    def display_user_balance(self):
        print (f"User : {self.name}, Checking Balance : {self.account['Checking'].balance}")
        print (f"User : {self.name}, Savings Balance : {self.account['Savings'].balance}")

    def transfer_money (self, user, amount):
        self.account.balance-= amount
        user.account.balance+= amount
        print("--------------------------------------------------------------------")
        print(f"{self.name} just sent {amount}$ to {user.name}")
        print("--------------------------------------------------------------------")
        return self
    
#Main
#! Go to main.py to test



