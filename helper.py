#!/usr/bin/python
import math


def parse_coords(file_path):
    coords = []

    input_file = open(file_path, mode='r', encoding="utf-8")
    for line in input_file:
        pair_str = line.split()
        if (len(pair_str) == 2):
            coords.append((int(pair_str[0]), int(pair_str[1])))
    input_file.close()

    return(coords)


def compare(p1, p2, min_result):
    dist = distance(p1, p2)
    if dist < min_result[0]:
        min_result = (dist, [(p1, p2)])
    if dist == min_result[0]:
        min_result[0].append((p1, p2))
    return min_result


def combine_results(res1, res2):
    if res1[0] == res2[0]:
        for point in res2[1]:
            res1[1].append(point)
    elif res2[0] < res1[0]:
        return res2
    return res1


def distance(p1, p2):
    dist_x = p2[0]-p1[0]
    dist_y = p2[1]-p1[1]
    dist = math.sqrt(dist_x**2 + dist_y**2)
    return(dist)
