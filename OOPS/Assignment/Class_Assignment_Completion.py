# Solution 1:
class Car:
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Color:", self.color)
    def update_price(self, new_price):
        self.price = new_price
    def change_color(self, new_color):
        self.color = new_color

car1 = Car("Toyota", "Sienna", 40000, "Grey")
car1.display_details()
print()
car1.update_price(41000)
car1.change_color("Gray")
car1.display_details()
print()

# Solution 2:
class BankAccount:
    def __init__(self, accountHolder, accountNum, Balance):
        self.accountHolder = accountHolder
        self.accountNum = accountNum
        self.Balance = Balance
    def display_details(self):
        print("Account Holder:", self.accountHolder)
        print("Account Number:", self.accountNum)
        print("Balance:", self.Balance)
    def deposit(self, amount1):
        self.Balance = self.Balance + amount1
    def withdraw(self, amount2):
        self.Balance = self.Balance - amount2

car1 = BankAccount("Bob", "1002", 15432)
car1.display_details()
print()
car1.deposit(2000)
car1.withdraw(100)
car1.display_details()
print()

# Solution 3: 
class Mobile:
    def __init__(self, brand, model, price, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.storage = storage
    def display_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)
        print("Storage:", self.storage)
    def update_price(self, new_price):
        self.price = new_price
    def update_storage(self, newStorage):
        self.storage = newStorage
    def make_call(self, num):
        print(f'Calling {num}...')

mobile1 = Mobile("Apple", "iphone 17 Pro Max", 2000, "1TB")
mobile1.display_details()
print()
mobile1.make_call("9897778892")
print()
mobile1.update_price(1500)
mobile1.update_storage("512GB")
car1.display_details()
print()

# Solution 4
class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary
    def display_details(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Department:", self.department)
        print("Salary:", self.salary)
    def give_bonus(self, amount):
        self.salary = self.salary + amount
    def change_department(self, new_dep):
        self.department = new_dep

employee1 = Employee("John", "1002", "IT", 100000)
employee1.display_details()
print()
employee1.give_bonus(1000)
employee1.change_department("Engineering")
employee1.display_details()
print()

# Solution 5
class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    def display_details(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Category:", self.category)
    def sell(self, quantity):
        self.quantity = self.quantity - quantity
    def update_price(self, new_price):
        self.price = new_price

product1 = Product("Keyboard", "500", 100, "Electronics")
product1.display_details()
print()
product1.sell(3)
product1.display_details()
print()
product1.update_price(200)
product1.display_details()
print()