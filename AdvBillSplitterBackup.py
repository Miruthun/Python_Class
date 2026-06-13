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
        print("What do you all want to order: ", menu)
        Item_List_Price = []
        Item_Name_List = {

        }
        done = True
        while done:
            item1 = int(input("Item number: "))
            item1Num = int(input("How many of this item do you all want: "))
            item1Total = (menu[item1][1])*item1Num
            item_Name = menu[item1][0]
            # print(item_Name)
            # Item_Name_List.append(item_Name)
            Item_List_Price.append([item_Name,item1Total])
            print(Item_List_Price)
            Item_Name_List[item_Name] = item1Num
            flag = input("Are you all done with order: Enter Yes(0) or No(1)")
            if flag == "0":
                done = False
        return Item_List_Price

    elif pay_config == "2":
        listNames = []
        listNamewOrder = []
        for i in range(1,peopleNum+1):
            listNames.append(input("Name: "))
        for i in range(0,peopleNum):
            listname = listNames[i]
            print(listname, "what do you want to order: ", menu)
            done = True
            while done:
                item1 = int(input("Item number: "))
                item1Num = int(input("How many of this item do you want: "))
                item1Total = (menu[item1][1])*item1Num
                item_Name = menu[item1][0]
                listNamewOrder.append([item_Name, item1Total, listname])
                flag = input("Are you all done with order: Enter Yes(0) or No(1)")
                if flag == "0":
                    done = False
        return listNamewOrder
        '''
        for i in range(0,peopleNum):
            listname = listNames[i]
            print(listname, ",How many items do you want to order?")
            ordertimes = int(input())
            for i in range(0,ordertimes):
                print(listname, ", What item do you want to order?", menu)
                ordernum = input()
                listofOrders = []
                listofOrders.append(menu[int(ordernum)])
                listNamewOrder[listNames[i]] = listofOrders
        print(listNamewOrder)
        '''
            

# order()

def totalCalc():
    Order = order()
    print("This is order:", Order)
    totalPrice = 0
    for i in range(len(Order)):
        print(i)
        totalPrice += Order[i][1]
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
print(tip())


#Backup2
'''
def participant_info_collector():
    num_of_people = input("How many people are there: ")
    print("Enter Names: ")
    print()
    
participant_info_collector()
'''
file = open("SavedInfo.txt", "a")
menu = {
    1:["Pasta", 15],
    2:["Cheese Pizza", 10],
    3:["Macaroni & Cheese", 7],
    4:["Tiramisu", 6],
    5:["Gelato", 4],
    6:["Milkshake", 8]
}
peopleNum = int(input("How many people are there: "))
x=20
#file.write(str(x))
pay_config = input("How will you guys pay: together(1) or separately(2)?")
if pay_config == "1":
    flag = False
elif pay_config == "2":
    flag = True

while flag == False:
    def order():
        #file.write(str(pay_config))
            print("What do you all want to order: ", menu)
            Item_List_Price = []
            Item_Name_List = {}
            done = True
            while done:
                item1 = int(input("Item number: "))
                item1Num = int(input("How many of this item do you all want: "))
                item1Total = (menu[item1][1])*item1Num
                item_Name = menu[item1][0]
                # print(item_Name)
                # Item_Name_List.append(item_Name)
                Item_List_Price.append([item_Name,item1Total])
                file.write(str(Item_List_Price))
                print(Item_List_Price)
                Item_Name_List[item_Name] = item1Num
                flag = input("Are you all done with order: Enter Yes(0) or No(1)")
                if flag == "0":
                    done = False
            return Item_List_Price
    # order()

    def totalCalc():
        Order = order()
        if Order[0] == 0:
            calclist = []
            print("This is order:", Order)
            totalPrice = 0
            for i in range(len(Order[1])):
                print(i)
                totalPrice += Order[1][i][1]
                print("Subtotal:", totalPrice)
        # file.write(str(totalPrice))
            calclist.append(0)
            calclist.append(totalPrice)
            print(calclist)
            return calclist


    def tax():
        subtotal = totalCalc()
        if subtotal[0] == 0:
            total = totalCalc()
            taxedTotal_NF = 1.15*total
            tax = round(taxedTotal_NF-total,3)
            taxedTotal_F = round(taxedTotal_NF,3)
            print("Tax:", tax)
            return [0,taxedTotal_F]
        elif subtotal[0] == 1:
            taxlist = []
            for i in subtotal:
                total = subtotal[i][1]
                taxedTotal_NF = 1.15*total
                tax = round((taxedTotal_NF-total),3)
                taxlist.append([subtotal[i][0],round(taxedTotal_NF,3)])
                print("STR",taxlist)
                print(subtotal[i][0], "'s Tax:", tax)
            return [1,taxlist]

    def tip():
        taxTot = tax()
        print(taxTot)
        if taxTot[0] == 0:
            tip_percent = (int(input("What is the percentage of total you all want to tip?")))/100
            tipped_total = round((1+tip_percent)*taxTot, 3)
            tip = taxTot*tip_percent
            print("Tip: ", tip)
            return tipped_total
        print("Total:", tipped_total)
        if taxTot[0] == 1:
            for i in taxTot[1]:
                tip_percent = (int(input("What is the percentage of total you all want to tip?")))/100
                tipped_total = round((1+tip_percent)*taxTot[1][i][1], 3)
                tip = (taxTot[1][i][1])*tip_percent
                tiplist = []
                tiplist.append(tip)
                print("Tip: ", tip)
                return [tiplist, tipped_total]
    tip()
    '''
            for i in taxTot[1]:
                print(tipl)
    '''
    file.close()
'''
            elif pay_config == "2":
            listNames = []
            listNamewOrder = {}
            for i in range(1,peopleNum+1):
                listNames.append(input("Name: "))
            for i in range(0,peopleNum):
                listname = listNames[i]
                print(listname)
                listNamewOrder[listname] = []
                print(listNamewOrder)
                file.write(str(listNamewOrder))
                """
                for i in range(1,peopleNum+1):
                    print(listNamewOrder[listname])
                    listNamewOrder[listname][] = []
                """
                print(listNamewOrder)
                print(listname, "what do you want to order: ", menu)
                done = True
                while done:
                    item1 = int(input("Item number: "))
                    item1Num = int(input("How many of this item do you want: "))
                    item1Total = (menu[item1][1])*item1Num
                    item_Name = menu[item1][0]
                    listNamewOrder[listname]=[item_Name, item1Total, listname]
                    flag = input("Are you all done with order: Enter Yes(0) or No(1)")
                    if flag == "0":
                        done = False
            file.write(str(listNames))
            return [1,listNamewOrder,listNames]
'''
'''
        elif Order[0] == 1:
            print("This is order:", Order)
            dict1 = Order[1]
            totalPrice = []
            for key in dict1:
                print(len(Order[1]))
                print(key)
                
                totalPrice.append([key,"'s subtotal:", dict1[(key)][1]])
                print(key,"'s subtotal:", dict1[(key)][1])
            return [1, totalPrice]
'''