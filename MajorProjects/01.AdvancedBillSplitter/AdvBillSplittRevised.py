from typing import List

# My Constants
min_customer_num = 2
max_customer_num = 10
food_tax = 15.00
max_tip = 30.00
menu = {
    1:["Pasta", 15],
    2:["Cheese Pizza", 10],
    3:["Macaroni & Cheese", 7],
    4:["Tiramisu", 6],
    5:["Gelato", 4],
    6:["Milkshake", 8]
}

# My Validation Functions
def int_check(question: str, min_int: int, max_int: int):
    while True:
        try: 
            input_num_people = int(input(question))
            if input_num_people >= min_int and input_num_people <= max_int:
                return input_num_people
            print(f'You have entered a number of people in your group that is not within bounds. Please enter a number of people between {min_int} and {max_int}.')
        except ValueError:
            print(f'Invalid number. Please enter a number of people between {min_int} and {max_int}.')

def name_check(question: str, Names: List[str]):
    while True:
        name = input(question).strip()
        if not name:
            print("Please enter a valid name.")
        elif name.lower() in [N.lower() for N in Names]:
            print("This name has already been entered.")
        else:
            return name

# My Customer Info Function
def customers():
    num_people = int_check(f'Please Enter the number of people in your group, between {max_customer_num} & {min_customer_num}.')
    customers = []
    for i in range(num_people):
        name = name_check(f'Person {i+1}: ', customers)
        customers.append(name)
    print(f'{len(customers)} people checked in.')

# My Menu Access Functions (NEEDS FINISHING)
def OrderStart(customers):
    print(menu)
    print("\nOrdering Modes")
    print("1. Common Orders")
    print("2. Individual Orders")
    print("3. Mixed Orders")
    payConfig = int_check("How are you going to pay: 1,2,or 3?: ", 1,3)
    if payConfig == 1:
        print()
    elif payConfig == 2:
        print()
    else:
        print()
# 

x = True
while x == True:
    payConfig = int(input("How are you going to pay: GroupSplit (1), Separate Orders (2), or Mixed (3)"))
    GroupNum = int(input("How many of y'all are here:"))
    if payConfig <= 3 and payConfig > 0:
        if GroupNum <= 10 and GroupNum >= 0:
            break
        else:
            print("The group size you have entered is not within bounds. Please keep group size between 1-10.")    
    else:
        print("The pay configuration you have entered is not within bounds. Please keep pay configuration between 1, 2, & 3.")  

Names = []
while len(Names) < GroupNum:
    Name_input = input("Name:")
    if Name_input in Names:
        print("You have already entered this name previously. Please enter a new name.s")
        continue
    elif Name_input == "":
        print("You have entered no name. Please enter a valid name.")
    else:
        Names.append(Name_input)

totalSharePeople = []

for name in Names:
    z = True
    totalShare = []
    while z == True:
        Share = input(f'{name}, Who do you want to share with (select 0 if no one)')
        if Share ==name:
            print("Please enter someone else's name ohter than yours.")
        elif Share in Names:
            totalShare.append(Share)
            print(totalShare)
            continue
        elif Share == '0':
            z = False
        else:
            print('Please enter a valid name to share with. Please try again.')
        totalSharePeople.append(totalShare)
print(totalSharePeople)

def order():
    print("What do you all want to order: ", menu)
    Item_List_Price = []
    Item_Name_List = {}
    done = True
    while done:
        if payConfig == 1:
            item1 = int(input("Item number: "))
            item1Num = int(input("How many of this item do you all want: "))
            item1Total = (menu[item1][1])*item1Num
            item_Name = menu[item1][0]
            Item_List_Price.append([item_Name,item1Total])
            print(Item_List_Price)
            Item_Name_List[item_Name] = item1Num
            flag = input("Are you all done with order: Enter Yes(0) or No(1)")
            if flag == "0":
                done = False
            return Item_List_Price
        elif payConfig == 2:
            Item_Dict_Price = {}
            for name in Names:
                ItemExport = []
                NewDone = True
                while NewDone:
                    print(name, "'s Order:")
                    SelectedItem = int(input("Item Number:"))
                    ItemMultiples = int(input("How many of these do you want to order:"))
                    ItemTot = (menu[SelectedItem][1])*ItemMultiples
                    ItemName = menu[SelectedItem][0]
                    ItemExport.append([ItemName, ItemTot])
                    NewFlag = input("Are you all done with order: Enter Yes(0) or No(1)")
                    if NewFlag == "0":
                        NewDone = False
                    Item_Dict_Price[name] = []
                    Item_Dict_Price[name] = ItemExport
            return Item_Dict_Price
        elif payConfig == 3:
            Item_Dict_Price = {}
            for name in Names:
                ItemExport = []
                NewDone = True
                while NewDone:
                    print(name, "'s Order:")
                    SelectedItem = int(input("Item Number:"))
                    ItemMultiples = int(input("How many of these do you want to order:"))
                    ItemTot = (menu[SelectedItem][1])*ItemMultiples
                    ItemName = menu[SelectedItem][0]
                    ItemExport.append([ItemName, ItemTot])
                    NewFlag = input("Are you all done with order: Enter Yes(0) or No(1)")
                    if NewFlag == "0":
                        NewDone = False
                    Item_Dict_Price[name] = []
                    Item_Dict_Price[name] = ItemExport
            return Item_Dict_Price

        done = False

def totalCalc():
    if payConfig == 1:
        Order = order()
        calclist = []
        print("This is order:", Order)
        totalPrice = 0
        for i in range(len(Order)):
            print(i)
            totalPrice += Order[i][1]
            print("Subtotal:", totalPrice)
    # file.write(str(totalPrice))
        calclist.append(totalPrice)
        print(calclist)
        return calclist
    elif payConfig == 2:
        Order = order()
        calclist = {}
        print("This is order:", Order)
        totalPrice = 0
        for name in Order:
            for i in range(0, len(Order[name])):
                totalPrice += Order[name][i][1]
            calclist[name] = totalPrice
            totalPrice = 0
    # file.write(str(totalPrice))
    print("This is CalcList:", calclist)
    return calclist

def tax():
    sumT = 0
    if payConfig == 1:
        total = totalCalc()
#        sumT = 0
        for i in total:
            sumT +=i
        taxedTotal_NF = 1.15*sumT
        tax = round(taxedTotal_NF-sumT,2)
        taxedTotal_F = round(taxedTotal_NF,2)
        print("Tax:", tax)
        return taxedTotal_F
    elif payConfig == 2:
        total = totalCalc()
#        sumT = 0
        taxed = {}
        for key in total:
            sumT += total[key]
            taxedTotal_NF = 1.15*sumT
 #           tax = round(taxedTotal_NF-sumT,2)
            taxedTotal_F = round(taxedTotal_NF,2)
            taxed[key] = taxedTotal_F
            sumT = 0
#        print("Tax:", tax)
        print(taxed)
        return taxed
    
def tip(Names):
    if payConfig == 1:
        taxTot = tax()
        tip_percent = (int(input("What is the percentage of total you all want to tip?")))/100
        tipped_total = round((1+tip_percent)*taxTot, 2)
        tip = round(taxTot*tip_percent,2)
        print("Tip: ", tip)
        print("Total:", tipped_total)
        return tipped_total
    elif payConfig == 2:
        Taxes = tax()
        TipAdd = {}
        tipDecimal = (int(input("What is the percentage of total you  want to tip?")))/100
#        print(tipDecimal)
        for key in Taxes:
            TipPercent = round((1+tipDecimal),2)
#            print(TipPercent)
            TaxedAmount = Taxes[key]
            TipAdd[key] = round(TipPercent*TaxedAmount, 2)
#        print(TipAdd)
        return TipAdd

if payConfig == 1:
    GroupTotal = tip()
    IndTotal = round(GroupTotal/GroupNum, 2)
    for i in range(0,len(Names)):
        print(Names[i],": $", IndTotal)
elif payConfig == 2:
    def Scenario_2():
        Bill_total = tip(Names)
        for key in Bill_total:
            print(key, ":", "$", Bill_total[key], end = "\n")
    Scenario_2()
elif payConfig == 3:
    print()
else:
    print("error!")