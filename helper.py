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

def distance(p1,p2):
        dist_x = p2[0]-p1[0]
        dist_y = p2[1]-p1[1]
        dist = math.sqrt(dist_x**2 + dist_y**2)
        return(dist)