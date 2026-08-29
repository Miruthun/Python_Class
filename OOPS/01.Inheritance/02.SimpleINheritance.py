# ============================================================
# 1. SIMPLE INHERITANCE
# One Parent Class → One Child Class
# ============================================================

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(self.name, "is barking")


# Creating object of child class
dog = Dog("Bruno", "Labrador")

print("Name:", dog.name)
print("Breed:", dog.breed)

dog.eat()       # Inherited method
dog.bark()      # Child class method