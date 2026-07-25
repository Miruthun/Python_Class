# My Booking Confirmation Function
import Constants as C

def BookCnf(ID):
    C.Bookings
    print("=============================")
    print("     Booking Confirmed       ")
    print("=============================")
    print()
    for key in C.Bookings[ID]:
        print(f"{key} : {C.Bookings[ID][key]}")
        print()
    golf_carts_unavail = {"list1": ["Placeholder"]}
    golf_carts_unavail["list1"] = [C.Bookings[ID]["Selected_Cart_ID"], C.Bookings[ID]["Driver"]]
    C.golf_carts.pop(C.Bookings[ID]["Selected_Cart_ID"])
    return golf_carts_unavail