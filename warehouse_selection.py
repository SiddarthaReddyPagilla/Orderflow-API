
# DispatchForge - Warehouse Selection
# Find warehouses that can fulfill an order.

from inventory import inventory, check_inventory


def find_eligible_warehouses(product_sku, requested_quantity):

    eligible_warehouses = []

    for warehouse_name in inventory:

        if check_inventory(
            warehouse_name, product_sku, requested_quantity
        ):
            eligible_warehouses.append(warehouse_name)

    return eligible_warehouses


if __name__ == "__main__":

    result = find_eligible_warehouses("WATER-500ML", 5)

    print("DispatchForge - Warehouse Selection")
    print("-----------------------------------")
    print("Warehouses that can fulfill the order:")

    for warehouse in result:
        print(warehouse)
