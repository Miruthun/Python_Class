# My Revenue Function
import Constants as C

def rev():
    C.Bookings
    C.luggage_cost
    totalBookings = len(C.Bookings)
    Vals = C.Bookings.values()
    luggageCount = 0
    for item in Vals:
        luggageCount += item["Bags"]
    total_luggage_fees = luggageCount * C.luggage_cost
    total_revenue = 0
    for item in Vals:
        total_revenue += item["Fare"]
    print(f"Total Bookings      : {totalBookings}")
    print(f"Total Luggage Fees  : ₹{total_luggage_fees}")
    print(f"Total Revenue       : ₹{total_revenue}") 