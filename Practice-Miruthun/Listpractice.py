# Initializing a list

list = ["milk","eggs","bread","butter","cheese"]

# Add more items

newGroceries = ["apples","bananas","orange juice"]

list.extend(newGroceries)

# Remove items

list.remove("cheese")
list.remove("orange juice")

# Update items

list[0] = "milk (cheaper brand)"
list[2] = "bread (cheaper brand)"

# Final list

print(list)