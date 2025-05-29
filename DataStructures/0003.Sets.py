# Lists , Dictionary

#  Lists --[1,2,3,67,"Sting",True,23.45,67]
#  Lists[0]
# Dictionary={
# "key1":"value1",
# "key2":"value2",
# "key3":"value1"
# }

#  Unique elements -- 
mySet ={1,2,3,4,5,5,5,5}
print(len(mySet))
print(mySet)

# Unordered elements ,non-indexed 

# Unchangeable -- We can't modify the existing elements of the set but we can add or remove elements 

mySet.add(34)
print(mySet)

mySet2 = {"Apple","Orange","Kiwi"}
mySet.update(mySet2)
print(mySet)

#  remove -- If the item does not exist. remove will throw an error
# mySet2.remove("Kiwi")
# # mySet2.remove("Kiwi")
# print(mySet2)
# #  discard -- It will print nothing
# mySet2.discard("Orange")
# mySet2.discard("Orange")
# print(mySet2)


# pop() -- It removes one random element evertytime
mySet.pop()
mySet.pop()
mySet.pop()
print(mySet)



# Clear()
# mySet.clear()
# print(mySet)


# del - to delete the set
# del mySet
# print(mySet)

# Set Operations 

mySetOne = {3,2,1,23,46,7,8,9,9,9,9}
mySetTwo = {30,12,46,7,80,10,9,9}

# Union of two sets -- Combining the sets 
# Every element will only come once and each and every element will come

mySet3 = mySetOne.union(mySetTwo)
# mySet3 = mySetOne.union(mySetTwo,mySet,mySet5)
# mySet3 = mySetOne | mySetTwo | mySet
print(mySet3)

# Intersection -- this only allows common elements 
mySet4 = mySetOne.intersection(mySetTwo)
# mySet4 = mySetOne & mySetTwo & mySet
print(mySet4)

# 1 - 0 , True ,False 

mySet6 = {1,0}
print("With 0, 1 only:", mySet6)

# True - 1 False - 0
mySet7 = {1,True,0}
print("With 0, 1 , true only:", mySet7)

mySet8 = {1,True,0,False}
print("With 0, 1 , true , False:", mySet8)

mySet9 = {True,False}
print("With True, False only:", mySet9)


mySet10 = {True,1,0}
print("With 0, 1 , true only:", mySet10)

mySet11 = {True,1.0,0.0}
print("With 0, 1 , true only:", mySet11)
