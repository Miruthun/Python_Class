'''
# Functions - A block of code
# A function is a reusable block of code that performs a specific task. It helps in organizing code, 
# reducing repetition, and making the program easier to understand and maintain.
# Functions are defined using the 'def' keyword, followed by the function name and parentheses.
# They can take parameters (inputs) and can return values.

# How functions are called:
# To execute a function, you simply write its name followed by parentheses. This is called "calling" or "invoking" the function.
# When a function is called, the control jumps to the function's code, executes it, and then returns to the point where it was called.

# How one function can call another function:
# Functions can call other functions inside their body. This is known as nesting function calls.
# When one function calls another, the calling function pauses, the called function executes, and then control returns back.
# Example below: The 'First' function calls the 'Second' function inside it.
'''
def Second():
    print("Second")
  
def First():
    print("First")
    Second()  # Here, First calls Second

First()  # Calling the First function, which in turn calls Second
# Output: 
# First
# Second

'''
# Recursion is a mechanism/algorithm in which a function calls itself.
# Recursion allows a function to solve a problem by breaking it down into smaller, similar sub-problems.
# It requires a base case (condition to stop recursion) to prevent infinite calls, which would lead to a stack overflow.
# Without a base case, recursion would continue forever.
# Recursion is useful for problems like tree traversals, factorials, or printing sequences in a specific order.

'''
# Example of recursion: Printing numbers from 1 to 5.
# The function calls itself with n+1 until n > 5 (base case), then stops.
def PrintNumber(n):
    if n > 5:  # Base case: Stop when n exceeds 5
        return 
    print(n)  # Print current n
    PrintNumber(n+1)  # Recursive call with next number

PrintNumber(1)  # Start recursion from 1
# Output:
# 1
# 2
# 3
# 4
# 5

'''
# Iterative vs Recursive approaches:
# Iterative approach uses loops (like for or while) to repeat actions. It's straightforward and efficient in terms of memory.
# Recursive approach uses function calls instead of loops. It can be more elegant for certain problems but may use more memory due to the call stack.

# Example: Summing numbers from 1 to 10 (though code snippets focus on printing, concept is similar).
# Iterative way: Go to each and every number and add it to the result (using a loop).
# Recursive way: You add one number and leave the rest to the "friend" (recursive call).
# Like: 1 + Function(2), which becomes 1 + 2 + Function(3), and so on.
'''
# Iterative example: Printing table of 2 from 1 to 10 using a for loop.
for i in range(1, 11):
    print(2 * i, end=" ")  # Iterative: Loop through each i and print
print()  # New line
# Output: 2 4 6 8 10 12 14 16 18 20 

# Recursive example: Printing table of 2 from 1 to 10 using recursion.
def Printtable(n):
    if n > 10:  # Base case: Stop when n exceeds 10
        return 
    print(2 * n, end=" ")  # Print current multiple
    Printtable(n + 1)  # Recursive call for next number

Printtable(1)  # Start from 1
# Note: print() for new line is not in the function, but output would be: 2 4 6 8 10 12 14 16 18 20
# (You may need to add a print() after calling if running in script)

# Return keyword:
# The 'return' statement is used to exit a function and send a value back to the caller.
# Code after return in a function is not executed.
# Functions can have multiple return statements, but only one executes per call.
# If no return, the function returns None by default.

# Example:
def Add(a, b):
    # print(a + b)  # If uncommented, would print but not return
    result = a + b
    return result  # Return the sum to the caller
    # print("After Return")  # This won't execute

x = Add(20, 30)  # Call and store returned value
print(x)  # Output: 50
print(Add(30, 40))  # Direct print of returned value: 70
# print(result)  # Error: result is local to the function, not accessible outside

'''
# Call Stack (Stack Frame):
# The call stack is a data structure that manages function calls. Each call adds a "frame" to the stack.
# When a function returns, its frame is popped off.
# In recursion, multiple frames build up until the base case, then unwind (pop) while executing remaining code.
# This is why recursion can cause stack overflow if too deep (too many frames).

'''
# Example using the reverse printing recursion:
def PrintNumber(n):
    if n > 5:
        return 
    PrintNumber(n + 1)  # Recursive call first
    print(n)  # Print after recursion (during unwind)

PrintNumber(1)
# Output:
# 5
# 4
# 3
# 2
# 1

# Call stack explanation with diagram (ASCII art):
# When PrintNumber(1) is called:
# Stack: [PrintNumber(1)]
#   Calls PrintNumber(2) -> Stack: [PrintNumber(1), PrintNumber(2)]
#     Calls PrintNumber(3) -> Stack: [PrintNumber(1), PrintNumber(2), PrintNumber(3)]
#       Calls PrintNumber(4) -> Stack: [PrintNumber(1), PrintNumber(2), PrintNumber(3), PrintNumber(4)]
#         Calls PrintNumber(5) -> Stack: [PrintNumber(1), PrintNumber(2), PrintNumber(3), PrintNumber(4), PrintNumber(5)]
#           Calls PrintNumber(6) -> Stack: [PrintNumber(1), PrintNumber(2), PrintNumber(3), PrintNumber(4), PrintNumber(5), PrintNumber(6)]
#             n=6 >5, return (pop PrintNumber(6))
#           Now print(5) in PrintNumber(5), then return (pop)
#         Now print(4) in PrintNumber(4), then return (pop)
#       Now print(3) in PrintNumber(3), then return (pop)
#     Now print(2) in PrintNumber(2), then return (pop)
#   Now print(1) in PrintNumber(1), then return (pop)
# Stack empty.

# Diagram (simplified stack growth and unwind):
# Initial call: PrintNumber(1)
# 
# Stack builds up:
# +-----------------+
# | PrintNumber(6)  |  <- Top (returns first, no print)
# +-----------------+
# | PrintNumber(5)  |
# +-----------------+
# | PrintNumber(4)  |
# +-----------------+
# | PrintNumber(3)  |
# +-----------------+
# | PrintNumber(2)  |
# +-----------------+
# | PrintNumber(1)  |  <- Bottom
# +-----------------+
# 
# Unwind (pop and print):
# Pop 6: no print
# Pop 5: print 5
# Pop 4: print 4
# Pop 3: print 3
# Pop 2: print 2
# Pop 1: print 1

# Actual code for the reverse printing example:
def PrintNumber(n):
    if n > 5:
        return 
    PrintNumber(n + 1)  # Recursive call first (build stack)
    print(n)  # Print during unwind

PrintNumber(1)  # Call to start
