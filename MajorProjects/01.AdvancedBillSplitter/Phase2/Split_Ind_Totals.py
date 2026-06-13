from typing import Dict, List

def calculate_individual_totals(
    customers: List[str],
    orders: List[Dict],
    tax_amount: float,
    tip_amount: float
) -> Dict[str, float]:

    people_totals = {
        customer: 0
        for customer in customers
    }

    for order in orders:
        split_amount = (
            order["price"] /
            len(order["shared_by"])
        )

        for person in order["shared_by"]:
            people_totals[person] += split_amount

    extra_cost = (
        tax_amount + tip_amount
    ) / len(customers)

    for person in people_totals:
        people_totals[person] += extra_cost
        people_totals[person] = round(
            people_totals[person],
            2
        )

    return people_totals