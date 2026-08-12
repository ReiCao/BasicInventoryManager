from inventory_manager import InventoryManager

def is_valid_action(action: str) -> bool:
    if action != "A" and action != "S" and action != "D" and action != "F": return False
    return True

def add_to_inventory(manager: InventoryManager) -> None:
    try:
        name = input("Enter name: ")

        amount = int(input("Enter amount: "))
        price = float(input("Enter price: "))

        if amount < 0 or price < 0: raise ValueError

        manager.add_item(name=name, amount=amount, price=price)

    except ValueError:
        print("Invalid Amount or Price")

def edit_item_name(manager: InventoryManager, id_: int) -> None:
    name = input("Enter name: ")
    manager.edit_name(id_, name)

def edit_item_amount(manager: InventoryManager, id_: int) -> None:
    amount = int(input("Enter amount: "))

    if amount < 0: raise ValueError("Invalid Amount")

    manager.edit_amount(id_, amount)

def edit_item_price(manager: InventoryManager, id_: int) -> None:
    price = float(input("Enter price: "))

    if price < 0: raise ValueError("Invalid Price")

    manager.edit_price(id_, price)

def edit_item(manager: InventoryManager) -> None:
    try:
        id_ = int(input("Enter id: "))

        print("A - Edit Name | S - Edit Amount | D - Edit Price | F - Delete Item")
        action = input().upper()

        if not is_valid_action(action) or not manager.is_valid_id(id_): raise ValueError

        if action == "A": edit_item_name(manager, id_)
        elif action == "S": edit_item_amount(manager, id_)
        elif action == "D": edit_item_price(manager, id_)
        elif action == "F": manager.remove_item(id_)

    except ValueError:
        print("Invalid ID or Action")

def print_inventory(manager: InventoryManager) -> None:
    item_list = manager.get_inventory()

    print("+-———-+-——————————————————————————————————-+-————————-+-———————-+")
    print("| Id  | Name                                   | Amount | Price |")

    for item in item_list:
        print("+-———-+-——————————————————————————————————-+-————————-+-———————-+")
        print("|{:^5}| {:<38} |{:^8}|{:^7}|".format(item[0], item[1], item[2], item[3]))

def close_program(manager: InventoryManager) -> None:
    print("Closing Program")
    manager.end_connection()

def start_menu() -> None:
    actions_bar = ("+-——————————————————-+-————————————-+-—————————————-+-—————————-+",
                   "| A - Show Inventory | S - Add Item | D - Edit Item | F - Close |",
                   "+-——————————————————-+-————————————-+-—————————————-+-—————————-+"
                   )

    inventory_manager = InventoryManager()

    while True:
        for bar in actions_bar: print(bar)

        try:
            action = input().upper()

            if not is_valid_action(action): raise ValueError

            if action == "A": print_inventory(inventory_manager)
            elif action == "S": add_to_inventory(inventory_manager)
            elif action == "D": edit_item(inventory_manager)
            elif action == "F": close_program(inventory_manager); break

        except ValueError:
            print("Invalid Action")

def program() -> None:
    start_menu()

if __name__ == "__main__":
    program()
