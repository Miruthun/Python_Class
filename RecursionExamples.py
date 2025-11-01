# Recursion -- Analogy  -- 

# Loops -- Iterative 
# funbctions -- Recursive 


# Task : Add all the numbers from 1 to 10 
#  Iterative 
"""
result = 0 
for i in range(1,11):
    result+=i
print(result)
"""
"""
result = 0 
for i in range(10,0,-1):
    result+=i
print(result)
"""

# Recursive 
# 1 + (2)
#  1 + 2 + (3)
#  1 + 2 + 3 + (4)

#  1 + 2 + 3 +4 +5 + 6 +7 +8 + 9 + 10
"""
def SumNumbers(n):
    if n == 10:
        return n
    result = 0
    result += n  + SumNumbers(n+1)
    return result 
print(SumNumbers(1))
"""
"""
def SumNumbers(n):
    if n == 1:
        return n
    result = 0
    result += n  + SumNumbers(n-1)
    return result 
print(SumNumbers(10))
"""

# Factorial: 

# 1 ! = 1 
# 2!  = 2 *1 = 2 
# 3! = 3 *2*1 = 6 

# 6! = 6*5*4*3*2*1 = 720 

# Recursive 

"""
def Fact(n):
    ft = 0
    if n ==0 or n ==1:
        return 1 
    if n < 0:
        return -1 
    ft = n* Fact(n-1)
    return ft 

print(Fact(6))
"""

# Fibonacci Series : 
"""
0  1  1  2  3  5  8  13  . . . . 

1  2  3  4  5  6  7  8 . . . . .
"""
"""
def Fib(n):
    if n ==1:
        return 0 
    if n==2 or n ==3:
        return 1 
    result = 0
    result = Fib(n-1) + Fib(n-2)

    return result 

print(Fib(8))
"""

#  0 1 1 2 4 7 13 . . . . . .
"""
def Trib(n):
    if n ==1 :
        return 0
    if n ==2 or n==3:
        return 1
    result = 0 
    result = Trib(n-1) + Trib(n-2) + Trib(n-3)
    return result 

print(Trib(5))
"""

