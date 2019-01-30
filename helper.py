#!/usr/bin/python
import os
import math
import random


def parse_coords(file_path):
    coords = []
    input_file = open(file_path, mode='r', encoding="utf-8")
    for line in input_file:
        pair_str = line.split()
        if (len(pair_str) == 2):
            coords.append((int(pair_str[0]), int(pair_str[1])))
    input_file.close()
    return(coords)


def distance(p1, p2):
    dist_x = p2[0]-p1[0]
    dist_y = p2[1]-p1[1]
    dist = math.sqrt(dist_x**2 + dist_y**2)
    return(dist)


def swap_tuple(tup):
    return((tup[1], tup[0]))


def map_indices(points1, points2):
    current_index = 0
    mapped_indices = []
    for (index, point) in enumerate(points2):
        if len(mapped_indices) == len(points1):
            return mapped_indices
        if point[1] >= points1[current_index][1]:
            mapped_indices.append(index)
            current_index += 1
    while(len(mapped_indices) < len(points1)):
        mapped_indices.append(len(points2)-1)
    return mapped_indices


def sort_results(results):
    # organize the points so the smaller point is first
    for idx,result in enumerate(results):
        if (result[0][0] > result[1][0]):
            results[idx] = swap_tuple(result)            
        elif (result[0][0] == result[1][0]):
            # if same x, choose point with lower y coord
            if (result[0][1] > result[1][1]):
                results[idx] = swap_tuple(result)
    # organize the list of tuples
    results.sort(key=lambda tup: (tup[0], tup[1]))
    return(results)

def pp_results(min_result,points,file_path):
    if not os.path.exists("output_files"):
        os.makedirs("output_files")
    output = open(file_path,"w")
    sorted_points = sort_results(points)
    output.write("%f\n" % min_result)
    for point in sorted_points:
        output.write("%d %d %d %d\n" % (point[0][0], point[0][1], point[1][0],point[1][1]))
    output.close()

def compare(p1, p2, min_result):
    dist = distance(p1, p2)
    if min_result[0] == None or dist < min_result[0]:
        min_result = (dist, [(p1, p2)])
    elif dist == min_result[0]:
        min_result[1].append((p1, p2))
    return min_result


def combine_results(res1, res2):
    if res2[0] == None:
        return res1
    if res1[0] == res2[0]:
        for point in res2[1]:
            res1[1].append(point)
    elif res1[0] == None or res2[0] < res1[0]:
        return res2
    return res1


def generate_sample_set(size,file_path):
    # generate samples
    points = []
    x_points = random.sample(range(1, 1000000), size)
    y_points = random.sample(range(1, 1000000), size)
    for x_point, y_point, in zip(x_points,y_points):
        points.append((x_point,y_point))
    # write them to a file
    if not os.path.exists("randomly_generated_points"):
        os.makedirs("randomly_generated_points")
    output = open(file_path,"w")
    for point in points:
        output.write("%d %d\n" % (point[0], point[1]))
    output.close()

# run this to create 4 sample sets of sizes 100, 1000, 10000, and 100000
def create_samples():
    sample_sizes = [10**2,10**3,10**4,10**5]
    sample_file_names = ["100_points.txt","1000_points.txt","10000_points.txt","100000_points.txt"]
    for size,name in zip(sample_sizes,sample_file_names):
        generate_sample_set(size,"randomly_generated_points/%s" % name)

