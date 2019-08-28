class BasketBallPlayer:
    def __init__(self, _age, _name, _phoneNumber):
        self.name=_name
        self.age=_age
        self.myphoneNumber=_myphoneNumber
        self.weight=0
        self.height=0
        self.attack=false
        self.defence=false
        self.shoot=false

    def canAttack(self, _val):
        self.attack=_val

#inheritance

class BankAccount:
    
        accountnumber
        accountbalance
        accountholderName

class ChequingsBankAccount(BankAccount):
        overdraftAmount

        def chargeOverdraftFee(self, _value)
        self.accountbalance=self.accountbalance-_value
    

class SavingsBankAccount:

accountInterestRate



class BankAccount:
    def __init__(self):
        self.accountNumber=0
        self.balance=0
        self.accountType=""
        self.myphoneNumber=0
        self.myPersonalInformation=""

    #self is basic syntax to define classes and constructors
    #1) Functions
    #1.1.Constructor
    #1.2. Accessors and Mutators
        #when you return some value its accessor
        #when you update its mutator(password?)

    def deposit(self, amount):
        self.balance = self.balance+amount
    
    def toString(self):
        print("Your account balance is:", self.balance)
    
    def withdraw(self, amount):
        self.balance = self.balance-amount
        print("Your remaining account balance is:", self.balance)


def main():
    obj1= BankAccount()
    obj1.deposit(1000)
    obj1.deposit(20)
    obj1.toString()
    obj1.withdraw(100)
    
main()
