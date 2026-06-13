import Constants as C
from typing import List, Dict, Tuple

def calculate_subtotal(
    orders: List[Dict]
) -> float:
    return round(
        sum(order["price"] for order in orders),
        2
    )


def calculate_tax(
    subtotal: float
) -> Tuple[float, float]:

    tax_amount = round(
        subtotal * (C.TAX_RATE / 100),
        2
    )

    total_with_tax = round(
        subtotal + tax_amount,
        2
    )

    return tax_amount, total_with_tax