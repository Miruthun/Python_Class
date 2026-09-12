# We can achieve similar behavior using:
# 1. Default arguments
# 2. *args
# 3. **kwargs
# 4. Conditional logic
# ============================================================
# EXAMPLE 1
# Calculator with different number of values
# ============================================================
# class Calculator:

# def add(self, a, b=0, c=0):
#     return a + b + c

# calculator = Calculator()

# print("Example 1")
# print(calculator.add(10))
# print(calculator.add(10, 20))
# print(calculator.add(10, 20, 30))

# print()

# ============================================================
# EXAMPLE 2
# Student marks
# One subject, two subjects or three subjects
# ============================================================
# class Student:

# def calculate_marks(self, maths, science=0, english=0):
#     total = maths + science + english
#     return total

# student = Student()

# print("Example 2")
# print(student.calculate_marks(80))
# print(student.calculate_marks(80, 75))
# print(student.calculate_marks(80, 75, 90))

# print()

# ============================================================
# EXAMPLE 3
# Shopping bill
# Different number of products
# ============================================================
# class ShoppingCart:

# def calculate_bill(self, price1, price2=0, price3=0, discount=0):

# total = price1 + price2 + price3

# final_price = total - (total * discount / 100)

# return final_price

# cart = ShoppingCart()

# print("Example 3")

# print(cart.calculate_bill(500))

# print(cart.calculate_bill(500, 300))

# print(cart.calculate_bill(500, 300, 200))

# print(cart.calculate_bill(500, 300, 200, 10))

# print()

# ============================================================
# EXAMPLE 4
# Employee salary
# Bonus can be provided or not
# ============================================================
# class Employee:

# def calculate_salary(self, salary, bonus=0):

# return salary + bonus

# employee = Employee()

# print("Example 4")

# print("Salary:", employee.calculate_salary(50000))

# print("Salary with bonus:",
#    employee.calculate_salary(50000, 10000))

# print()

# ============================================================
# EXAMPLE 5
# *args
# Calculate average of different number of marks
# ============================================================
# class Marks:

# def average(self, *marks):

# if len(marks) == 0:
#       return 0

# total = sum(marks)

# return total / len(marks)

# marks = Marks()

# print("Example 5")

# print(marks.average(80, 90))

# print(marks.average(80, 90, 70))

# print(marks.average(80, 90, 70, 85, 95))

# print()

# ============================================================
# EXAMPLE 6
# Area calculator
# One value = square
# Two values = rectangle
# ============================================================
# class AreaCalculator:

# def calculate_area(self, length, width=None):

# if width is None:

# # One argument
#       # Treat it as a square

# return length * length

# else:

# # Two arguments
#       # Treat them as length and width

# return length * width

# area = AreaCalculator()

# print("Example 6")

# print("Square Area:",
#    area.calculate_area(5))

# print("Rectangle Area:",
#    area.calculate_area(5, 10))

# print()

# ============================================================
# EXAMPLE 7
# Login system
# Username only
# Username + password
# ============================================================
# class Login:

# def login(self, username, password=None):

# if password is None:

# return "Welcome " + username

# else:

# if password == "python123":
#         return "Login successful"

# return "Incorrect password"

# login = Login()

# print("Example 7")

# print(login.login("Arvinder"))

# print(login.login("Arvinder", "python123"))

# print(login.login("Arvinder", "wrong"))

# print()

# ============================================================
# EXAMPLE 8
# Message system using *args
# ============================================================
# class Notification:

# def send(self, *users):

# if len(users) == 0:

# return "No users selected"

# message = "Message sent to: "

# for user in users:
#       message += user + " "

# return message

# notification = Notification()

# print("Example 8")

# print(notification.send("Rahul"))

# print(notification.send("Rahul", "Aman"))

# print(notification.send("Rahul", "Aman", "Priya", "Simran"))

# print()

# ============================================================
# EXAMPLE 9
# Product price calculator
# Different ways to calculate price
# ============================================================
# class Product:

# def price(self, amount, quantity=1, discount=0):

# total = amount * quantity

# discount_amount = total * discount / 100

# final_price = total - discount_amount

# return final_price

# product = Product()

# print("Example 9")

# One argument
# print(product.price(1000))

# Price + quantity
# print(product.price(1000, 3))

# Price + quantity + discount
# print(product.price(1000, 3, 10))

# print()

# ============================================================
# EXAMPLE 10
# *args with different operations
# ============================================================
# class CalculatorAdvanced:

# def calculate(self, operation, *numbers):

# if len(numbers) == 0:
#       return "No numbers provided"

# if operation == "add":

# return sum(numbers)

# elif operation == "multiply":

# result = 1

# for number in numbers:
#         result = result * number

# return result

# elif operation == "maximum":

# return max(numbers)

# elif operation == "minimum":

# return min(numbers)

# else:

# return "Invalid operation"

# calculator = CalculatorAdvanced()

# print("Example 10")

# print(calculator.calculate("add", 10, 20, 30))

# print(calculator.calculate("multiply", 2, 3, 4))

# print(calculator.calculate("maximum", 10, 50, 20, 40))

# print(calculator.calculate("minimum", 10, 50, 20, 40))

# print()