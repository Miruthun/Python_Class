"""
  _____       _   _                    _______ ______  _____ _______ 
 |  __ \     | | | |                  |__   __|  ____|/ ____|__   __|
 | |__) |   _| |_| |__   ___  _ __      | |  | |__  | (___    | |   
 |  ___/ | | | __| '_ \ / _ \| '_ \     | |  |  __|  \___ \   | |   
 | |   | |_| | |_| | | | (_) | | | |    | |  | |____ ____) |  | |   
 |_|    \__, |\__|_| |_|\___/|_| |_|    |_|  |______|_____/   |_|   
         __/ |                                                      
        |___/                                                       

"""
# 1. What is the correct way to write a comment in Python?
#    a) // This is a comment
#    b) # This is a comment
#    c) /* This is a comment */
#    d) <!-- This is a comment -->

# 2. Which of these is a valid variable name in Python?
#    a) 2myVar
#    b) my_var
#    c) my-var
#    d) my var

# 3. What is the output of?
print(type("5"))
#    a) <class 'float'>
#    b) <class 'int'>
#    c) <class 'str'>
#    d) <class 'bool'>

# 4. What will be the output of this code?
print(bool(100)+bool(-100) - bool("Hello"))
#    a) 1
#    b) 2
#    c) -1
#    d) Error

# 5. What is the output of this code?
myData = {1, True, 0 , False}
print(len(myData))
#    a) 4
#    b) 2
#    c) 1
#    d) None

# 6. How many times will "Hi" be printed in this code?
for i in range(3):
    print('Hi')
#    a) 2
#    b) 3
#    c) 4
#    d) 0

# 7. What is the output of this code?
i = 1
while i < 4:
    print(i)
    i += 1
#    a) 1 2 3
#    b) 1 2 3 4
#    c) 2 3 4
#    d) 1

# 8. What is the output of this code?
x = 8
print(x << 2)
#     a) 32
#     b) 2
#     c) 16
#     d) 4

# 9. What will be the output of this code?
a = 5
b = 10
print("A") if a > b else print("B") if a < b else print("Equal")
#     a) A
#     b) B
#     c) Equal
#     d) SyntaxError

# 10. Consider the following code:
x = 0
y = 10 if x else 20
print(y)
#     a) 10
#     b) 20
#     c) 0
#     d) None

# 11. What is the output of the following code?
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i, j, end=" ")
#     a) 0 1 0 2 1 0 1 2 2 0 2 1
#     b) 1 0 2 0 2 1
#     c) 0 1 0 2 1 0 2 0
#     d) 1 0 2 0

# 12. How many times will "Hello" be printed in this code?
i = 1
while i < 10:
    if i % 3 == 0:
        i += 1
        continue
    print("Hello")
    i += 2
#     a) 4
#     b) 5
#     c) 6
#     d) 7

# 13. What is the output of this code?
lst = [1, 2, 3]
lst.extend([lst.append(4), lst.append(5)])
print(lst)
#     a) [1, 2, 3, 4, 5]
#     b) [1, 2, 3, 4, 5, None, None]
#     c) [1, 2, 3, None, None, 4, 5]
#     d) Error


# 14. What is the output of this code?
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
print(len(s3))
#     a) 3
#     b) 6
#     c) 2
#     d) 4

# 15. Which of the following operations will raise an error?
#     a) s = {1, 2, [3, 4]}
#     b) s = {1, 2, 3}.add(4)
#     c) s = {1, 2, 3}.union({4, 5})
#     d) s = {1, 2, 3}.discard(4)

# 16. What is the output of this code?
t = (1, 2, [3, 4])
t[2][0] = 5
print(t)
#     a) (1, 2, [5, 4])
#     b) (1, 2, [3, 4])
#     c) TypeError
#     d) IndexError

# 17. Which of the following is a valid tuple operation?
#     a) t = (1, 2, 3); t[0] = 4
#     b) t = (1, 2, 3); t += (4,)
#     c) t = (1, 2, 3); t.append(4)
#     d) t = (1, 2, 3); t.remove(2)

# 18. What is the output of this code?
x = 5
y = 2
print(x ** y * 2 // 3 + x % y)
#     a) 17
#     b) 16
#     c) 18
#     d) 15

# 19. What is the output of this code?
x = 20
y = x >> 2
print(y > 4 and x & 1 == 0)
#     a) True
#     b) False
#     c) 5
#     d) Error

# 20. Operators: What is the result of this code?
x = 10
x += x > 5
print(x)
#     a) 10
#     b) 11
#     c) 9
#     d) TypeError

# 21. What is the output of this code combining multiple bitwise operations?
x = 13  
y = 6   
print((x & y) ^ (x | y))
#     a) 11
#     b) 9
#     c) 7
#     d) 15

# 22. What is the output of this recursive function?
def mystery(n):
    if n <= 1:
        return n
    return mystery(n - 1) + mystery(n - 2)
print(mystery(5))
#     a) 5
#     b) 10
#     c) 9
#     d) 11

# 23. How many times is the following recursive function called (including the initial call) for func(4)?
def func(n):
    if n <= 1:
        return n
    return func(n - 1) + func(n - 2)
func(4)
#     a) 5
#     b) 9
#     c) 7
#     d) 15

# 24.What is the output of this code?
s = {1, 2, 3}
t = (4, 5, 6)
d1 = {s: 1, t: 2}
d2 = {1: s, 2: t}
print(d1 , d2) 
#     a) {(1, 2, 3): 1, (4, 5, 6): 2} {1:(1, 2, 3), 2:(4, 5, 6)}  
#     b) TypeError: unhashable type: 'set'
#     c) {1: 1, 2: 2}
#     d) SyntaxError

# 25. What is the result of this code?
lst = [1, 2, 6,33,4,2,1,3]
s = set(lst)
t = tuple(s)
print(t[3:7])
#     a) (4, 3, 6)
#     b) (2, 2, 3)
#     c) (33, 4, 2)
#     d) TypeError

# 26. What is the output of this code with complex logical expressions?
a = 0
b = 5
c = -1
print(a or b and c or not a)
#     a) 5
#     b) -1
#     c) True
#     d) 0

# 27. What is the output of this code combining lists, sets, and operators?
lst = [1, 2, 2, 3, 4]
s = set(lst)
print(len(s) + (2 in s and 5 not in s))
#     a) 4
#     b) 3
#     c) 5
#     d) 2

# 28. What is the primary purpose of the 'return' keyword in Python?
#    a) To exit a loop early
#    b) To skip the current iteration of a loop
#    c) To send a value back from a function to the caller
#    d) To terminate the entire program

# 29. What is the output of this code?
def check_loop():
    for i in range(1, 6):
        if i % 2 == 0:
            continue
        print(i, end=" ")
check_loop()
#    a) 1 2 3 4 5
#    b) 1 3 5
#    c) 2 4
#    d) Error

# 30. What is the output of this code?
def test_break():
    i = 1
    while i <= 10:
        if i > 3:
            break
        print(i, end=" ")
        i += 1
test_break()
#    a) 1 2 3 4 5 6 7 8 9 10
#    b) 1 2 3
#    c) 1 2 3 4
#    d) Error

# 31.What is the output of this code?
x = "123"
y = int(x) + float("4.5")
print(type(y), y)
#    a) <class 'int'> 127
#    b) <class 'float'> 127.5
#    c) <class 'str'> 1234.5
#    d) Error


# 32. What is the main purpose of the 'pass' keyword in Python?
#    a) To terminate a function and return a value
#    b) To act as a placeholder for future code without causing an error
#    c) To skip the current iteration of a loop
#    d) To break out of a loop entirely

# 33. What is the output of this code?
def calculate(a, b):
    if a > b:
        return a - b
    return a + b
print(calculate(5, 8))
#    a) 13
#    b) -3
#    c) 3
#    d) Error

# 34.What is the output of this code?
lst = [10, 20, 30, 40, 50]
print(lst[1:4][1] > 25 and lst[-1] == 50)
#    a) True
#    b) False
#    c) 30
#    d) Error

# 35. What is the output of this code?
x = 9  
y = 5  
if x & y == 1:
    print(x ^ y)
else:
    print(x | y)
#    a) 12
#    b) 13
#    c) 1
#    d) 5

# 36. What is the output of this code?
s = {1, 2, 3, 4}
total = 0
for x in s:
    if x % 2 == 0:
        total += x
print(total)
#    a) 6
#    b) 10
#    c) 4
#    d) 0

# 37.What is the output of this code?
t = (1, 2, 3, 4)
lst = [x * 2 for x in t if x % 2 == 1]
print(lst)
#    a) [2, 6]
#    b) [2, 4, 6, 8]
#    c) [1, 3]
#    d) Error

# 38. What is the output of this code?
a = ""
b = "Python"
c = "Code"
print(a or (b and len(c) > 2))
#    a) Python
#    b) Code
#    c) True
#    d) ""
