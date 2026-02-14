'''
def participant_info_collector():
    num_of_people = input("How many people are there: ")
    print("Enter Names: ")
    print()
    
participant_info_collector()
'''
menu = {
    1:["Pasta", 15],
    2:["Cheese Pizza", 10],
    3:["Macaroni & Cheese", 7],
    4:["Tiramisu", 6],
    5:["Gelato", 4],
    6:["Milkshake", 8]
}
peopleNum = int(input("How many people are there: "))
def order():
    pay_config = input("How will you guys pay: together(1) or separately(2)?")
    if pay_config == "1":
        print(input("What do you all want to order: "), menu)
        Item_List_Price = []
        Item_Name_List = {

        }
        done = True
        while done:
            item1 = int(input("Item number: "))
            item1Num = int(input("How many of this item do you all want: "))
            item1Total = (menu[item1][1])*item1Num
            item_Name = menu[item1][0]
            # Item_Name_List.append(item_Name)
            Item_List_Price.append(item1Total)
            Item_Name_List[item_Name] = item1Num
            flag = input("Are you all done with order: Enter Yes(0) or No(1)")
            if flag == "0":
                done = False

        # orderlist = []
        # done = True
        # counter = 0
        # for i in range(1,done):
        #     item_current = print(input("Item: "))
        #     if item_current == "done":
        #         done = counter
        #     else:
        #         orderlist.append(item_current)
        #     counter+=1
    listdetails = []
    for i in range(1,peopleNum+1):
        people_info = input("What's your names")
    return [Item_List_Price, Item_Name_List]
# print(order())
# Don't assume, input number, not string
# Create separate functions for major features, like tax, tip, etc
# Parse variables to next finctions, use return
def totalCalc():
    Order = order()
    Prices = Order[0]
    totalPrice = 0
    for i in Prices:
        totalPrice += i
# I can use sum function here too
    return totalPrice

def tax():
    total = totalCalc()
    taxedTotal_NF = 1.15*total
    taxedTotal_F = round(taxedTotal_NF,2)
    return taxedTotal_F

def tip():
    taxTot = tax()
    tip_percent = (int(input("What is the percentage of total you all want to tip?")))/100
    tipped_total = round((1+tip_percent)*taxTot, 2)
    return tipped_total
# print(tip())
