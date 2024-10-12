from constants import OSRM_BASE_URL
import requests


def is_valid_coordinate(coordinate):
    # Ensure the coordinate is a list and has exactly two elements
    if not isinstance(coordinate, list) or len(coordinate) != 2:
        return False

    lat, lon = coordinate

    # Ensure latitude and longitude are floats and within valid ranges
    if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
        return False
    if not (-90 <= lat <= 90) or not (-180 <= lon <= 180):
        return False

    return True


def fetch_distance_matrix(coordinates: list):
    params = ""
    for coordinate in coordinates:
        lat, long = coordinate
        params += f"{long},{lat};"

    params = params.rstrip(";")

    url = f"{OSRM_BASE_URL}{params}?annotations=distance&skip_waypoints=true"
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()
        return response.get("distances")
    except requests.exceptions.RequestException as e:
        print(f"Error during the API call: {e}")
        return None
