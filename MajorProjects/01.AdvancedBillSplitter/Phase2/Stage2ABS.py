# Project Code - Arvinder Pal
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import Constants, Customers, Bill, Tip, Split_Ind_Totals, Reciept, Export, OrderAccess


# -----------------------------------
# Main
# -----------------------------------
def main():
    print(Constants.HASHED_LINE)
    print("WELCOME TO ADVANCED BILL SPLITTER")
    print(Constants.HASHED_LINE)

    try:
        customers = Customers.get_customers()

        orders = OrderAccess.get_orders(customers)

        subtotal = Bill.calculate_subtotal(orders)

        print(Constants.SINGLE_LINE)
        print(f"Subtotal: ${subtotal:.2f}")

        tax_amount, total_with_tax = Bill.calculate_tax(
            subtotal
        )

        print(
            f"Tax ({Constants.TAX_RATE}%): "
            f"${tax_amount:.2f}"
        )

        print(
            f"Total After Tax: "
            f"${total_with_tax:.2f}"
        )

        tip_rate = Tip.get_tip()

        tip_amount, final_total = Tip.calculate_tip(
            total_with_tax,
            tip_rate
        )

        print(
            f"Tip Amount: "
            f"${tip_amount:.2f}"
        )

        print(
            f"Final Total: "
            f"${final_total:.2f}"
        )

        people_totals = Split_Ind_Totals.calculate_individual_totals(
            customers,
            orders,
            tax_amount,
            tip_amount
        )

        Reciept.generate_receipt(
            customers,
            orders,
            subtotal,
            tax_amount,
            tip_amount,
            final_total,
            people_totals
        )

        Export.export_receipt(
            customers,
            people_totals,
            final_total
        )
        print("p")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

    except Exception as e:
        print(
            f"\nAn error occurred: {str(e)}"
        )
    print("a")

if __name__ == "__main__":
    main()