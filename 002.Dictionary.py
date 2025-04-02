myDictionary= {
    "name":"Miruthun",
    "age":16,
    "roll":1234
}

# Priting the whole dictionary
print(myDictionary)

# printing s specific element
print(myDictionary["age"])
print(myDictionary.get("roll"))


# keys can't be duplicated
myDictionary2= {
    "name":"Miruthun",
    "age":16,
    "roll":1234
}

# len()
print(len(myDictionary))
print(type(myDictionary))
print(type(myDictionary["age"]))

print(myDictionary.keys())
print(myDictionary.values())
print(myDictionary.items())

# Updating the existing element

myDictionary["roll"]= 2345
print(myDictionary)

myDictionary.update({"Birth Year":2000})
print(myDictionary)


# Removing a specific item from dictionary

myDictionary.pop("roll")
print(myDictionary)

# Always removes the last inserted value 
myDictionary.popitem()
print(myDictionary)


# Delete the dictionary 
# del myDictionary
# print(myDictionary)

# clear()

# myDictionary.clear()
# print(myDictionary)

# Create a dictionary copy 

newDictionary = myDictionary.copy()
print(newDictionary)
