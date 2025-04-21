# Initializing a list

list = ["milk","eggs","bread","butter","cheese"]

# Add more items

newGroceries = ["apples","bananas","orange juice"]

list.extend(newGroceries)

# Remove items

list.remove(4,7)

# Update items

list[0] = "milk (cheaper brand)"
list[2] = "bread (cheaper brand)"

# Final list

print(list)