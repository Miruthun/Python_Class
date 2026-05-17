menu = {
    1:["Pasta", 15],
    2:["Cheese Pizza", 10],
    3:["Macaroni & Cheese", 7],
    4:["Tiramisu", 6],
    5:["Gelato", 4],
    6:["Milkshake", 8]
}
x = True
while x == True:
    payConfig = int(input("How are you going to pay: GroupSplit (1), Separate Orders (2), or Mixed (3)"))
    GroupNum = int(input("How many of y'all are here:"))
    if payConfig < 3 and payConfig > 0:
        if GroupNum < 10 and GroupNum > 0:
            break
        else:
            print("The group size you have entered is not within bounds. Please keep group size between 1-10.")    
    else:
        print("The pay configuration you have entered is not within bounds. Please keep pay configuration between 1, 2, & 3.")    
Names = []
for i in range(1,GroupNum+1):
    Names.append(input("Name:"))
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
#            sumT = 0
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
        print(tipDecimal)
        for key in Taxes:
            TipPercent = round((1+tipDecimal),2)
            print(TipPercent)
            TaxedAmount = Taxes[key]
            TipAdd[key] = TipPercent*TaxedAmount
        print(TipAdd)
        return TipAdd
tip(Names)            

if payConfig == 1:
    GroupTotal = tip()
    IndTotal = round(GroupTotal/GroupNum, 2)
    for i in range(0,len(Names)):
        print(Names[i],": $", IndTotal)
elif payConfig == 2:
    print()