myList = [1,2,3,4,5]
myList.append(6)
myList.insert(0,0)
mytuple = (7,8,13,5.5)
myList.extend(mytuple)
print(myList)
myList[4] = 34
print(myList)
print(myList.pop())
print[len(myList)-1]
print(myList[3:6])
print(myList)
print(myList[:len(myList)])

myDictionary = {
    "Age" : 10,
    "Number" : 12,
    "Care" : 7
}
print(myDictionary)
print(myDictionary["age"])
print(myDictionary[10])
print(myDictionary.get("age"))
print(myDictionary["roll"])
print(myDictionary.get("roll"))
print(len(myDictionary))
print(type(myDictionary))
print(type(myDictionary["Care"]))
print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())
myDictionary["Care"] = 6
myDictionary.update({"roll" : 19})
newDictionary = myDictionary.copy()

mySet = {1,2,3,4,5,6,6,6}
print(mySet)
print(len(mySet))
mySet.add(34)
mySet.add(34)
mySet.add(34)
mySet.add(34)
mySet.add(35)
mySet2 = {7,8,9,0}
mySet.update(mySet2)
mySet.remove(3)
mySet.remove(59)
mySet.discard(4)
mySet.discard(56)

mySet3 = {11,21,31,41,51,61,71,8,9,0,1,2,3}
mySet4 = {11,21,31,41,51,61,71,8,9,0,1,2,3,101,102,103,104}
mySet5 = mySet.union(mySet3)
mySet6 = mySet|mySet3|mySet4
mySet7 = mySet3.intersection(mySet4)
mySet8 = mySet & mySet3 & mySet4

myTuple = (1,2,3,4,"Hi",True)
print(sum(myTuple))
print(sorted(myTuple))