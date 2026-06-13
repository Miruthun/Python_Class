import Constants as C

def generate_receipt(
    customers,
    orders,
    subtotal,
    tax_amount,
    tip_amount,
    final_total,
    people_totals
):
    print(C.HASHED_LINE)
    print("FINAL RECEIPT")
    print(C.HASHED_LINE)

    print("\nOrdered Items:")

    for order in orders:
        print(
            f"{order['name']} "
            f"- ${order['price']:.2f} "
            f"(Shared by: "
            f"{', '.join(order['shared_by'])})"
        )

    print(C.SINGLE_LINE)

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax_amount:.2f}")
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Final Total: ${final_total:.2f}")

    print(C.SINGLE_LINE)
    print("INDIVIDUAL TOTALS")

    for person, amount in people_totals.items():
        print(
            f"{person}: ${amount:.2f}"
        )
