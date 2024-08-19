# Coordinate Visualization and Sorting

This project allows you to sort GPS coordinates and visualize them on an interactive map. It also lets you copy the coordinates to your clipboard by clicking on the corresponding point on the map.

## How to Use

### 1. Add New File

Put the file containing the coordinates you want to sort into the `input` folder. Ensure the coordinates are in the format:

## latitude, longitude
40.779028, -73.950583
40.739083, -73.976083
40.746694, -74.007611

### 2. Run the Sorting Script

Start the Python script to process the coordinates:

```
python sort_coordinates.py
```

This will generate a sorted file in the output folder.

### 3. Visualize the Points on a Map
To visualize the sorted points, start a simple HTTP server in the project directory. This will allow you to view the map in your browser.

```
python -m http.server
```

After running the command, open your browser and go to:

http://localhost:8000

4. Interact with the Map
Click on any point to copy its coordinates to the clipboard.
The first point in the sorted list will be highlighted to indicate the starting point of your route.
Points are connected with a line to visualize the optimal route.
Notes
Make sure to run the Python script and start the HTTP server from the root directory of the project.
The coordinates file in the input folder should be a plain text file with one pair of coordinates per line.
