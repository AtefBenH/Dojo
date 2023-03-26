class BankAccount:
    #! Class Attribute
    all_accounts =[] 

    #! Constructor
    def __init__(self, balance = 0, in_rate = 0.02, type = "Checking"): 
        self.balance = balance
        self.in_rate = in_rate
        self.type = type
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance+= amount
        return self
    
    def withdraw (self, amount):
        self.balance-= amount
        return self
    
    def display_account_info(self):
        print(f"Balance : {self.balance}")
    
    def yield_interest(self):
        if BankAccount.check_balance(self.balance) :
            self.balance+= self.balance*self.in_rate
        else :
            print(f"Sorry, we can't yield the interest, the balance is negative : {self.balance}")
        return self
    
    @classmethod
    def display_all_info(cls):
        for account in BankAccount.all_accounts :
            print(f"Balance : {account.balance}")

    #? a static method to check if the balance is positive, we use it in the method yield_interest()
    @staticmethod
    def check_balance(balance):
        if balance>0 :
            return True
        else :
            return False

# account1= BankAccount(1500, 0.1)
# account2= BankAccount()
# account1.deposit(2000).deposit(1200).deposit(4400).withdraw(5500).yield_interest().display_account_info()
# account2.deposit(1500).deposit(200).withdraw(500).withdraw(700).withdraw(1500).withdraw(200).yield_interest().display_account_info()
# BankAccount.display_all_info()