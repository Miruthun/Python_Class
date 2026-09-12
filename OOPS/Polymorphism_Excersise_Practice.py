import random

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
class WordPredict:
    def __init__(self, username):
        self.username = username
        print()
        print(f"Hello {self.username}, welcome to Word Predict! Here, we will guess a word that you might have been thinking of!")
        print()
    def words(self, *words):
        list1 = []
        for item in words:
            list1.append(item)
        #comp_choice = random.random(list1)
        #print(comp_choice)
        print("Was it your choice?")

#trial1 = WordPredict("Miruthun")
#print(trial1.words("Hi", "I", "Am", "Miruthun", "You", "won't", "Guess", "My", "Word!"))

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
