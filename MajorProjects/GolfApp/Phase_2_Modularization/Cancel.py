# My Cancel Booking Function
import Constants as C
import ValidationChecks as VC

def cancelBook():
    C.Bookings
    BID_Input = VC.name_check("Please enter Booking ID of desired deletion: ", C.Bookings)
    deleted_cart = C.Bookings[BID_Input]["Selected_Cart_ID"]
    Removed_cart_driver = C.Bookings[BID_Input]["Driver"]
    key = deleted_cart
    value = Removed_cart_driver
    C.golf_carts[key] = value
    del C.Bookings[BID_Input]
    print(C.Bookings)
