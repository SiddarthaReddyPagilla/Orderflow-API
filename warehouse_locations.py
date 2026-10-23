# DispatchForge - DFW Warehouse Locations
# Public geographic reference points.
# All inventory and delivery operations are simulated.

WAREHOUSE_LOCATIONS = {
    "West Dallas Hub": {
        "reference_site": "DAL3",
        "latitude": 32.7558565,
        "longitude": -96.9041442
    },
    "Coppell Hub": {
        "reference_site": "DFW6",
        "latitude": 32.95805,
        "longitude": -97.01704
    },
    "North Fort Worth Hub": {
        "reference_site": "DFW7",
        "latitude": 32.97059,
        "longitude": -97.33571
    }
}


if __name__ == "__main__":
    print("DispatchForge - DFW Warehouse Locations")
    print("---------------------------------------")

    for name, location in WAREHOUSE_LOCATIONS.items():
        print(f"Warehouse: {name}")
        print(f"Latitude: {location['latitude']}")
        print(f"Longitude: {location['longitude']}")
        print("---------------------------------------")
