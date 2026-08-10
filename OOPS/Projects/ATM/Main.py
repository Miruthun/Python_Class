# BankAccount - Entity 

# name , account_number , pin -- attributes 

# withdraw , deposit , checkBalance , pinChange, 

class BankAccount:
    def __init__(self, name,acc_number,pin,balance=0):
        self.name = name
        self.acc_number = acc_number
        self.pin = pin
        self.balance=balance
        print("Hi ",self.name , "Your account is created with us.Thanks for trusting our bank with your money.")
    
    def display_details(self):
        print("========= Account Details =======")
        print("Account Holder Name:",self.name)
        print("Account Number:" , self.acc_number)
        print("Balance:",self.balance)
    
    def display_balance(self):
        print("Current Balance:",self.balance)
    
    def deposit(self,amount):
        if amount<=0:
            print("Error: Amount should be greater than 0")
            return 
        
        self.balance+=amount
        print("Current balance:",self.balance)
   
    def withdraw(self,amount):
        if amount<=0:
            print("Error: Withdraw amount should be greater than 0")
            return 
        
        if amount > self.balance:
            print("Insufficient Balance")
            return 
        
        self.balance-= amount 
        print("Current balance:",self.balance)
    
    def change_pin(self,cPass,nPass):
        # cPass - Current Password 
        # nPass - New Password

        if cPass!=self.pin:
            print("Current Pin is incorrect")
            return 
        
        self.pin = nPass 
        print("Pin changed successfully.")

class Greet:
    def __init__(self):
        print("Hello")


account1 = BankAccount(
    name="Arvinder",
    acc_number=5776,
    pin = 1234,
    balance=1000
)
# account1.display_details()
account1.change_pin(1234,4040)
account2 = BankAccount(
    name="Miruthun",
    acc_number=4545,
    pin = 5678,
    balance=3000
)

firstGreet = Greet()
# Object->method -- For calling Methods in c/c++
# account2.display_details() - In Python


    

    




