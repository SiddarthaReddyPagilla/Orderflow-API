
# DispatchForge - Inventory Management
# All stock quantities are simulated data.

inventory = {
    "West Dallas Hub": {
        "WATER-500ML": 20,
        "SNACK-001": 15
    },
    "Coppell Hub": {
        "WATER-500ML": 7,
        "SNACK-001": 10
    },
    "North Fort Worth Hub": {
        "WATER-500ML": 0,
        "SNACK-001": 25
    }
}

def check_inventory(warehouse_name, product_sku, requested_quantity):

    if requested_quantity <= 0:
        return False

    warehouse_stock = inventory.get(warehouse_name)

    if warehouse_stock is None:
        return False

    available_quantity = warehouse_stock.get(product_sku, 0)

    if available_quantity >= requested_quantity:
        return True

    return False

def reserve_inventory(warehouse_name, product_sku, requested_quantity):

    # Step 1: Check if enough inventory is available
    if not check_inventory(warehouse_name, product_sku, requested_quantity):
        return False

    # Step 2: Reduce the available inventory
    inventory[warehouse_name][product_sku] -= requested_quantity

    # Step 3: Confirm the reservation was successful
    return True


if __name__ == "__main__":
    print("DispatchForge - Inventory Check")
    print("--------------------------------")

    print(check_inventory("West Dallas Hub", "WATER-500ML", 5))
    print(check_inventory("Coppell Hub", "WATER-500ML", 10))
    print(check_inventory("North Fort Worth Hub", "SNACK-001", 20))
    print(check_inventory("West Dallas Hub", "UNKNOWN-001", 2))
