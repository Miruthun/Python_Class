# My Booking Records Function (Combines Entered Data)
import InfoCollect as IC
import Booking as B
import CostCalc as CC
import Constants as C

def Bookings_Record():
    z = IC.infoCollect()
    x = B.BookingMech()
    y = CC.Cost()
    BNC = C.bookingNumCount
    BNC += 1
    C.bookingNumCount = BNC
    ID = f"B{BNC:03d}"
    A = z | x | y
    C.Bookings 
    C.Bookings[ID] = A
    return ID