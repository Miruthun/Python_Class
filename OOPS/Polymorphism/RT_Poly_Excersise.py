# Example 1
class Cars:
    def show_engine_details(self):
        print("Cars have engines that can accelerate very fast, depending on model.")

class Racecars(Cars):
    def show_engine_details(self):
        print("Racecars have engines that can accelerate the car to 60 mph in under 3 seconds!")

obj = Racecars()
obj.show_engine_details()
print("____________________________________")

# Example 2

class Drums:
    def identity(self):
        print("I am a drum, a band instrument.")

class Violins:
    def identity(self):
        print("I am a violin, an orchestra instrument")

drum = Drums()
violin = Violins()

drum.identity()
violin.identity()
print("____________________________________")

# Example 3

class Apple:
    def color(self):
        print("The apple is red.")

class Banana:
    def color(self):
        print("The banana is yellow.")

def color_describe(fruit):
    fruit.color()

apple = Apple()
banana = Banana()

color_describe(apple)
color_describe(banana)
print("____________________________________")

# Example 4

class Instruments:
    def Range(self):
        print("C1-C12")

class Piano(Instruments):
    def Range(self):
        print("C3-C7")

class Voice(Instruments):
    def Range(self):
        print("C4-C9")

ins = [Instruments(), Piano(), Voice()]
for i in ins:
    i.Range()
print("____________________________________")

# Example 5

class Calculator:
    def calc(self,a,b):
        print("Summation: ", a+b)

class Multiplier(Calculator):
    def calc(self,a,b):
        print("Multiplied result: ", a*b)

class Divisor(Calculator):
    def calc(self,a,b):
        print("Divided Result: ", a/b)

operations = [Calculator(), Multiplier(), Divisor()]
for operation in operations:
    operation.calc(100,5)
print("____________________________________")

# Example 6
class Vehicle:
    def engine_Start(self):
        print("Engine Started")

class Car(Vehicle):
    def start(self):
        super().engine_Start()
        print("Engine Type: Car")

car1 = Car()
car1.start()
print("____________________________________")

# Example 7

class UPI:
    def pay(self, amount):
        print(f'Paid {amount} using UPI')

class Credit_Card:
    def pay(self, amount):
        print(f'Paid {amount} using Credit Card')

class Net_Banking:
    def pay(self, amount):
        print(f'Paid {amount} using Net Banking')

def AnyPay(method, amount):
    method.pay(amount)

AnyPay(UPI(), 15000)
AnyPay(Credit_Card(), 25000)
AnyPay(Net_Banking(), 100000)
print("_____________________________")

# Example 8

class Gmail:
    def send(self, message):
        print(f"Gmail Notification: {message}")

class SMS:
    def send(self, message):
        print(f"SMS Notification: {message}")

class WhatsApp:
    def send(self, message):
        print(f"WhatsApp Notification: {message}")

def Notify(service, message):
    service.send(message)

message = "Order Shipped"
services = [Gmail(), SMS(), WhatsApp()]
for service in services:
    Notify(service, message)