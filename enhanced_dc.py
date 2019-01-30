import sys
import math
import timeit
import helper


def closest_points(points_sorted_x,points_sorted_y):
    # num points (n)
    num_points = len(points_sorted_x)

    # the generic structure for every "result" object.
    #   result[0] - min distance
    #   result[1] - List of tuples containing every point that has the min distance.
    min_result = (None, [])

    # Base cases
    if num_points == 1:
        return min_result
    if num_points == 2:
        return helper.compare(points_sorted_x[0], points_sorted_x[1], min_result)

    # Median Index (point[med_index] = Xm)
    med_index = math.ceil(num_points/2)

    # Get subsets of the points for the two recursive calls. Held in their own variable to be sorted on y later.
    left_points_x = points_sorted_x[:med_index]
    right_points_x = points_sorted_x[med_index:]

        # get minimum and maximum x values in left list
    x_min_left = left_points_x[0][0]
    x_max_left = left_points_x[len(left_points_x)-1][0]

    # get points sorted by y in this x range
    left_points_y = helper.get_points_from_sorted_y(
        points_sorted_y,
        x_min_left,
        x_max_left)

    # get minimum and maximum x values in left list
    x_min_right = right_points_x[0][0]
    x_max_right = right_points_x[len(right_points_x)-1][0]
    
    # get points sorted by y in this x range
    right_points_y = helper.get_points_from_sorted_y(
        points_sorted_y,
        x_min_right,
        x_max_right)


    # left_result[0] (d1), right_result[0] (d2)
    # Recursive calls
    left_result = closest_points(left_points_x,left_points_y)
    right_result = closest_points(right_points_x,right_points_y)

    # min_result[0] (d)
    # compares the two recursive calls results and chooses the best result of the two. if they are the same,
    # keep them and combine the results.
    # O(n)
    min_result = helper.combine_results(left_result, right_result)

    # get X range of M ( [m_left_index, m_right_index])
    # m_left_index is index of last point that qualifies Xm-d
    # m_right_index is the last point that qualifies Xm+d
    m_left_index = m_right_index = 0

    # scan linearly until the point no longer is within the range
    for (index, point) in enumerate(right_points_x):
        if(abs(points[med_index][0] - point[0]) > min_result[0]):
            break
        m_right_index = index

    # scan linearly until a point is within the range
    for (index, point) in enumerate(left_points_x):
        if(abs(points[med_index][0] - point[0]) <= min_result[0]):
            m_left_index = index
            break

        # get minimum and maximum x values in left list
    x_min_left = left_points_x[0][0]
    x_max_left = left_points_x[len(left_points_x)-1][0]

    # get points sorted by y in this x range
    sorted_left_points_y = helper.get_points_from_sorted_y(
        left_points_y,
        x_min_left,
        x_max_left)

    # get minimum and maximum x values in left list
    x_min_right = right_points_x[0][0]
    x_max_right = right_points_x[len(right_points_x)-1][0]
    
    # get points sorted by y in this x range
    sorted_right_points_y = helper.get_points_from_sorted_y(
        right_points_y,
        x_min_right,
        x_max_right)

    #print('\n---\nTime: ', sorted_left_points_y_stop - sorted_left_points_y_timer)

    # map the indices of the sorted left and right point lists.
    # essentially, given some index i for a point in the left,
    # give the index i for the closest point in the y for the left.
    mapped_indices = helper.map_indices(
        sorted_left_points_y, sorted_right_points_y)

    # check for smaller distance in center.
    for point_index, src_point in enumerate(sorted_left_points_y):
        # compare points with y > src
        for dest_point in sorted_right_points_y[mapped_indices[point_index]:]:
            if min_result[0] != None and abs(dest_point[1] - src_point[1]) > min_result[0]:
                break
            min_result = helper.compare(src_point, dest_point, min_result)

        # compare points with y < src
        for dest_point in reversed(sorted_right_points_y[:mapped_indices[point_index]]):
            if min_result[0] != None and abs(dest_point[1] - src_point[1]) > min_result[0]:
                break
            min_result = helper.compare(src_point, dest_point, min_result)

    return min_result

# get input file from command argument
points = helper.parse_coords(sys.argv[1])

# sort points on x
sorted_points_x = sorted(points, key=lambda tup: tup[0])

# sort points on y
sorted_points_y = sorted(points, key=lambda tup: tup[1])

# do D&C call on the sorted points. Store the result.
start = timeit.default_timer()
final_result = closest_points(sorted_points_x,sorted_points_y)
stop = timeit.default_timer()

# use the pretty print to sort the results and print them.
helper.pp_results(final_result[0], final_result[1], "output_files/output_enhanced_dc.txt")

if(len(sys.argv) >= 3 and sys.argv[2] == "-v"):
    print('\n---\nTime: ', stop - start)
