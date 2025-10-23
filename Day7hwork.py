inventory = []

def add_item(item):
    """Adds an item to the inventpory list."""
    inventory.append(item)

def main():
    """Adding items with calling the add_items function."""
    add_item("Dog Food")
    add_item("Cat Toy")
    add_item("Bird Cage")
    add_item("Fish Tank")
    print("INVENTORY: ",inventory)
    
    total_items = count_items(inventory)
    print("TOTAL ITEMS: ",total_items)
    
    show_item = lambda item: print(f"Item in Stock: {item}")
    for item in inventory:
        show_item(item)

def count_items(items):
    """Counts the number of items in the list using recursion."""
    if not items:
        return 0
    else:
        return 1 + count_items(items[1:])

    
main()