import Constants as C, Validation as V
from typing import Dict, List

def order_separate_items(
    customers: List[str]
) -> List[Dict]:

    orders = []

    print("\nINDIVIDUAL ORDERING MODE")

    for person in customers:
        print(C.SINGLE_LINE)
        print(f"{person}'s Order")

        while True:
            item_choice = V.validate_integer(
                "Enter item number (0 to finish): ",
                0,
                len(C.FOOD_MENU)
            )

            if item_choice == 0:
                break

            quantity = V.validate_integer(
                "Enter quantity: ",
                1,
                100
            )

            item_name, item_price = C.FOOD_MENU[item_choice]

            for _ in range(quantity):
                orders.append({
                    "name": item_name,
                    "price": item_price,
                    "shared_by": [person]
                })

            print(
                f"Added {quantity} x {item_name}"
            )

    return orders
