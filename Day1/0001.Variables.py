# Data Types - 
# Python is a dynamically typed language.
x = "Miruthun"
print(type(x))
x = 200
print(type(x))
x = True
print(type(x))
x = 400.56
print(type(x))

# Data types - 
# Basic Data Types - Built in Data Types:
    # int -- Number wihtout decimal - 300 , 2 , -100, 0,34
y = 200
print(y)
print(400)

    # float -- Number with decimal -- 30.56,40.46, -123.789,0.0,34.0
f = 100.34
print(f)
print(100.56)

    # string -- "Hello" , 'Miruthun',"Anything,"123"
name = "New York"
print(name)
print("India")
    # Boolean -- True (on -- 1) and False (off -- 0)

flag = True 
NoFlag = False 
print(Flag)
print(True)
    # Complex Numbers


# Can we convert one type to another ? -- yes 

# Type Casting - Type Coversion
# int to float --- float()
u = 100
print(type(u))
print(u)

t = float(u)
print(type(t))
print(t)

# float to int -- int()
i = 100.456
print(type(i))
print(i)

s = int(i)
print(type(s))
print(s)

# string to int 

name = "hello"      # THis will cause an error
name ="123"
print(type(name))

y = int(name)
print(y)

# int/float -- string 

g = 1000
# print(1000+"Hello")       # This will throw an error
print(str(1000)+"Hello")

# Boolean 
flag = True
print(int(flag))

# True - Any number (+ve / -ve ) except 0 , Any string will be considered as true
# False - 0, ""

x = bool(1000)
print(int(x))

print(int(bool(1000)) + int(bool(-1000)))

print(bool("Hello"))

# Data Type range - Every data type has a Max and MIN value 
# import sys
# print(sys.maxsize)
# print(-sys.maxsize-1)

# print(sys.float_info.max)
# print(sys.float_info.min)
# print(-sys.float_info.max)

