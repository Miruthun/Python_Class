# Recursion -- A function calling itself.

# Iterative -- Loops 

# Recursive -- functions


# A function can be called from anywhere. 

# def Second():
#     print("Hello Second")

# def First():
#     print("Hello First")
#     Second()
#     print("Completed")

# For a code inside function to execute we have to call a function atleast once.
# First()


#  A function can be called as many times as we need.
# First() 
# First()


# 

# def PrintNumbers():
#     print("Started")
#     Print1()

# def Print1():
#     print("1")
#     Print2()

# def Print2():
#     Print3()
#     Print4()
#     print("2")

# def Print3():
#     print("3")

# def Print4():
#     print("4")


# print("Let's See the Output")
# PrintNumbers()
# print("Task Completed")


#  A function can call itself. Recursion

# Print 1-5

# for i in range(1,6):
#     print(i , end=" ")

# print()

# def PrintNumbers(n):
#     # Base condition
#     if n > 5:
#         return 
#     print(n , end = " ")

#     # Function Call
#     PrintNumbers(n+1)

# PrintNumbers(1)

# 5-1 --- Print

for i in range(5,0,-1):
    print(i, end=" ")

print()
# def PrintNumbers(n):
#     # Base condition
#     if n <= 0:
#         return 
#     print(n , end = " ")

#     # Function Call
#     PrintNumbers(n-1)

# PrintNumbers(5)

def PrintNumbers(n):
    # Base condition
    if n > 5:
        return 

    # Function Call
    PrintNumbers(n+1)
    print(n , end = " ")

PrintNumbers(1)
