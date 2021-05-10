#Do not change any part of the initial code.
class BankAccount:
    def __init__(self):
        self.balance=0
    
    def withdraw(self, _amount):
      if (self.balance>=_amount):  
        self.balance=self.balance- _amount
        print("Withdrawal was completed successfully")

    def deposit(self, _amount):
      if (_amount>0):  
        self.balance=self.balance+ _amount
        print("Deposit completed successfully")
        
    def currentBalance(self):
      return self.balance
        
class MinimumBalanceAccount(BankAccount):
    def __init__(self, _minimumBalance):
        BankAccount.__init__(self) #new inheretance
        self.minimumBalance=_minimumBalance
   
    def withdraw(self, _amount):
      if (self.balance-self.minimumBalance>=_amount):  
        BankAccount.withdraw(self,_amount)
      
      else:    
          print("Warning! Minimum balance must be maitained")
            
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
