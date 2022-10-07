class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
            self.balance += amount
            #print("Balance:" , self.balance)
            return self
    def withdraw(self, amount):
            self.balance -= amount
            #print("Balance:", self.balance)
            return self
    def display_account_info(self):
            print("Balance: $",self.balance)
            return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate) 
            return self

account1 = BankAccount(0.01, 0)
account2 = BankAccount(0.01, 0)

account1.deposit(50).deposit(70).deposit(69).withdraw(30).yield_interest().display_account_info()
account2.deposit(150).deposit(170).withdraw(30).withdraw(12).withdraw(5).withdraw(72).yield_interest().display_account_info()


