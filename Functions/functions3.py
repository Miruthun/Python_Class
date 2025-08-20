# Sum of all the elements in a list 

# def SumOfList(myList):
#     total = 0 
#     for i in myList:
#         total+=i 
    
#     return total

# myList = [12,23,43,25,16,37]
# print(SumOfList(myList))


# Product of all the elements of List

# def ProdOfList(myList):
#     total = 1

#     for i in myList:
#         total *=i 
    
#     return total

# myList = [12,23,43,25,16,37]
# print(ProdOfList(myList))


# Search for a specific element in a list

# def SearchElem(myList,elem):
#     for i in myList:
#         if i == elem:
#             return True 
             
#     return False 
# myList = [12,23,43,25,16,37]
# print(SearchElem(myList,431))

# myList = [12,23,43,25,16,37]
# if 43 in myList:
#     print("True")
# else:
#     print("False")



def SumOfThreeMulti():
    threeMultiples = 0
    for i in range(1,21):
        if i % 3 == 0:
            threeMultiples += i
        else: continue
        
    return threeMultiples
print(SumOfThreeMulti())

def Calculator(no1, no2, operator):
    if operator == "+":
        return no1 + no2
    elif operator == "-":
        return no1 - no2
    elif operator == "*":
        return no1 * no2
    elif operator == "/":
        return no1 / no2
print(Calculator(5,15,"/"))

def Calculator2():
    no1 = input("First Number")
    no2 = input("Second Number")
    operator = input("Operator")
    int_no1 = int(no1)
    int_no2 = int(no2)
    if operator == "+":
        return int_no1 + int_no2
    elif operator == "-":
        return int_no1 - int_no2
    elif operator == "*":
        return int_no1 * int_no2
    elif operator == "/":
        if int_no2 == 0:
            return "error"
        return int_no1 / int_no2

print(Calculator2())
