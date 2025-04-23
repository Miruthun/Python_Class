#Scenario 1
list = ["Vase","Statue","Coin"]
list.append("Tablet")
list[0] = "Mask"
print(sorted(list))

#Scenario 2
set1 = {"Mango","Apple","Banana"}
set2 = {"Banana","Apple","Banana"}
set3 = set1.union(set2)
set3.add("Lemon")
print(set3)

#Scenario 3
tuple1 = ("Museum","Park","Museum","Bridge")
print(tuple1.count("Museum"))
print(tuple1.index("Museum"))

#Scenario 4
Dictionary1 = {
    "Cloth":100,
    "Spice":50
}
Dictionary2 = {
    "Spice":75,
    "Jewelery":20
}
Dictionary1.update(Dictionary2)
print(Dictionary1["Spice"])

#Scenario 5
ThisSet1 = {"James","Sophia","Lily"}
ThisSet2 = {"James","Ethan","Mia"}
ThisSet3 = ThisSet1.union(ThisSet2)
print(sorted(ThisSet3))

#Scenario 6
ThisDictionary = {
    "Novel":1920,
    "Poetry":1850
}
ThisTuple = tuple(ThisDictionary)
print(ThisTuple[0])