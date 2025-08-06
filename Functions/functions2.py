# -----------------------------------------------
# Functions in Python: Input Parameters and Return
# -----------------------------------------------

# ✅ Category 1: No Parameters, No Return
def add_numbers_fixed():
    a = 100
    b = 300
    print("Sum (fixed values):", a + b)

add_numbers_fixed()

# ✅ Category 2: With Parameters, No Return
def add_numbers(a, b):
    print("Sum (with parameters):", a + b)

add_numbers(200, 300)
add_numbers(-200, 3002)

# ✅ Category 3: With Parameters, With Return
# return → Used to send back a result and end the function
def add_and_return(a, b):
    result = a + b
    print("Result (inside function):", result)
    return result  # Function ends here

# Calling the function and storing the result
result = add_and_return(200, 300)
print("Result (outside function):", result + 100)

# ✅ Category 4: Without Parameters, With Return
def add_and_return_fixed():
    a = 100
    b = 300
    return a + b

x = add_and_return_fixed()
print("Sum (returned from no-param function):", x)

# -------------------------
# Return Keyword
# -------------------------
def greet():
    return "Hello World"
    print("This line will NOT be executed.")  # Dead code

message = greet()
print("Greeting:", message)

# -------------------------
# Next Topics
# -------------------------
# - Recursion 
# - Call Stack 
# Coding examples using functions

