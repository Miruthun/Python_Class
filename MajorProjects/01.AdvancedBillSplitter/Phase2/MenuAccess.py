import Constants as C
def display_menu():
    print(C.HASHED_LINE)
    print("RESTAURANT MENU")
    print(C.HASHED_LINE)

    print(f"{'Item No':<10}{'Item Name':<25}{'Price'}")

    for item_num, (name, price) in C.FOOD_MENU.items():
        print(
            f"{item_num:<10}"
            f"{name:<25}"
            f"${price:.2f}"
        )

    print(C.SINGLE_LINE)
