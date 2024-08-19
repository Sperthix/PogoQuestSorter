import re
import os
from math import radians, sin, cos, sqrt, atan2

# Function to calculate the distance between two coordinates using the Haversine formula
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius of the Earth in km
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

# Function to sort coordinates in an optimized path
def sort_coordinates(coords):
    sorted_coords = [coords.pop(0)]
    while coords:
        last = sorted_coords[-1]
        next_coord = min(coords, key=lambda coord: haversine(last[0], last[1], coord[0], coord[1]))
        sorted_coords.append(next_coord)
        coords.remove(next_coord)
    return sorted_coords

# Function to filter and sort coordinates from the GPX file
def filter_and_sort_coordinates(input_file, output_file, lat_min, lat_max, lon_min, lon_max):
    # Define a regex pattern to match the <wpt> tags and extract lat and lon
    pattern = re.compile(r'<wpt lat="([\d\.-]+)" lon="([\d\.-]+)"></wpt>')
    coordinates = []

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Search for the pattern in each line
        match = pattern.search(line)
        if match:
            # Extract latitude and longitude as floats
            lat = float(match.group(1))
            lon = float(match.group(2))
            
            # Check if the coordinate is within the square
            if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
                coordinates.append((lat, lon))
    
    # Sort the coordinates in an optimized path
    sorted_coordinates = sort_coordinates(coordinates)

    # Write the sorted coordinates to the output file
    with open(output_file, 'w') as output:
        for lat, lon in sorted_coordinates:
            output.write(f"{lat}, {lon}\n")

# Coordinates for the square
lat_min = 40.739083
lat_max = 40.779028
lon_min = -74.007611
lon_max = -73.950583

# Input and output file paths
input_folder = 'input'
output_folder = 'output'

# Input file path
input_file = os.path.join(input_folder, 'Mienfoo-4403-Quests-AUG-19-2024-Power-up-Pokemon-10-times-POKEHUB.gpx')

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Output file path (same name as input but with _sorted.txt extension)
output_file_name = os.path.splitext(os.path.basename(input_file))[0] + '_filtered_sorted.txt'
output_file = os.path.join(output_folder, output_file_name)

# Run the filtering and sorting function
filter_and_sort_coordinates(input_file, output_file, lat_min, lat_max, lon_min, lon_max)

print(f"Filtered and sorted coordinates have been saved to {output_file}")
