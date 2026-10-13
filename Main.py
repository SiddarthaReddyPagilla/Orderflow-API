
# DispatchForge - Seattle Delivery Simulator
# Day 1: Warehouse Inventory

warehouses = [
    {"name": "Seattle Central", "stock": 15},
    {"name": "Ballard Hub", "stock": 8},
    {"name": "Capitol Hill Hub", "stock": 0}
]

print("Welcome to DispatchForge!")
print("Warehouse Inventory Report")
print("--------------------------")

for warehouse in warehouses:
    print(f"{warehouse['name']}: {warehouse['stock']} items")
