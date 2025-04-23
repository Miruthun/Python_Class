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
tuple = ("Museum","Park","Museum","Bridge")
print(tuple.count("Museum"))
print(tuple.index("Museum"))

#Scenario 4
Dictionary1 = {
    "Cloth":100,
    "Spice":50
}
Dictionary2 = {
    "Spice":75,
    "Jewelery":20
}
Dictionary3 = Dictionary1.update(Dictionary2)
print(Dictionary3.values("Spice"))

#Scenario 5
ThisTuple = ("James","Sophia","Lily")
ThisTuple2 = ("James","Ethan","Mia")
ThisTuple3 = ThisTuple.union(ThisTuple2)
print(sorted(ThisTuple3))

#Scenario 6
ThisDictionary = {
    "Novel":1920,
    "Poetry":1850
}
ThisSet = set(ThisDictionary)
print(ThisSet[0])