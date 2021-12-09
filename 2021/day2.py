"""Day One"""

import itertools
import functools

forward = 'forward'
down = 'down'
up = 'up'

def parseCommand(command):
    word, distance = command.split()
    if word == forward:
        return (int(distance), 0)
    elif word == down:
        return (0, int(distance))
    else:
        return (0, -int(distance))

def parseCommandTwo(command):
    word, distance = command.split()
    if word == forward:
        return (int(distance), int(distance), 0)
    elif word == down:
        return (0, 0, int(distance))
    else:
        return (0, 0, -int(distance))

def applyCommand(a, b):
    return (a[0] + b[0], a[1] + b[1])

def applyCommandTwo(a,b):
    return (a[0] + b[0], a[1] + (a[2] * b[1]), a[2] + b[2])


def part_one(commands):
    res = functools.reduce(applyCommand, map(parseCommand, commands))
    return res[0] * res[1]

def part_two(commands):
    res = functools.reduce(applyCommandTwo, map(parseCommandTwo, commands), (0,0,0))
    return res[0] * res[1]



with open('day2.txt') as f:
    commands = list(f)
    one, two = itertools.tee(commands)
    print(part_one(one))
    print(part_two(two))