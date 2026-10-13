
# DispatchForge - Warehouse Ranking Engine
# Version 1: Rank eligible warehouses by available stock.

from inventory import inventory
from warehouse_selection import find_eligible_warehouses


def rank_warehouses(product_sku, requested_quantity):

    # Step 1: Find warehouses with enough inventory
    eligible = find_eligible_warehouses(
        product_sku, requested_quantity
    )

    # Step 2: Define how warehouses are ranked
    def get_stock(warehouse_name):
        return inventory[warehouse_name][product_sku]

    # Step 3: Sort by available stock (highest first)
    ranked = sorted(
        eligible,
        key=get_stock,
        reverse=True
    )

    return ranked


if __name__ == "__main__":

    product_sku = "WATER-500ML"
    requested_quantity = 5

    results = rank_warehouses(
        product_sku, requested_quantity
    )

    print("DispatchForge - Warehouse Ranking")
    print("---------------------------------")

    for warehouse_name in results:
        available = inventory[warehouse_name][product_sku]

        print(f"{warehouse_name}: {available} available")
