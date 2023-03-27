class account:
    def __init__(self, title=None, balance=0):
       # a = "account_holder : "
        #b = "main balance : "
        self.title =title
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount     

    def withdrawal(self, amount):
        self.balance = self.balance - amount

    def getbalance(self):
        print("now current balance is :")
        return  self.balance


class saving_account(account):
    print("initial account details :")
    def __init__(self, title=None, balance=0, interest_rate=0):
       # c = "interest rate : "
        super().__init__(title,balance)
        self.interest_rate =interest_rate  

    def interest_amount(self):
        print("my interest amount is...")
        return (self.balance * self.interest_rate / 100)


account = saving_account('sam',2000,5) 

print(account.title, account.balance, account.interest_rate, sep=" ")

account.deposit(int(input("enter deposit amount :")))

account.withdrawal(int(input("enter withdrawl amount :")))

print(account.getbalance())

print(account.interest_amount())