from collections import namedtuple
import math
import curses
from curses import wrapper
import time

with open('10.dat') as f:
    asteroid_map = f.read().splitlines()

Size = namedtuple('size', 'h w')
Coords = namedtuple('coordinates', 'x y')
size = Size(len(asteroid_map[0]), len(asteroid_map))

def get_asteroids(asteroid_map):
    return [Coords(x, y) for y in range(size.h) for x in range(size.w) if asteroid_map[y][x] == '#']

def get_angle(target, source):
    angle = math.degrees(math.atan2(target.y - source.y, target.x - source.x))
    if angle < 0:
        angle += 360
    if angle < 270:
        angle += 360
    return angle

asteroids = get_asteroids(asteroid_map)
best = Coords(19,11)

ast_dict = {}
for asteroid in asteroids:
    if asteroid != best:
        angle = get_angle(asteroid, best)
        if angle in ast_dict:
            ast_dict[angle] += [asteroid]
        else:
            ast_dict[angle] = [asteroid]

def dist(e):
    return abs(e.x - best.x) + abs(e.y - best.y)

for k in ast_dict:
    ast_dict[k] = sorted(ast_dict[k], key=dist)

print('Part 1: ', len(ast_dict.keys()))

vaporized = 0
for k in sorted(ast_dict.keys()):
    if ast_dict[k]:
        if vaporized < 199:
            vaporized += 1
            del ast_dict[k][0]
        else:
            final = ast_dict[k][0]
            print('Part 2: ', final.x * 100 + final.y)
            # break