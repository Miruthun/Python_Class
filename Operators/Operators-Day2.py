# Comparision Operators -- These operators always return the result as True or False 
# print(30+40)

#  Becuase of booolean type return these are used in contions (if , elif)

# == -- Equal to 
print("Equal to ---------------")
print(3==3)
print(3==5)

# != -- Not equal to 
print("Not Equal to ---------------")
print(3!=5)
print(3!=3)

# Logical Operator -- to combine multiple conditions --- These operators always return the result as True or False 
#  Becuase of booolean type return these are used in contions (if , elif)
print("Logical Operators ---------------")
# print(3 > 5)

# AND OR NOT 

# Truth Table 

'''
AND Operator Truth Table:
True and True   ---> True   ---> Case 1
True and False  ---> False  ---> Case 2 
False and True  ---> False  ---> Case 3 
False and False ---> False  ---> Case 4
'''
print("-------- And Operator --------------")
print(3<5 and 3 >2)         #Case 1 
print(3 < 5 and 3 < 2)      #Case 2
print(3>5 and 3 > 2)        #Case 3 
print(3 >5 and 3 < 2)       #Case 4 

'''
Or Operator Truth table:

True or True    ---> True     ---> Case 1 
True or False   ---> True     ---> Case 2
False or True   ---> True     ---> Case 3
False or False  ---> False    ---> Case 4

'''

print("------ Or Operator ----------")

print(3<5 or 3 >2)    # Case 1 
print(3 < 5 or 3 <2)  # Case 2
print(3>5 or 3 >2)    # Case 3
print(3 > 5 or 3<2)   # Case 4

# Not Operator -- It toggles the result -- true will be converted to flase and vice-versa.

print("------ Not Operator ----------")
print(not(True))
print(not(False))
print(not(3<5 or 3 >2))
print(not(3 > 5 or 3<2))


# Python Identity Opertors -- to compare two or more objects (List , Sets , Tuple , Dictionary)
#  is , is not 
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
list3 = [4,6,7,8,9]
list4 = list1
list2[0] = 123
list3[0] = 103
list4[0]= 105
# print(list1)
# print(list2)
# print(list3)
# print(list4)
#  list5 = list1.copy()
print("------ Identity Operator ----------")
print(list1 is list2)
print(list1 is list3)
print(list1 is list4)
print("--- ")
print(list1 is not list2)
print(list1 is not list3)
print(list1 is not list4)

# Python Memebership Operators 
print("------ Memebership Operator ----------")
# list1 = [1,2,3,4,5]
print(5 in list1)
print(51 in list1)

print(5 not in list1)
print(51 not in list1)


#  Bitwise Operators -- bits 
#  Computer understand -- Binary Langauage -- Bi - two -- 0 1 
#  Bits -- 0 1 

# 5 -- 101 

#  Decimal Number -- 0-9 
#  Binary Number -- 00101010

# 5 -- 

'''
1 2 4 8 16 32 64 128 .....
. . . 16      8     4     2     1 
                    1     0     1 
                    
12 -->  8+4 
              1     1     0     0 

45 -- 32 + 8 + 4 + 1  
1 0 1 1 0 1 
'''

'''
Bitwise : 3 any bitwise operator 5
011 101
'''
