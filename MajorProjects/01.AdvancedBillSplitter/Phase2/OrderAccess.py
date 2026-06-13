import Validation as V, MenuAccess as MA, CommOrders as CO, IndOrders as IO
from typing import Dict, List

def get_orders(
    customers: List[str]
) -> List[Dict]:

    MA.display_menu()

    print("\nOrdering Modes")
    print("1. Common Orders")
    print("2. Individual Orders")
    print("3. Mixed Orders")

    mode = V.validate_integer(
        "Choose option: ",
        1,
        3
    )

    all_orders = []

    if mode == 1:
        all_orders = CO.order_common_items(customers)

    elif mode == 2:
        all_orders = IO.order_separate_items(customers)

    elif mode == 3:
        print("\nAdding common orders...")
        common_orders = CO.order_common_items(customers)
        all_orders.extend(common_orders)

        print("\nAdding individual orders...")
        individual_orders = IO.order_separate_items(customers)
        all_orders.extend(individual_orders)

    return all_orders
