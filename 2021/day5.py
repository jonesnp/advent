"""Day One"""

import itertools
import functools


def build_map(lines, diagonal=False):
    map = [[0]*1000 for _ in range(1000)]

    for start, end in lines:
        if start[0] == end[0]:
            x = start[0]
            increment = -1 if start[1] > end[1] else 1
            for y in range(start[1], end[1] + increment, increment):
                map[x][y] += 1
        elif start[1] == end[1]:
            y = start[1]
            increment = -1 if start[0] > end[0] else 1
            for x in range(start[0], end[0] + increment, increment):
                map[x][y] += 1
        elif diagonal:
            x_increment = -1 if start[0] > end[0] else 1
            y_increment = -1 if start[1] > end[1] else 1
            y = start[1]
            for x in range(start[0], end[0] + x_increment, x_increment):
                map[x][y] += 1
                y += y_increment
    return map



def part_one(lines):
    points = [point for line in build_map(lines) for point in line]
    return len(list(filter(lambda x: x >= 2, points)))

def part_two(lines):
    points = [point for line in build_map(lines, True) for point in line]
    return len(list(filter(lambda x: x >= 2, points)))

with open('input5.txt') as f:
    lines = [tuple(tuple(map(int,x.split(','))) for x in line.split('->')) for line in f]
    res = part_one(lines)
    print(res)
    res = part_two(lines)
    print(res)