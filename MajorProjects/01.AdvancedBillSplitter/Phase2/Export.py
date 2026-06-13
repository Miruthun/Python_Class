import datetime as datetime
import json
def export_receipt(
    customers,
    people_totals,
    final_total
):
    data = {
        "date": str(datetime.datetime.now()),
        "customers": customers,
        "individual_totals": people_totals,
        "final_total": final_total
    }

    filename = (
        f"bill_"
        f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w") as file:
        json.dump(
            data,
            file,
            indent=4
        )

    print(
        f"\nReceipt exported to {filename}"
    )
