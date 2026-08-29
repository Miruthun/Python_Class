# ============================================================
# 2. MULTILEVEL INHERITANCE
# Grandparent → Parent → Child
# ============================================================

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):

    def bark(self):
        print(self.name, "is barking")


class Puppy(Dog):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def play(self):
        print(self.name, "is playing")


puppy = Puppy("Tommy", 2)

print("\nName:", puppy.name)
print("Age:", puppy.age)

puppy.eat()       # From Animal
puppy.bark()      # From Dog
puppy.play()      # From Puppy