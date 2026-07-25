# My Search Function
import ValidationChecks as VC
import Constants as C

def Search():
    C.Bookings
    options = ["1","2"]
    while True:
        print("Search Bookings:")
        choice = VC.name_check("Choose a search operator: BID(1) or Employee Name(2)", options)
        if choice == "1":
            BookID = input("BID: ")
            EmpName = None
        else:
            EmpName = input("Name: ")
            BookID = None
            EmpName = EmpName.strip()
            EmpName = EmpName.lower()
        found = False
        for item in C.Bookings:
            EN = C.Bookings[item]["Employee Name"]
            EN = EN.lower()
            EN = EN.strip()
            if BookID == item or EmpName == EN:
                for key in C.Bookings[item]:
                    print(f"{key} : {C.Bookings[item][key]}")
                found = True
        if found:
            break
        else:
            print("What you have entered is not found. Please try again.")