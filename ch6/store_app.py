import store

inventory = store.Inventory()
inventory.add_item(store.Item('Milk', 0))
inventory.print_items()

try:
    inventory.remove_item('Milk')
except (store.OutOfStockError, ValueError) as e:
    print(e)