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
#    b) # This is a comment : Answer
#    c) /* This is a comment */
#    d) <!-- This is a comment -->

# 2. Which of these is a valid variable name in Python?
#    a) 2myVar
#    b) my_var : Answer
#    c) my-var
#    d) my var

# 3. What is the output of?
print(type("5"))
#    a) <class 'float'>
#    b) <class 'int'> : Answer
#    c) <class 'str'>
#    d) <class 'bool'>

# 4. What will be the output of this code?
print(bool(100)+bool(-100) - bool("Hello"))
#    a) 1
#    b) 2
#    c) -1
#    d) Error : Answer

# 5. What is the output of this code?
myData = {1, True, 0 , False}
print(len(myData))
#    a) 4
#    b) 2 : Answer
#    c) 1
#    d) None

# 6. What is the output of this code?
x = 5
y = 3
print(x * y + x // y)
#    a) 18
#    b) 16
#    c) 17
#    d) 15 : Answer

# 7. What is the output of this code?
a = "Hello"
b = a.upper().replace("H", "J")
print(b)
#    a) JELLO: Answer
#    b) HELLO
#    c) Jello
#    d) hello


# 8. What is the output of this code?
x = 8
print(x << 2)
#     a) 32 : Answer
#     b) 2
#     c) 16
#     d) 4

# 9. What will be the output of this code?
a = 5
b = 10
print("A") if a > b else print("B") if a < b else print("Equal")
#     a) A
#     b) B: Answer
#     c) Equal
#     d) SyntaxError

# 10. Consider the following code: - Skip
x = 0
y = 10 if x else 20
print(y)
#     a) 10
#     b) 20
#     c) 0
#     d) None

# 11. What is the output of this code?
x = "Python"
print(x[1:4] + x[-2:])
#    a) ythno
#    b) ython : Answer
#    c) Pytn
#    d) ythn

# 12. What is the output of this code?
s = "  Welcome to Python  "
print(s.strip().count("o"))
#    a) 1
#    b) 2
#    c) 3: Answer
#    d) 0

# 13. What is the output of this code?
lst = [1, 2, 3]
lst.extend([lst.append(4), lst.append(5)])
print(lst)
#     a) [1, 2, 3, 4, 5]: Answer
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
#     d) 4 : Answer

# 15. Which of the following operations will raise an error?
#     a) s = {1, 2, [3, 4]} : Answer
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
#     d) IndexError  : Answer

# 17. Which of the following is a valid tuple operation?
#     a) t = (1, 2, 3); t[0] = 4
#     b) t = (1, 2, 3); t += (4,): Answer
#     c) t = (1, 2, 3); t.append(4) 
#     d) t = (1, 2, 3); t.remove(2)

# 18. What is the output of this code?
x = 5
y = 2
print(x ** y * 2 // 3 + x % y)
#     a) 17 : Answer
#     b) 16
#     c) 18
#     d) 15

# 19. What is the output of this code?
x = 20
y = x >> 2
print(y > 4 and x & 1 == 0)
#     a) True : Answer
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
#     d) TypeError : Answer

# 21. What is the output of this code combining multiple bitwise operations?
x = 13  
y = 6   
print((x & y) ^ (x | y))
#     a) 11 : Answer
#     b) 9
#     c) 7
#     d) 15

# 22. What is the output of this code?
a = "Python"
print(a.startswith("P") and a.endswith("n"))
#    a) True : Answer
#    b) False
#    c) Python
#    d) Error

# 23. What is the output of this code?
lst = [1, 2, 3, 4]
print(lst[2] * lst[-1] + lst[0])
#    a) 13 : Answer
#    b) 12
#    c) 10
#    d) 14

# 24.What is the output of this code?
s = {1, 2, 3}
t = (4, 5, 6)
d1 = {s: 1, t: 2}
d2 = {1: s, 2: t}
print(d1 , d2) 
#     a) {(1, 2, 3): 1, (4, 5, 6): 2} {1:(1, 2, 3), 2:(4, 5, 6)}  : Answer
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
#     c) (33, 4, 2) : Answer
#     d) TypeError

# 26. What is the output of this code with complex logical expressions?
a = 0
b = 5
c = -1
print(a or b and c or not a)
#     a) 5
#     b) -1
#     c) True : Answer
#     d) 0

# 27. What is the output of this code combining lists, sets, and operators?
lst = [1, 2, 2, 3, 4]
s = set(lst)
print(len(s) + (2 in s and 5 not in s))
#     a) 4
#     b) 3
#     c) 5 : Answer
#     d) 2

# 28. What is the primary purpose of the 'return' keyword in Python? - Skip
#    a) To exit a loop early
#    b) To skip the current iteration of a loop
#    c) To send a value back from a function to the caller
#    d) To terminate the entire program

# 29. What is the output of this code?
s = "Hello World"
print(s.split()[1].upper())
#    a) HELLO
#    b) WORLD : Answer
#    c) Hello
#    d) Error

# 30. What is the output of this code?
d = {1: "one", 2: "two"}
print(d.get(3, "three"))
#    a) one
#    b) two
#    c) three
#    d) Error: Answer


# 31.What is the output of this code?
x = "123"
y = int(x) + float("4.5")
print(type(y), y)
#    a) <class 'int'> 127
#    b) <class 'float'> 127.5 : Answer
#    c) <class 'str'> 1234.5
#    d) Error


# 32. What is the main purpose of the 'pass' keyword in Python? : Answer
#    a) To terminate a function and return a value
#    b) To act as a placeholder for future code without causing an error
#    c) To skip the current iteration of a loop
#    d) To break out of a loop entirely

# 33. What is the output of this code?
x = 7
y = 3
print(x // y + x % y * 2)
#    a) 5
#    b) 4 : Answer
#    c) 6
#    d) 3

# 34.What is the output of this code?
lst = [10, 20, 30, 40, 50]
print(lst[1:4][1] > 25 and lst[-1] == 50)
#    a) True : Answer
#    b) False
#    c) 30
#    d) Error

# 35. What is the output of this code? - Skip
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

# 36. What is the output of this code? - Skip
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

# 37.What is the output of this code? - Skip
t = (1, 2, 3, 4)
lst = [x * 2 for x in t if x % 2 == 1]
print(lst)
#    a) [2, 6]
#    b) [2, 4, 6, 8]
#    c) [1, 3]
#    d) Error : 

# 38. What is the output of this code?
a = ""
b = "Python"
c = "Code"
print(a or (b and len(c) > 2))
#    a) Python
#    b) Code
#    c) True : Answer
#    d) ""

# 39. What is the output of this code?
d = {"a": 1, "b": 2, "c": 3}
d1 = d.copy()
d1["a"] = 10
print(d["a"], d1["a"])
#    a) 1 10 : Answer
#    b) 10 1
#    c) 1 1
#    d) 10 10

# 40. What is the output of this code?
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1.intersection(s2) == s1 & s2)
#    a) True
#    b) False : Answer
#    c) {2, 3}
#    d) Error