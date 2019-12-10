import collections
import math

Position = collections.namedtuple('Position', 'x y')


def manhattan(start, end):
    return abs(start.x - end.x) + abs(start.y - end.y)


def tracepath(location, direction, units, path):
    for unit in range(1, units + 1):
        if direction == 'D':
            path.append(Position(location.x, location.y - unit))
        elif direction == 'U':
            path.append(Position(location.x, location.y + unit))
        elif direction == 'L':
            path.append(Position(location.x - unit, location.y))
        elif direction == 'R':
            path.append(Position(location.x + unit, location.y))


with open('3.dat') as f:
    wire1, wire2, *_ = f.readlines()

wire1 = wire1.split(',')
wire2 = wire2.split(',')

wire1_location = Position(0, 0)
wire1_path = []
for instruction in wire1:
    direction, units = instruction[0], int(instruction[1:])
    tracepath(wire1_location, direction, units, wire1_path)
    wire1_location = wire1_path[-1]

wire2_location = Position(0, 0)
wire2_path = []
for instruction in wire2:
    direction, units = instruction[0], int(instruction[1:])
    tracepath(wire2_location, direction, units, wire2_path)
    wire2_location = wire2_path[-1]

intersections = set(wire1_path).intersection(set(wire2_path))

most_efficient = math.inf
for intersection in intersections:
    efficiency = wire1_path.index(intersection) + wire2_path.index(intersection) + 2
    most_efficient = efficiency if efficiency < most_efficient else most_efficient
print(most_efficient)

shortest = math.inf
origin = Position(0, 0)
for intersection in intersections:
    distance = manhattan(origin, intersection)
    shortest = distance if distance < shortest else shortest
print(shortest)
