
class BankAccount:
 
    def __init__(self):
        self.name = name
        self.no = 0
        self.balance = initial_amount
    
    def withdraw(self, amount):

         self.balance -= amount
         return self._balance
    
    def deposit(self, amount):
         
        self.balance += amount
        return self._balance
         
    def currentBalance(self, amount):

        self.balance = amount
        return self.b_alance
        
class MinimumBalanceAccount(BankAccount):
   
    def withdraw(self, amount):
      
          self._balance = amount
         
      
def main():
    account1 = MinimumBalanceAccount(5000)
    print(account1.currentBalance())
    account2 = BankAccount()
    account1.deposit(10000)
    account2.deposit(5000)
    print(account1.currentBalance())
    account2.withdraw(2000)
    print(account2.currentBalance())
    account1.withdraw(3000)
    account1.withdraw(6000)
    
main()
