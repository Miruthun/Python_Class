# Parents - Height ,Blonde Hairs , Skin Color
# Son - Height , Blonde Hairs , Skin Color 

# Father - Height , Blonde Hairs , Skin Color , Overweight , Illness 

# repeating the code. -- DRY Principle - Don't repeat yourself

# Calculator -- Add , Sub , Mul, Div , History

# SciCalculator -- Logs, trigometric 

# DOG IS A ANIMAL. 
# 
# Farari is a Car. 

# Parent (Animal) - Child (DOG)

# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name
        # self.__age = age

    def eat(self):
        print(f"{self.name} is eating.")

# Child Class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

# Usage
my_dog = Dog("Buddy")
my_dog.eat()  # Inherited method: prints "Buddy is eating."
my_dog.bark() # Child method: prints "Buddy says Woof!"
# print(my_dog.__age)
print(my_dog.name)

# # Parent Class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating.")

# # Child Class inheriting from Animal
# class Dog():
#     def __init__(self,name):
#         self.name=name
#     def bark(self):
#         print(f"{self.name} says Woof!")
#     def eat(self):
#         print(f"{self.name} is eating.")

# # Usage
# my_dog = Dog("Buddy")
# my_dog.eat()  # Inherited method: prints "Buddy is eating."
# my_dog.bark() # Child method: prints "Buddy says Woof!"


# Types of Inheritance - 
# 1. Simple Inheritance 
# 2. Multilevel Inheritance -- A (parent) - B (Child of A) - C (Child of B)
# 3. Multiple Inheritance - A , B - C (Child of both A and B) 
# 4. Hybrid 
# 5. Heirarchical Inheritance - 


