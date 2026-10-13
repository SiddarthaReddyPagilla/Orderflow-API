
# DispatchForge
# Dallas-Fort Worth Delivery Optimization System
# Week 1: Real Warehouse Reference Locations

warehouses = [
    {
        "id": 1,
        "name": "West Dallas Hub",
        "reference_site": "DAL3",
        "address": "1301 Chalk Hill Rd",
        "city": "Dallas",
        "state": "TX",
        "zip_code": "75211"
    },
    {
        "id": 2,
        "name": "Coppell Hub",
        "reference_site": "DFW6",
        "address": "940 W Bethel Rd",
        "city": "Coppell",
        "state": "TX",
        "zip_code": "75019"
    },
    {
        "id": 3,
        "name": "North Fort Worth Hub",
        "reference_site": "DFW7",
        "address": "700 Westport Pkwy",
        "city": "Fort Worth",
        "state": "TX",
        "zip_code": "76177"
    }
]

print("Welcome to DispatchForge!")
print("Dallas-Fort Worth Warehouse Network")
print("-----------------------------------")

for warehouse in warehouses:
    print(f"Hub ID: {warehouse['id']}")
    print(f"Name: {warehouse['name']}")
    print(f"Reference site: {warehouse['reference_site']}")
    print(f"Location: {warehouse['address']}, "
          f"{warehouse['city']}, "
          f"{warehouse['state']} {warehouse['zip_code']}")
    print("-----------------------------------")

print(f"Total warehouse locations: {len(warehouses)}")
