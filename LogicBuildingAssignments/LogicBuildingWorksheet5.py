# 1.
'''
list1 = [1,2,3,4,5]
def sum():
    sum=0
    for i in list1:
        sum+=i
    return sum
print(sum())
'''
# 2.
'''
list2 = [1,2,1,1,1,1]
def even():
    for i in list2:
        if i%2 == 0:
            print("Yes, there is 1 or more even numbers in this list")
            break
        else:
            continue
even()
'''
# 3.
'''
usernum = int(input("Enter num:"))
list3 = [1,3,5,789,43,3546]
def numAdd():
    if usernum > 0:
        list3.append(usernum)
        print("New list:", list3)
    else:
        print("This is a negative number, please try again.")
numAdd()
'''
# 4.
'''
list4 = [1,12,123,123,567,345,1007,56756,0]
def maxVal():
    maxnum = 0
    for i in list4:
        if i > maxnum:
            maxnum=i
            continue
        else:
            continue
    return maxnum
print(maxVal())
'''
# 5.
'''
list5 = [1,2,3,45,67,10,11,435,9,10.7]
def counterOver10():
    counter = 0
    for i in list5:
        if i > 10:
            counter+=1
        else:
            continue
    return counter
print(counterOver10())
'''
# 6.
'''
list6 = [1,2,67,983,4,7,8,9,10,12]
def reverseList():
    for i in range(1,((len(list6))+1)):
        print(list6[-i])
reverseList()
'''
# 7.
'''
list7 = [1,3,88,5,7,9,12]
list7Copy = []
def oddRemove():
    for i in list7:
        if i%2 == 0:
            list7Copy.append(i)
    return list7Copy
print(oddRemove())
'''
# 8.
'''
list8 = [1,-98,2,3,4,5,10,11]
list8Doubled = []
def double():
    for i in list8:
        list8Doubled.append(i*2)
    return list8Doubled
print(double())
'''
# 9.
'''
list9 = []
def emptyCheck():
    if len(list9) == 0:
        print("Empty list")
    else:
        print("Not empty list")
emptyCheck()
'''
# 10.
'''
usernum = int(input("Enter num"))
list10 = [1,3,5,65,78,344]
def numFind():
    if usernum in list10:
        print(list10.index(usernum))
    else:
        print("Entered number is not in list")
numFind()
'''
# 11.
'''
list11A = [1,23,34,56,56,6857]
list11B = [86,56,374,2094,840]
def mergeLists():
    for i in list11B:
        list11A.append(i)
    return list11A
print(mergeLists())
'''
# 12.
'''
listnorm = [1,2,7,3,9,4]
def listSort():
    for i in range(len(listnorm)):
        x=0
        for i in listnorm:
            if i > x:
                x=i
        print(x,end = ', ')
        listnorm.remove(x)
listSort()
'''
#13.***
'''
listDup = [1,2,2,3,5,8,2]
def listDupCount():
    counter = 0
    x=0
    for i in listDup:
        if i in listDup:
            counter+=1
    print(counter)
listDupCount()
'''

# 14.
'''
list_3 = [1,2,3,4,5,6,7,8,9]
def Div3List():
    for i in list_3:
        if i%3 == 0:
            print(i)
        
Div3List()
'''

# 15.
'''
list_neg = [-3,-2,-1,0,1,2,3]
list_new = []
def Positifier():
    for i in list_neg:
        if i < 0:
            list_new.append(0)
        else:
            list_new.append(i)
    print(list_new)
Positifier()
'''

# 16.
'''
tuple = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def tupleLen():
    return len(tuple)
print(tupleLen())
'''

# 17.
'''
tuple_reused = (1,2,3,4,5,7,7,5,4,3,5,3,2)
usernum = int(input("Enter num: "))
def userNumChecker():
    if usernum in tuple_reused:
        print("Yes, your num exists in tuple.")
    else:
        print("not found")
userNumChecker()
'''

# 18.
'''
tuple_reused2 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def tupleSumCount():
    x=0
    for i in tuple_reused2:
        x+=i
    return x
print(tupleSumCount())
'''

# 19.
'''
tuple_reused3 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def FiveFinder():
    count = 0
    for i in tuple_reused3:
        if i == 5:
            count+=1
        else:
            continue
    return count
print(FiveFinder())
'''

# 20.
'''
tuple_reused4 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def fstLastTpleElmnts():
    list0 = []
    list0.append(tuple_reused4[0])
    list0.append(tuple_reused4[-1])
    return list0
print(fstLastTpleElmnts())
'''

# 21.
'''
def concatenator():
    tuple_reused4 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
    tuple_part2 = (1,2,34,5,6,4,6,4,5,4,4,3,)
    tuplenew = tuple_reused4 + tuple_part2
    return tuplenew
print(concatenator())
'''

# 22.
'''
tuple_reused5 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def posCheck():
    for i in tuple_reused4:
        if i < 0:
            print("Negative num found")
            break
        else:
            continue
posCheck()
'''

# 23.
'''
tuple_reused6 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def limitTuple():
    userNum = int(input("Enter num: "))
    list_t = []
    for i in tuple_reused6:
        if i > userNum:
            list_t.append(i)
        else: 
            continue
    return tuple(list_t)
print(limitTuple())
'''

# 24.
'''
tuple_reused7 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def minTuple():
    x = 100
    for i in tuple_reused7:
        if i < x:
            x=i
        else:
            continue
    return x
print(minTuple())
'''

# 25.
'''
tuple_reused8 = (1,2,3,4,5,7,7,5,4,3,5,3,2)
def reverse():
    list_R = []
    list_R = tuple_reused8[::-1]
    return list_R
print(reverse())
'''

# 26.
'''
def setAdd():
    usernum = int(input("Enter num: "))
    set1 = {1,2,3,5,6,7,7,432,2}
    set1.add(usernum)
    print(set1)
setAdd()
'''

# 27.

set2 = {1,2,3,5,6,7,7,432,2}
set2Dupe = {1,2,3}
if set2Dupe in set2:
    print("")
