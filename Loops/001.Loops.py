# Python Loops: For and While

# Introduction to Loops
# Loops allow repetitive execution of code blocks.
# Two main types: 'for' (definite iterations) and 'while' (indefinite iterations).
# Iteration: Visiting each element in a sequence or repeating until a condition is met.

print("=== While Loop ===")
# While loop executes as long as a condition is True.
# Structure: Initialize, Check Condition, Execute, Update Counter.
i = 0  # Initialization: Set starting value
while i < 5:  # Condition: Loop runs if True
    print(i)  # Task: Print current value
    i += 1  # Increment: Update counter to avoid infinite loop
# Output: 0, 1, 2, 3, 4

print("\n=== Squares from 1 to 10 ===")
# Print squares of numbers from 1 to 10 using while loop.
x = 1  # Initialize
while x <= 10:  # Condition
    print(x**2)  # Task: Print square
    x += 1  # Increment
# Output: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

print("\n=== Decrementing Loop ===")
# Print double of numbers from 10 to 0.
x = 10  # Initialize
while x >= 0:  # Condition
    print(x * 2)  # Task: Print double
    x -= 1  # Decrement
# Output: 20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0

# When to Use While Loops
# Use while loops when the number of iterations is unknown.
# Example: Guessing a random number until correct.
# Note: Ensure condition eventually becomes False to avoid infinite loops.

print("\n=== For Loop ===")
# For loop iterates over a sequence (e.g., range, list, string).
# Syntax: for variable in sequence:
# Range function: range(start, stop, step) - stop is excluded.
for x in range(11):  # Default start=0, step=1
    print(x)  # Print numbers 0 to 10
# Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print("\n=== Custom Range ===")
# Print double of numbers from 2 to 10.
for x in range(2, 11):  # Start=2, Stop=11, Step=1
    print(x * 2)
# Output: 4, 6, 8, 10, 12, 14, 16, 18, 20

print("\n=== Range with Step ===")
# Print double of even numbers from 2 to 10.
for x in range(2, 11, 2):  # Step=2 (skip every other number)
    print(x * 2)
# Output: 4, 8, 12, 16, 20

print("\n=== Reverse Range ===")
# Print double of numbers from 20 to 1.
for x in range(20, 0, -1):  # Step=-1 (decrement)
    print(x * 2)
# Output: 40, 38, 36, ..., 4, 2

print("\n=== Iterating Over Sequences ===")
# For loops can iterate over strings, lists, etc.
for i in "hello":  # Iterate over each character
    print(i)
# Output: h, e, l, l, o

print("\n=== Iterating Over a List ===")
# Iterate over a list directly.
nums = [1, 22, 34, 45, 67, 78]
for i in nums:
    print(i)
# Output: 1, 22, 34, 45, 67, 78

print("\n=== Iterating with Index ===")
# Use range(len(sequence)) to access indices and values.
nums = [1, 22, 34, 45, 67, 78]
for i in range(len(nums)):
    print("index:", i, "Value:", nums[i])
# Output:
# index: 0 Value: 1
# index: 1 Value: 22
# index: 2 Value: 34
# index: 3 Value: 45
# index: 4 Value: 67
# index: 5 Value: 78

print("\n=== Control Statements: Continue ===")
# Continue skips the current iteration and proceeds to the next.
for i in range(10):
    if i == 5:  # Skip when i is 5
        continue
    print(i)
# Output: 0, 1, 2, 3, 4, 6, 7, 8, 9

print("\n=== Control Statements: Break ===")
# Break exits the loop entirely.
for i in range(10):
    if i == 5:  # Exit loop when i is 5
        break
    print(i)
# Output: 0, 1, 2, 3, 4