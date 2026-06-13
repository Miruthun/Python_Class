import Constants as C, Validation as V
from typing import List

def get_customers() -> List[str]:
    print(C.HASHED_LINE)
    print("GROUP SETUP")
    print(C.HASHED_LINE)

    num_people = V.validate_integer(
        f"Enter number of people ({C.MIN_PEOPLE}-{C.MAX_PEOPLE}): ",
        C.MIN_PEOPLE,
        C.MAX_PEOPLE
    )

    customers = []

    print("\nEnter names:")

    for i in range(num_people):
        name = V.validate_name(
            f"Person {i+1}: ",
            customers
        )
        customers.append(name)

    print(f"\nGroup created for {len(customers)} people")
    print(C.SINGLE_LINE)

    return customers