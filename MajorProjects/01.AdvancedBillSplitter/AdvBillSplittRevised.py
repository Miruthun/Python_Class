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
def Customers():
    num_people = int_check(f'Please Enter the number of people in your group, between {max_customer_num} & {min_customer_num}.')
    customers = []
    for i in range(num_people):
        name = name_check(f'Person {i+1}: ', customers)
        customers.append(name)
    print(f'{len(customers)} people checked in.')
    return customers

# My Menu Access Functions (NEEDS FINISHING)
def OrderStart(customers):
    print(menu)
    print("Ordering Modes")
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

# My IndOrders Functions
def SepOrder(customers):
    orders = []
    print("You are entering Individual Ordering Mode.")
    for person in customers:
        print(f"{person}'s order:")
        while True:
            Item = int_check("Enter the number of the item you want from the menu! (Or press 0 to finish your order):", 0, len(menu))
            if Item == 0:
                break
            item_quantity = int_check("Enter how many times you want this dish?", 0,100)
            itemName, itemPrice = menu[Item]
            for i in range(item_quantity):
                orders.append({"Name": itemName, "Price": itemPrice, "Shared By": person})
            print(f'Added {item_quantity} x {itemName}')
    return orders

# My Common Orders Functions
def CommOrder(customers):
    orders = []
    print("You are entering Common Ordering Mode:")
    while True: 
        Item = int_check("Enter menu item number to order it, or click 0 to say you're done!", 0, len(menu))
        if Item == 0:
            if not orders:
                print("Please choose atleast one item.")
                continue
            break
        if Item not in menu:
            print("That is not a valid menu number. Please try again.")
            continue
        quantity = int_check("Enter how many times you are ordering this item:", 0, 100)
        ItemName, ItemPrice = customers(Item)
        while True:
            ShareInp = input("Shared By: (Enter Names, separating them by commas, or use 'all' if everyone is sharing the item)").strip()
            SharedTrue = int_check(ShareInp, customers)
            if SharedTrue is not None:
                break
        for i in range(quantity):
            orders.append({"Name":ItemName, "Price": ItemPrice, "Shared By": SharedTrue})
        print(f'Added {quantity} x {ItemName}')
    return orders

# My Billing Functions
def SubTotal(orders):
    subtotal = 0
    for i in range(orders):
        subtotal += 1
    return subtotal

def Tax(subtotal):
    taxpercent = food_tax/100
    tax_amount = round(taxpercent*subtotal, 2)
    taxed_total = round(tax_amount + subtotal, 2)
    return tax_amount, taxed_total

def TipAsk():
    print("How much would you like to tip?")
    print("1. 0%")
    print("2. 10%")
    print("3. 20%")
    print("4. 25%")
    print("5. 30%")
    print("6. Custom")
    TipInp = int_check("Enter your choice:", 1, 6)
    TipPercent = 0
    if TipInp == 1:
        TipPercent = 0
    elif TipInp == 2:
        TipPercent = 0.1
    elif TipInp == 3:
        TipPercent = 0.2
    elif TipInp == 4:
        TipPercent = 0.25
    elif TipInp == 3:
        TipPercent = 0.3
    else:
        TipPercent = int_check("Enter Your Custom Tip Percent (must be a whole number)", 0, 30)
    return TipPercent

def TipCalc(TipPercent, taxed_total):
    tip_amount = round(TipPercent*taxed_total,2)
    Final_Total = round(tip_amount + taxed_total)
    return tip_amount, Final_Total

# My FinalIndTotals Functions
def FinalIndTotals(customers, orders, tax_amount, tip_amount):
    IndTotals = {
        customer : 0
        for customer in customers
    }
    for order in orders: 
        SplitAmount = (order["Price"]/order["Shared By"])
        for person in order["Shared By"]:
            IndTotals[person] +=SplitAmount
    Billings = (tax_amount + tip_amount)/len(customers)
    for person in IndTotals:
        IndTotals[person] += Billings
        IndTotals[person] = round(IndTotals[person],2)
    return IndTotals

# My Receipt Function
def receipt(customers, orders, tax_amount, tip_amount, subtotal, Final_Total, IndTotals):
    print("Final Receipt:")
    print()
    print("Orders:")
    for order in orders:
        print(
            f"{order['name']} "
            f"- ${order['price']:.2f} "
            f"(Shared by: "
            f"{', '.join(order['shared_by'])})"
        )
    print()
    print(f'Subtotal: ${subtotal:.2f}')
    print(f'Tax: ${tax_amount:.2f}')
    print(f'Tip: ${tip_amount:.2f}')
    print(f'Final Total: ${Final_Total:.2f}')
    print()
    print("Final Individual Totals:")
    for person in IndTotals:
        print(f'{person}: ${IndTotals[person]:.2f}')

# My Export Functions
import datetime as datetime
import json
def export_receipt(
    customers,
    IndTotals,
    Final_Total
):
    data = {
        "date": str(datetime.datetime.now()),
        "customers": customers,
        "individual_totals": IndTotals,
        "final_total": Final_Total
    }

    filename = (
        f"bill_"
        f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    print(
        f"\nReceipt exported to {filename}"
    )

# My Main.py Function
def main():
    print()
    print("WELCOME TO ADVANCED BILL SPLITTER")
    print()

    try:
        customers =  Customers()

        orders = get_orders(customers)

        subtotal = Bill.calculate_subtotal(orders)

        print(Constants.SINGLE_LINE)
        print(f"Subtotal: ${subtotal:.2f}")

        tax_amount, total_with_tax = Bill.calculate_tax(
            subtotal
        )

        print(
            f"Tax ({Constants.TAX_RATE}%): "
            f"${tax_amount:.2f}"
        )

        print(
            f"Total After Tax: "
            f"${total_with_tax:.2f}"
        )

        tip_rate = Tip.get_tip()

        tip_amount, final_total = Tip.calculate_tip(
            total_with_tax,
            tip_rate
        )

        print(
            f"Tip Amount: "
            f"${tip_amount:.2f}"
        )

        print(
            f"Final Total: "
            f"${final_total:.2f}"
        )

        people_totals = Split_Ind_Totals.calculate_individual_totals(
            customers,
            orders,
            tax_amount,
            tip_amount
        )

        Reciept.generate_receipt(
            customers,
            orders,
            subtotal,
            tax_amount,
            tip_amount,
            final_total,
            people_totals
        )

        Export.export_receipt(
            customers,
            people_totals,
            Final_Total)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()













'''
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
'''
'''
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
    '''