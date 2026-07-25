# My Booking Mechanism Function
import Availability as A
import ValidationChecks as VC

def BookingMech():
    Deps = A.Available_Deps()
    print(f'Here are the available departments:{Deps}')
    while True:
        PickupDep = VC.name_check("What is the place you want to be picked up at: ", Deps.keys())
        DropoffDep = VC.name_check("What is your intended destination: ", Deps.keys())
        if PickupDep == DropoffDep:
            print("Your pickup and dropoff destinations that you have entered are the same. Please enter  separate pickup and dropoff destinations.")
            continue
        else:
            break
    Carts = A.Avail_Carts()
    print(f"Here are the available carts: {Carts}")
    CID = VC.name_check("Please enter desired cart ID: ", Carts.keys())
    Driver = Carts[CID]
    return {
        "Pickup_Place": PickupDep,
        "Dropoff_Place": DropoffDep,
        "Selected_Cart_ID": CID,
        "Driver": Driver
    }