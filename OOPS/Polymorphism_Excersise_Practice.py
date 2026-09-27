# Default Arguments

# Example 1
class Calculator:
    def __init__(self, model):
        self.model = model
    def add(self, a, b=0, c=0):
        return a + b + c
calculator = Calculator("Scientific")
print(calculator.add(10))
print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))

#Example 2
class Employee:
    def calc_Sal(self, pay, bonus=0):
        return pay + bonus
employee1 = Employee()
print("Salary w/o bonus: $", employee1.calc_Sal(100000))
print(f'Salary w/ bonus: ${employee1.calc_Sal(100000, 10000)}')

#Example 3
class ArVo:
    def calc(self, length, width=None, height=None, radius=None):
#        print("If Circle, enter Other vars as 1")
        if not width:
            print(f"Area of Square: {length**2}")
        elif not height:
            print(f'Area of Rectangle: {length*width}')
        elif not radius:
            print(f"Volume of Prism: {length*width*height}")
        elif radius:
            print(f"Area of Circle: {3.14*radius}")
        else:
            print("ERROR! TRY AGAIN.")
calc = ArVo()
calc.calc(2)
calc.calc(2,3)
calc.calc(2,3,4)
calc.calc(1,1,1,3)

#Example 4
class Login:
    def login_info(self, username, password = None):
        self.username = username
        self.password = password

        if self.password == None:
            print(f'Welcome {self.username}!')
            nPassword = input("Create a password: ")
            password = nPassword
            return "Account created!"
        elif password == "I_l0ve_c0ding>#<":
            print("Correct! Access to account granted.")
        else:
            print("ERROR! WRONG PASSWORD! INITIATING ACCOUNT LOCKDOWN & ALERT!!!")

me = Login()
me.login_info("miruthun_is_here")
me.login_info("miruthun_is_here", "I_l0ve_c0ding>#<")
me.login_info("miruthun_is_here", "1234567890")

#Example 5
class bankAccount:
    def bankAccInit(self, holder_name, password, balance=0):
        self.holder_name = holder_name
        self.password = password
        self.balance = balance
        balance += int(input("Enter deposit amount (or negative if withdrawing): "))
        print(balance)

accMe = bankAccount()
accMe.bankAccInit("Miruthun", "123454321")
accMe.bankAccInit("Miruthun", "123454321", 123)

# *args Examples

# Example 1
class Grade_AVG_calc:
    def __init__(self):
        if self:
            print("***")
    def AVG(self, *marks):
        if len(marks) < 1:
            print("Not Applicable")
        else:
            tot = sum(marks)
            length = len(marks)
        return round((tot / length), 2)
student1 = Grade_AVG_calc()
print(student1.AVG(90,20))
print(student1.AVG(1,2,3))
print(student1.AVG(70, 80, 90, 100, 89, 79, 69, 100, 76, 98, 82))

# Example 2
class Scanner:
    def Scan(self, *prices):
        return (sum(prices) + 0.07*(sum(prices)))
scanner1 = Scanner()
print(round(scanner1.Scan(2.99, 3.99, 4.99, 5.99, 10.99, 1.99, 0.25, 101.01, 100.00, 12.99), 2))

# Example 3
class messenger:
    def message(self, message, *people):
        print(f"To: {people}")
        print(message)
    def massSend(self, message, *people):
        for person in people:
            print(f'{person}, {message}')
message1 = messenger()
message1.message("Hi everyone!", "Rahul", "Dravid", "Pranav", "John")
message1.massSend("I hope you are doing well", "Rahul", "Dravid", "Pranav", "John")

#Example 4
class Words:
    def concatenator(self, decision=0, *words):
        self.decision = decision
        self.words = words
        if decision == 1:
            for item in words:
                print(item)
        else:
            for item in words:
                print(item, end = " ")
User1 = Words()
User1.concatenator(1, "Hello", "World", "I", "Now", "Exist")
print()
User1.concatenator("Hello", "World", "I", "Now", "Exist")
print()
print("---------------------------------")

#Example 5
class word_Check():
    def message_sum(self, *keywords):
        message = input("Enter message: ")
        for item in keywords:
            if item in message:
                print(f"{item} is Present")
            else:
                print(f"{item} was not found")
error1 = word_Check()
error1.message_sum("Error", "Failure", "Disaster")