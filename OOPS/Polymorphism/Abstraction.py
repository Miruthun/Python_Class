# Example 2: Child Cannot Access Private Variable Directly
class Parent:
  def init(self):
    self.__name = "Aman"

class Child(Parent):
  def show_name(self):
    print(self.__name)

obj = Child()

obj.show_name() # AttributeError
# Example 3: Access Private Variable Using Getter
class Parent:
    def init(self):
        self.__name = "Aman"

    def get_name(self):
        return self.__name

class Child(Parent):
  def show_name(self):
    print(self.get_name())

obj = Child()
obj.show_name()

# Example 4: Access Private Age Using Getter
class Parent:
    def init(self):
        self.__age = 20

    def get_age(self):
        return self.__age

class Child(Parent):
  def show_age(self):
    age = self.get_age()
    print(age)

obj = Child()
obj.show_age()

# Example 5: Access Private Variable Using Public Method
class Parent:
  def init(self):
    self.__city = "Jalandhar"

def show_city(self):
    print(self.__city)

class Child(Parent):
  def display(self):
    self.show_city()

obj = Child()
obj.display()

# Example 6: Access Private Method Indirectly
class Parent:
  def __private_message(self):
    print("Hello from the parent")

def send_message(self):
    self.__private_message()

class Child(Parent):
  def show_message(self):
    self.send_message()

obj = Child()
obj.show_message()

# Example 7: Use Private Variable in Parent Calculation
class Parent:
  def init(self):
    self.__price = 100

def get_price_with_tax(self):
    return self.__price + 10

class Child(Parent):
  def show_total(self):
    print(self.get_price_with_tax())

obj = Child()
obj.show_total()

# Example 8: Update Private Variable Using Setter
class Parent:
  def init(self):
    self.__score = 0

def set_score(self, score):
    self.__score = score

def get_score(self):
    return self.__score

class Child(Parent):
  def update_and_show(self):
    self.set_score(95)
    print(self.get_score())

obj = Child()
obj.update_and_show()

# Example 9: Access Private Variable Using Name Mangling
class Parent:
  def init(self):
    self.__language = "Python"

class Child(Parent):
  def show_language(self):
    print(self._Parent__language)

obj = Child()
obj.show_language()

# Example 10: Separate Private Variables in Parent and Child
class Parent:
  def init(self):
    self.__value = "Parent value"

def get_parent_value(self):
    return self.__value

class Child(Parent):
  def init(self):
    super().init()
    self.__value = "Child value"

def show_values(self):
    print(self.get_parent_value())
    print(self.__value)

obj = Child()
obj.show_values()