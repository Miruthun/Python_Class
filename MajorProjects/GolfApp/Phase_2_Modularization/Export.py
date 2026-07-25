# My Export Function
import json
import Constants as C

def export():
    C.Bookings
    with open("Golf_Cart_Bookings.json", "w") as gcb:
        json.dump(C.Bookings, gcb)
    print("Export Complete: Golf_Cart_Bookings.json")