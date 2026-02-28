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
#13.
'''
listDup = [1,2,2,3,3,5,8,2]
def listDupCount():
    duplicates = {}
    for i in listDup:
        if i in duplicates:
            duplicates[i] +=1
        else:
            duplicates[i] = 1
    duplicates2 = duplicates.copy()
    for item in duplicates:
        if duplicates[item] < 2:
            del duplicates2[item]
    print(duplicates2)
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
'''
def subsetCheck():
    set2 = {1,2,3,5,6,7,7,432,2}
    set2Dupe = {2323}
    if set2Dupe.issubset(set2):
        print("Yes, subset found")
    else: 
        print("No, subset not found")
subsetCheck()
'''

# 28.
'''
set1 = {1,2,3,4,5,7,7,5,4,3,5,3,2}
set1Dupe = {10,11,12,13,14,999,99909}
def SetUnion():
    UnionSets1 = set1 | set1Dupe
    return UnionSets1
print(SetUnion())
'''

# 29.
'''
set1 = {1,23,4,5,77,5,4,3,53,2}
def elemSort():
    for i in set1:
        if i < 10:
            continue
        else:
            print(i)
elemSort()
'''

# 30.
'''
set1 = {1,2,3,4,5,7,7,5,4,3,5,3,2}
set1Dupe = {1,11,2,13,4,999,99909}
def setInter():
    Interset = set1 & set1Dupe
    return Interset
print(setInter())
'''

# 31.
'''
set31 = {1,4,8,10,14,17,21}
def setLen():
    return len(set31)
print(setLen())
'''

# 32.
'''
set0 = {1}
def set0check():
    if len(set0) == 0:
        print("Empty Set")
    else:
        print("Set not empty")
set0check()
'''

# 33. 
'''
set1 = {1,2,3,4,5,7,7,5,4,3,5,3,2}
set1Dupe = {10,2,11,12,13,14,999,99909}
def commonSet():
    common = set1.intersection(set1Dupe)
    return common
print(commonSet())
'''

# 34. 
'''
set1 = {1,2,3,4,5,7,7,5,4,3,5,3,2}
usernum = int(input("Enter num: "))
def numcheck():
    if usernum in set1:
        print("Yes, num in set")
    else:
        print("No, num not in set")
numcheck()
'''

# 35.
'''
set1 = {1,2,3,4,5,7,7,5,4,3,5,3}
set1Dupe = {10,2,11,12,13,14,999,99909}
def setsDiff():
    diff = set1.union(set1Dupe)
    return diff
print(setsDiff())
'''

# 36.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":109.98
}
UserKey = input("Enter Key: ")
def valFinder():
    return dict1[UserKey]
print(valFinder())
'''

# 37.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":109.98
}
def KeyCheck():
    if "Key5" in dict1:
        print("Key Found")
    else:
        print("Key Not Found")
KeyCheck()
'''

# 38.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":109.98
}
def KeyAdd():
    if "Key5" in dict1:
        print("Key Found")
    else:
        dict1["Key5"] = 3.141592
        print(dict1)
KeyAdd()
'''

# 39.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":109.98
}
def DictValSum():
    valSet = dict1.values()
    valSum = 0
    for i in valSet:
        valSum +=i
    print(valSum)
DictValSum()
'''

# 40.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":109.98
}
def valCheck():
    dictVals = dict1.values()
    count = 0
    for i in dictVals:
        if i > 50:
            count+=1
    print(count)
valCheck()
'''

# 41.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":109.98
}
def KeyReturn():
    keys = dict1.keys()
    listKeys = list(keys)
    return listKeys
print(KeyReturn())
'''

# 42.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def negChecker():
    for key in dict1:
        if dict1[key] < 0:
            dict1[key] *= -1
    return dict1
print(negChecker())
'''

# 43.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
dict2 = {
    "Key5":10,
    "Key3":1098,
    "Key7":1762543,
    "Key8":-109.98
}
def dictmerge():
    return dict1 | dict2
print(dictmerge())
'''

# 44.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
userKey = input("Enter Key: ")
def KeyDel():
    del dict1[userKey]
    return dict1
print(KeyDel())
'''

# 45. 
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def maxKeyVal():
    maxvallist = [0]
    maxkeylist = ["key"]
    for key in dict1:
        if int(dict1[key]) > int(maxvallist[0]):
            maxvallist[0] = dict1[key]
            maxkeylist[0] = key
        else: continue
    print(maxkeylist[0])
maxKeyVal()
'''

# 46. 
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def dictValSq():
    keys = dict1.keys()
    values = list(dict1.values())
    for k in range(0,len(values)):
        values[k] *= values[k]
    print(values)
dictValSq()
'''

# 47.
'''
 dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
    }
    def valstrCheck():
    vals = dict1.values()
    for i in vals:
        if i == str:
            continue
        else: 
            print("Not all values are strs")
            break
valstrCheck()
'''

# 48.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def Counter():
    counter = 0
    for keys in dict1:
        counter+=1
    print(counter)
Counter()
'''

# 49.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def dictswap():
    keys = dict1.keys()
    vals = dict1.values()
    print(dict(zip(vals,keys)))
dictswap()
'''

# 50. 
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def dictFilter():
    for key in dict1:
        dict2 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
        if dict2.get(key) > 0:
            continue
        else: 
            del dict2[key]
    return dict2
print(dictFilter())
'''

# 51.
'''
list1 = [1,2,3,4,5,6,7,8,9,0]
usernum = int(input("Enter num: "))
def listAppend():
    if usernum > 0:
        list1.append(usernum)
    else: 
        print("Error")
    print(list1)
listAppend()
'''

# 54.
'''
list1 = [1,2,3,4,5,6,7,8,9,0]
def listpop():
    list1.pop()
    print(list1)
listpop()
'''

# 53.
'''
list1 = [1,2,3,4,6,5,7,8,9,0]
def MultiCheck():
    list1Ord = list1.sort()
    if len(list1Ord) > 3:
        print(list1Ord, "len is > 3")
    else:
        print(list1Ord, "Len <= 3")
'''

# 54.
'''
list1 = [1,2,3,4,5,6,7,6,8,9,0]
usernum = int(input("Enter num"))
def userCount():
    counter = 0
    for i in list1:
        if i is usernum:
            counter+=1
        else:
            continue
    return counter
print(userCount())
'''

#55.
'''
list2 = [1,2,3]
list2b = [5,8,11]
def extender():
    list2.extend(list2b)
    if len(list2) > 5:
        return list2
    else:
        return None
print(extender())
'''

# 56.
'''
tuple1 = (1,2,3,4,5,6,7,8,990)
def userPos(a):
    if a in tuple1:
        return tuple1.index(a)
    else:
        return -1
print(userPos(6))
'''

# 57.
'''
tuple1 = (0,1,2,3,4,5,6,7,8,99,0)
def zeroCheck():
    counter = tuple1.count(0)
    if counter > 2:
        return True
    else:
        return False
print(zeroCheck())
'''

# 58.
'''
tuple1 = (1,2,3,4,5,6,7,8,990)
def tupleLen():
    length = len(tuple1)
    print(length, ": ", end = "")
    if length > 4:
        print("Long")
    else: 
        print("Short")
tupleLen()
'''

# 59.
'''
set1 = {1,5,0,12,56,9,46,4868}
usernum = int(input("Enter num:"))
def setInsert():
    set1.add(usernum)
    return set1
print(setInsert())
'''

# 60.
'''
set1 = {1,5,0,12,56,9,46,4868}
usernum = int(input("Enter num:"))
def setDelete():
    set1.discard(usernum)
    return set1
print(setDelete())
'''

# 61.
'''
set2a = {6,3,4,5,7}
set2b = {10391039,10399310,4898429,42892,48,49,4}
def setUnion():
    set2Union = set2a.union(set2b)
    if len(set2Union) > 10:
        print(">10 elements")
    else:
        print("Less than 10")
setUnion()
'''

# 62.
'''
set2a = {6,3,5,7}
set2b = {10391039,10399310,4898429,42892,48,49,4}
def setIntersect():
    set2Intersect = set2a.intersection(set2b)
    if len(set2Intersect) > 0:
        print(set2Intersect)
    else:
        print("No overlap")
setIntersect()
'''

# 63.
'''
set2b = {10391039,10399310,4898429,42892,2,1}
def setCheckLen():
    if len(set2b) > 5:
        set2b.clear()
    return set2b
print(setCheckLen())
'''

# 64.
'''
set2a = {6,3,5,7}
set2b = {10391039,10399310,4898429,42892,48,49,4}
def setDiff():
    diff = set2a.difference(set2b)
    if len(diff) > 0:
        return diff
    else:
        return "empty"
print(setDiff())
'''

# 65.
'''
userkey = input("Enter Key: ")
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def ValGet():
    if userkey in dict1:
        print(dict1.get(userkey))
    else:
        print("Not found")
ValGet()
'''

# 66.
'''
userkey = input("Enter Key: ")
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def keyPop():
    if userkey in dict1:
        print(dict1.pop(userkey))
        print(dict1)
    else:
        print("Key not Found")
keyPop()
'''

# 67.
'''
dict1 = {
    "Key1":10,
    "Key2":1098
}
def keyList():
    listdict = list(dict1.keys())
    if len(listdict) > 3:
        return("Greater than 3 keys; ", listdict)
    else:
        return("<3 keys, ", listdict)
print(keyList())
'''

# 68.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}

def DictVals():
    list1 = list(dict2.values())
    sum = 0
    for i in list1:
        sum += i
    return sum
print(DictVals())
'''

# 69.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":-109.98
}
def dictUpdate():
    usrky = input("Enter Key: ")
    if usrky in dict1:
        print(dict1)
    else:
        tuple1 = [(usrky, input("Enter Val: "))]
        dict1.update(tuple1)
        print(dict1)
dictUpdate()
'''

# 70.
'''
dict1 = {
    "Key1":10,
    "Key2":1098,
    "Key3":1762543,
    "Key4":109.98
}
def itemDict():
    for key in dict1:
        if dict1.get(key) > 0:
            continue
        else:
            return dict1.items(), False
    return (True, dict1.items())
print(itemDict())
'''