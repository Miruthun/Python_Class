# Data Types : Numeric - Int , Float -- 20 , 30.45

# strings - "Something"
# Boolean - True , False 

# List , Tuples , Sets , Dictionary - Advanced Data Types / Data Structures

# List -- It is a data type which can store multiple values under one name 

x = 30
x = 40 
print(x)

myList = []             # An empty list

myList2 = [2,3,4,5,6,7,8]       # Non-empty list
# We can mix different types of values / Data types 
myList3 = ["Hello",39, 30.45, True, 1234]

# How to find number of elements inside a list.
print(len(myList))
print(len(myList2))

# Lists are index based data structures 

# [2,   3,      4,      5 ,     6,      7,      8]
# 0     1       2       3       4       5       6

# Negative Indexing
# -7  -6     -5      -4       -3     -2      -1
# We can add and remove elements dynamically 
# CRUD -- Create READ UPDATE DELETE
# CREATE - Creating / Initializing a list
myList2 = [2,3,4,5,6,7,8,45]

myList2 = [2,3,4,5,6,7,8,45]
#myList3 = ["Hello",39, 30.45, True, 1234]
# Adding a new element to the list . The element will be added at the last index always.
myList2.append(1234)
print(myList2)

# Insert -- we can insert an element at any specific index
myList2.insert(2,3456)
print(myList2)

# extend -- When we want to add a list to list / tuple /set.
myList2.extend(myList3)
print(myList2)


# READ - Reading / accessing a particular value from the list
print(myList2[5])
print("Negative Index:",myList2[-2])
# How to print the first element -
print("First Element: ",myList2[0])

# How to print the last element
print("Last Element: ",myList2[len(myList2)-1])

# Printing the complete list
print(myList2)

# UPDATE - Changing the existing value
myList2[4]= "Hello"
print(myList2)

# myList2[8]="New"

# DELETE - Deleting an updated value
# pop() it removes the last element. -- Returns the last element

print(myList2.pop())
print(myList2)

# Remove() -- It removes a particular element from the list. 
myList2.remove(5)
print(myList2)

# del myList2     # Deleteing the complete list
# print(myList2)


# Clear() --- To empty a list
# myList2.clear()
# print(myList2)

# Slicing -- making smaller lists fromh the a given list
# [start:end].  -- Indexes. -- End is excluded (0-3) -- 0 ,1 2 
print(myList2[:])

print(myList2[0:])
print(myList2[:len(myList2)])

print(myList2[2:6])         # 2 , 3 , 4, 5

# Start < End
print(myList2[-4:-1])

