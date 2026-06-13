import Constants as C, Validation as V
from typing import List, Dict

def order_common_items(
    customers: List[str]
) -> List[Dict]:

    orders = []

    print("\nCOMMON ORDERING MODE")

    while True:
        item_choice = V.validate_integer(
            "Enter item number (0 to finish): ",
            0,
            len(C.FOOD_MENU)
        )

        if item_choice == 0:
            if not orders:
                print("Please add at least one item.")
                continue
            break

        if item_choice not in C.FOOD_MENU:
            print("Invalid item.")
            continue

        quantity = V.validate_integer(
            "Enter quantity: ",
            1,
            100
        )

        item_name, item_price = C.FOOD_MENU[item_choice]

        while True:
            shared_input = input(
                "Shared by (comma names or 'all'): "
            ).strip()

            shared_by = V.validate_sharing_input(
                shared_input,
                customers
            )

            if shared_by is not None:
                break

        for _ in range(quantity):
            orders.append({
                "name": item_name,
                "price": item_price,
                "shared_by": shared_by
            })

        print(
            f"Added {quantity} x {item_name}"
        )

    return orders