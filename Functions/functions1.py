# What are functions?
# A function is a block of code (in Python: defined using 'def') 
# that can be executed (called) multiple times, whenever required.

# -------------------------
# Basic Example (No Function)
# -------------------------

# Print "Hello World!" once
print("Hello World!")

# -------------------------
# Level 2: Print it 10 times
# -------------------------

# Repeating print() 10 times (not optimal)
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")

# This violates the DRY Principle: Don't Repeat Yourself

# -------------------------
# Better Method: Using Loops
# -------------------------

# Loop to print "Hello World!" 10 times
for i in range(10):  # Loop runs from 0 to 9 (10 times)
    print("Hello World!")

# Note: This prints the same message every time.
# What if we want to customize the message?

# -------------------------
# Best Method: Using Functions
# -------------------------

# Types of Functions:
# 1. Built-in Functions – Provided by Python, e.g., print(), len(), type(), list(), set()
# 2. User-defined Functions – Created by developers using 'def' keyword

# Example of a User-defined Function
def greet():
    print("Good Morning!")

# Calling the function multiple times
greet()
greet()
greet()
