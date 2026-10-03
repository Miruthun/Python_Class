# EXAMPLE 1: Basic Method Overriding
# Concept: Child class overrides parent class method

class Parent:


    def show(self):
        print("This is the parent class")

class Child(Parent):


    def show(self):
        print("This is the child class")

obj = Child()
obj.show()

# EXAMPLE 2: Same Method, Different Classes
# Concept: Different classes have the same method name

class Student:

    def introduce(self):
        print("I am a student")

class Teacher:

    def introduce(self):
        print("I am a teacher")

student = Student()
teacher = Teacher()

student.introduce()
teacher.introduce()

# EXAMPLE 3: Same Function, Different Objects
# Concept: One function can work with different objects

class Dog:

    def sound(self):
        print("Dog says Woof")

class Cat:

    def sound(self):
        print("Cat says Meow")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

# EXAMPLE 4: Runtime Polymorphism with Inheritance
# Concept: Parent reference can hold different child objects

class Employee:

    def work(self):
        print("Employee is working")

class Developer(Employee):

    def work(self):
        print("Developer is writing code")

class Designer(Employee):

    def work(self):
        print("Designer is creating designs")

employees = [
    Developer(),
    Designer(),
    Employee()
]

for employee in employees:
    employee.work()

# EXAMPLE 5: Method Overriding with Parameters
# Concept: Overridden methods can accept arguments

class Calculator:

    def calculate(self, a, b):
        print("Parent calculation:", a + b)

class Multiplier(Calculator):

    def calculate(self, a, b):
        print("Multiplication:", a * b)

class Divider(Calculator):

    def calculate(self, a, b):
        print("Division:", a / b)

operations = [
    Calculator(),
    Multiplier(),
    Divider()
]

for operation in operations:
    operation.calculate(20, 5)

# EXAMPLE 6: Using super()
# Concept: Child can call the parent method too

class Vehicle:

    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):

    def start(self):
        super().start()
        print("Car engine is running")

car = Car()
car.start()

# EXAMPLE 7: Real World Payment System
# Concept: Different payment methods perform the same action

class UPI:

    def pay(self, amount):
        print("Paid", amount, "using UPI")

class CreditCard:

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class NetBanking:

    def pay(self, amount):
        print("Paid", amount, "using Net Banking")

def make_payment(payment_method, amount):
    payment_method.pay(amount)

make_payment(UPI(), 1500)
make_payment(CreditCard(), 2500)
make_payment(NetBanking(), 3500)

# EXAMPLE 8: Notification System
# Concept: One function handles different notification types

class Email:

    def send(self, message):
        print("Email sent:", message)

class SMS:

    def send(self, message):
        print("SMS sent:", message)

class WhatsApp:

    def send(self, message):
        print("WhatsApp message sent:", message)

def notify(service, message):
    service.send(message)

message = "Your order has been shipped!"

services = [
    Email(),
    SMS(),
    WhatsApp()
]

for service in services:
    notify(service, message)
