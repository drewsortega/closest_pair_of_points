import sys
import math
import helper

input_file = sys.argv[1]
coordinates = helper.parse_coords(input_file)
min_distance = None
min_distance_points = []

for src_idx, source in enumerate(coordinates):
    for dest in coordinates[src_idx:]:
        if (dest != source):
            # First point
            if (min_distance == None):
                min_distance = helper.distance(source, dest)
                min_distance_points.append((source,dest))
            else:
                distance = helper.distance(source, dest)
                # Found a pair with the same distance
                if (distance == min_distance):
                    min_distance_points.append((source,dest))
                # Found a smaller distance
                elif (distance < min_distance):
                    min_distance = distance
                    min_distance_points.clear()
                    min_distance_points.append((source,dest))

helper.pp_results(min_distance,min_distance_points)