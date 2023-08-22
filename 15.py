import os
import re
from scipy.spatial import cKDTree

def read_file_as_list(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []

puzz_input = read_file_as_list('15_input.txt')


def parse_puzz_input(file_path):
    """
    read the txt file and convert it to a list of tuples
    :param file_path:
    :return:
    """
    puzz_input = read_file_as_list(file_path)

    sensor_positions = list()

    beacon_positions = list()

    for line in puzz_input:
        line = line.split(': ')

        sensor, beacon = [re.findall(pattern=r'\d+', string=l) for l in line]

        sensor = [int(s) for s in sensor]
        beacon = [int(b) for b in beacon]

        sensor_positions.append(tuple(sensor))
        beacon_positions.append(tuple(beacon))


    return sensor_positions, beacon_positions

sensor_positions, beacon_positions = parse_puzz_input('15_input.txt')


def define_grid_size(sensor_positions, beacon_positions):
    max_x_sensor = max(sensor_positions, key=lambda item: item[0])[0]
    max_y_sensor = max(sensor_positions, key=lambda item: item[0])[1]

    max_x_beacon = max(beacon_positions, key=lambda item: item[0])[0]
    max_y_beacon = max(beacon_positions, key=lambda item: item[0])[1]

    max_x = max([max_x_sensor, max_x_beacon])
    max_y = max([max_y_sensor, max_y_beacon])


    min_x_sensor = min(sensor_positions, key=lambda item: item[0])[0]
    min_y_sensor = min(sensor_positions, key=lambda item: item[0])[1]

    min_x_beacon = min(beacon_positions, key=lambda item: item[0])[0]
    min_y_beacon = min(beacon_positions, key=lambda item: item[0])[1]

    min_x = min([min_x_sensor, min_x_beacon])
    min_y = min([min_y_sensor, min_y_beacon])

    return [(max_x, max_y), (min_x, min_y)]


sensor = sensor_positions[0]
beacon = beacon_positions[0]

def sensor_calculate_monitored_positions(sensor: tuple,
                                         beacon: tuple):
    """
    calculates the monitored positions on the grid of one sensor, based on its closest beacon
    :param sensor: tuple
    :param beacon: tuple
    :return:
    """
    x_diff = abs(sensor[0]) + abs(beacon[0])
    y_diff = abs(sensor[1]) + abs(beacon[1])



def taxicab_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])






def points_within_distance(center_point, distance):
    result = []
    x, y = center_point

    for dx in range(-distance, distance + 1):
        print(dx/distance)
        max_dy = distance - abs(dx)
        for dy in range(-max_dy, max_dy + 1):
            result.append((x + dx, y + dy))

    return result

center = (3, 4)
distance = 2
points_within = points_within_distance(center, distance)
print(points_within)

### TOO SLOW - DOING IT WITH A QUAD TREE STRUCTURE ###

from scipy.spatial import cKDTree

# Create a large grid of points
# You would replace this with your actual data
grid_points = [(x, y) for x in range(1000) for y in range(1000)]

grid_points = sensor_positions


# Create a KDTree
kdtree = cKDTree(grid_points)

def points_within_distance(point, distance):
    indices = kdtree.query_ball_point(point, distance)
    return [grid_points[idx] for idx in indices]

center = (300, 400)
distance = 200
points_within = points_within_distance(center, distance)
print(points_within)

points_within = points_within_distance(sensor, distances[0])
print(points_within)




def create_kdtree(input_data):
    points = [point for point in input_data]
    return cKDTree(points)


def points_not_within_input_distances(row_index, input_data, x_range):
    row_points = [(row_index, y) for y in range(x_range)]  # Adjust the range according to your grid size

    kdtree = create_kdtree(input_data)

    # Find points within each distance and accumulate their indices
    indices = []
    for point, distance in input_data:
        indices_within_distance = kdtree.query_ball_point(point, distance)
        indices.extend(indices_within_distance)

    # Remove duplicates from indices
    indices = list(set(indices))

    # Return all points in the row
    all_points_in_row = row_points

    # Filter out points within the distances
    not_within_points = [point for i, point in enumerate(all_points_in_row) if i not in indices]

    return not_within_points


# Example input data: list of points with associated distances
input_data = [((3, 4), 5), ((10, 20), 10)]
row_index = 5  # Adjust this to the desired row index
points_not_within = points_not_within_input_distances(row_index, input_data, 100)
print(points_not_within)


distances = [taxicab_distance(s, b) for s, b in zip(sensor_positions, beacon_positions)]
# input_data = zip(beacon_positions, distances)

input_data = [tuple(b, d) for b, d in (sensor_positions, distances)]

grid_limits = define_grid_size(sensor_positions, beacon_positions)
x_range = abs(grid_limits[0][0]-grid_limits[1][0])

row_index = 2000000
points_not_within = points_not_within_input_distances(row_index, input_data, x_range)
print(points_not_within)





def points_within_input_distances(row_index, sensor_positions, distances, x_range):
    row_points = [(row_index, y) for y in range(x_range)]  # Adjust the range according to your grid size

    kdtree = cKDTree(sensor_positions)

    # Find points within each distance and accumulate their indices
    indices = set()
    for point, distance in sensor_positions, distances:
        indices_within_distance = kdtree.query_ball_point(point, distance)
        indices.update(indices_within_distance)

    # Get the points within the distances
    within_points = {row_points[i] for i in indices}

    return within_points


row_index = 2000000
points_within_distances = points_within_input_distances(row_index, sensor_positions, distances, x_range)
print(points_within_distances)
