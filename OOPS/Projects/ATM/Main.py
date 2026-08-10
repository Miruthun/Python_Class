# BankAccount - Entity 

# name , account_number , pin -- attributes 

# withdraw , deposit , checkBalance , pinChange, 

class BankAccount:
    def __init__(self):
        name = input("Account Holder's Name:")
        acc_number = input('Account Number:')
        pin = int(input("PIN Number:"))
        balance = input("Balance:")
        self.name = name
        self.acc_number = acc_number
        self.pin = pin
        self.balance = balance
        print("Hello ", self.name , "! Your account is created with us. Thanks for trusting our bank with your money.")
    
    def display_details(self):
        print("========= Account Details =======")
        print("Account Holder Name:",self.name)
        print("Account Number:" , self.acc_number)
        print("Balance:",self.balance)
    
    def display_balance(self):
        pin = input("Please Enter Your Pin:")
        if pin == self.pin:
            print("Current Balance:",self.balance)
        else:
            print("Error: Pin is Incorrect")
            return
    
    def deposit(self):
        pin = input("Please Enter Your Pin:")
        if pin != self.pin:
            print("Error: Incorrect Pin")

        amount = int(input("Enter Amount:"))

        if amount<=0:
            print("Error: Amount should be greater than 0")
            return 
        
        self.balance+=amount
        print("Current balance:",self.balance)
   
    def withdraw(self):
        pin = input("Please Enter Your Pin:")
        if pin != self.pin:
            print("Error: Incorrect Pin")

        amount = int(input("Enter Amount:"))

        if amount<=0:
            print("Error: Withdraw amount should be greater than 0")
            return 
        
        if amount > self.balance:
            print("Insufficient Balance")
            return 
        
        self.balance-= amount 
        print("Current balance:",self.balance)
    
    def change_pin(self):
        # cPass - Current Password 
        # nPass - New Password

        cPass = int(input("Input your current PIN:"))
        nPass = (input("Input your new PIN:"))

        if len(nPass) < 4:
            print("Error: Please Enter a PIN with 4 characters or more.")

        intTrack = 0
        for char in nPass:
            if char.isdigit():
                intTrack+=1
            else:
                continue
        if intTrack == 0:
            print("Error: Please Inculde atleast one Integer Character")

        if cPass!=self.pin:
            print("Current Pin is incorrect")
            return 
        
        self.pin = nPass 
        print("Pin changed successfully.")

class Greet:
    def __init__(self):
        print("Hello")


account1 = BankAccount()
account1.display_details()
account1.change_pin()
'''
account2 = BankAccount(
    name="Miruthun",
    acc_number=4545,
    pin = 5678,
    balance=3000
)
'''
firstGreet = Greet()
# Object->method -- For calling Methods in c/c++
# account2.display_details() - In Python


    

    




