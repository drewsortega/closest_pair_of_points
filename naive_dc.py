import sys
import math
import timeit
import helper


def closest_points(points):
    # num points (n)
    num_points = len(points)

    # the generic structure for every "result" object.
    #   result[0] - min distance
    #   result[1] - List of tuples containing every point that has the min distance.
    min_result = (None, [])

    # Base cases
    if num_points == 1:
        return min_result
    if num_points == 2:
        return helper.compare(points[0], points[1], min_result)

    # Median Index (point[med_index] = Xm)
    med_index = math.ceil(num_points/2)
    med_point = points[med_index]

    # Get subsets of the points for the two recursive calls. Held in their own variable to be sorted on y later.
    left_points = points[:med_index]
    right_points = points[med_index:]

    # left_result[0] (d1), right_result[0] (d2)
    # Recursive calls
    left_result = closest_points(left_points)
    right_result = closest_points(right_points)

    # min_result[0] (d)
    # compares the two recursive calls results and chooses the best result of the two. if they are the same,
    # keep them and combine the results.
    # O(n)
    min_result = helper.combine_results(left_result, right_result)

    # get left points within the proper range on x, sorted by y
    points_y = sorted(
        points,
        key=lambda tup: tup[1]
    )

    # get deviation between delta
    dev_max = float(med_point[0])+min_result[0]
    dev_min = float(med_point[0])-min_result[0]

    points_center_y = []
    for point in points_y:
        if(point[0] >= dev_min and point[0] <= dev_max):
            points_center_y.append(point)
    num_in_center = len(points_center_y)
    for (i1, point1) in enumerate(points_center_y):
        # maximum of 8 iterations
        for point2 in points_center_y[i1+1:min(num_in_center, 8+i1)]:
            min_result = helper.compare(point1, point2, min_result)

    return min_result


# get input file from command argument
points = helper.parse_coords(sys.argv[1])

# sort points on x
sorted_points_x = sorted(points, key=lambda tup: tup[0])

# do D&C call on the sorted points. Store the result.
start = timeit.default_timer()
final_result = closest_points(sorted_points_x)
stop = timeit.default_timer()

# use the pretty print to sort the results and print them.
helper.pp_results(final_result[0], final_result[1],
                  "output_files/output_naive_dc.txt")

if(len(sys.argv) >= 3 and sys.argv[2] == "-v"):
    print('\n---\nTime: ', stop - start)
