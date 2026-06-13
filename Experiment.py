peopleNum = 2
Names = []
OrderList = {}
for i in range(1,peopleNum+1):
    Names.append(input("Name: "))
print(Names)
for i in range(0,peopleNum):
    key = Names[i]
    OrderList[key] = []
    for j in range(0,peopleNum):
        (OrderList[key]).add(0)
print(OrderList)
