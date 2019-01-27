import sys
import math
import helper


def closest_points(points):
    num_points = len(points)
    min_result = (None, [])

    # Base cases
    if num_points == 1:
        return min_result
    if num_points == 2:
        return helper.compare(points[0], points[1], min_result)

    # Median Index
    med_index = math.ceil(num_points/2)
    print(med_index)

    # Recursive calls TODO: check to see this is proper range
    left_result = closest_points(points[:med_index-1])
    right_result = closest_points(points[med_index:])

    min_result = helper.combine_results(left_result, right_result)

    sorted_y_points = sorted(points, key=lambda tup: tup[1])

    # check for smaller distance
    for point_index, src_point in enumerate(sorted_y_points):
        # compare points with y > src
        for dest_point in sorted_y_points[point_index+1:]:
            if min_result[0] != None and abs(dest_point[1] - src_point[1]) > min_result[0]:
                break
            min_result = helper.compare(src_point, dest_point, min_result)

        # compare points with y < src
        for dest_point in reversed(sorted_y_points[:point_index-1]):
            if abs(dest_point[1] - src_point[1]) > min_result[0]:
                break
            min_result = helper.compare(src_point, dest_point, min_result)

    return min_result


points = helper.parse_coords(sys.argv[1])
sorted_points = sorted(points, key=lambda tup: tup[0])

final_result = closest_points(sorted_points)
# print(final_result[0])
# for point in final_result[1]:
#     print(point[0][0], point[0][1], point[1][0], point[1][1])
