# Example 1:
class SecretInfo:
    def init(self):
        self.__privInfo = "123PrivateDr"

class Hack(SecretInfo):
    def show_info(self):
        print(self.__privInfo)

hack1 = Hack()
print("---------------")
# Note: This example will output nothing as show_info cannot access privInfo.

# Example 3:
class InfoStorage:
    def __init__(self):
        self.__info1 = 3542617828

    def get_info(self):
        return self.__info1

class User(InfoStorage):
    def show_info(self):
        print(super().get_info())

bob = User()
bob.show_info()
print("---------------")

# Example 4:
class Parent:
    def __init__(self):
        self.__age = 15

    def get_age(self):
        return self.__age

class Child(Parent):
    def show_age(self):
        age = self.get_age()
        print(age)

timmy = Child()
timmy.show_age()
print("---------------")

# Example 5
class Alice:
    def __init__(self):
        self.__message = "Hi Bob"

    def msgRd(self):
        print(self.__message)

class Bob(Alice):
    def display(self):
        self.msgRd()

bob1 = Bob()
bob1.display()
print("---------------")

# Example 6
class Messenger:
    def __send_priv_msg(self):
        print("Encrypted message to Reciever")

    def send_message(self):
        self.__send_priv_msg()

class Reciever(Messenger):
    def show_message(self):
        self.send_message()

msg1 = Reciever()
msg1.show_message()
print("---------------")

# Example 7:
class Sticker_price:
    def __init__(self):
        self.__price = 100

    def taxed_price(self):
        return self.__price + 10

class Checkout(Sticker_price):
    def Show_total(self):
        print(self.taxed_price())

bill = Checkout()
bill.Show_total()
print("---------------")

# Example 8:
class Parent:
    def __init__(self):
        self.__score = 0

    def set_score(self,score):
        self.__score = score

    def get_score(self):
        print(self.__score)

class Child(Parent):
    def set_n_show(self):
        self.set_score(90)
        print(self.get_score())

obj = Child()
obj.set_n_show()
print("---------------")

# Example 9
class Parent:
    def __init__(self):
        self.__lang = "Python"

class Child(Parent):
    def Show_lang(self):
        print(self._Parent__lang)

obj = Child()
obj.Show_lang()
print("---------------")

# Example 10
class Parent:
    def __init__(self):
        self.__value = 123

    def getParVal(self):
        return self.__value

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 321

    def Show_vals(self):
        print(self.getParVal())
        print(self.__value)

obj = Child()
obj.Show_vals()
print("---------------")