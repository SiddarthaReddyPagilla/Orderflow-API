
# DispatchForge - Geographic Distance Engine
# Calculates straight-line geographical distance.
# Driving distance and travel time are not calculated here.

from math import radians, sin, cos, sqrt, asin

EARTH_RADIUS_KM = 6371.0088


def haversine_distance(lat1, lon1, lat2, lon2):

    # Step 1: Convert degrees to radians
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Step 2: Calculate coordinate differences
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Step 3: Apply the Haversine formula
    a = (
        sin(delta_lat / 2) ** 2
        + cos(lat1) * cos(lat2)
        * sin(delta_lon / 2) ** 2
    )

    a = min(1.0, max(0.0, a))

    # Step 4: Calculate distance in kilometers
    distance = 2 * EARTH_RADIUS_KM * asin(sqrt(a))

    return distance


if __name__ == "__main__":

    print("DispatchForge - Distance Engine")
    print("-------------------------------")

    distance = haversine_distance(0, 0, 0, 1)

    print(f"Calculated distance: {distance:.2f} km")

    same_location = haversine_distance(
        32.8, -96.8, 32.8, -96.8
    )

    print(f"Same-location distance: {same_location:.2f} km")
