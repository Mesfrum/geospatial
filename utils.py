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