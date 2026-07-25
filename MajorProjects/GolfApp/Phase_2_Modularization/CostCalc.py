# My Cost Calc Function
import ValidationChecks as VC
import Constants as C
def Cost():
    bags = VC.int_check("How many bags will you be bringing", 0, 10)
    cost = C.base_fare + (bags*C.luggage_cost)
    return {
        "Bags": bags,
        "Fare": cost
    }