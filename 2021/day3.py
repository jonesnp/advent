"""Day One"""

import itertools
import functools


def gamma(numbers):
    sums = [0] * 12
    for number in numbers:
        for i in range(12):
            sums[i] += int(number[i])
    return ''.join(map(lambda x: '1' if x >= len(numbers)/2 else '0', sums))


def part_one(numbers):
    gm = int(gamma(numbers), 2)
    ep = ~gm & int('1'*12, 2)
    return gm * ep


def part_two(numbers):
    candidates = numbers.copy()
    oxy_rating = 0
    for i in range(12):
        gm = gamma(candidates)
        candidates = list(filter(lambda x: x[i] == gm[i], candidates))
        if len(candidates) == 1:
            oxy_rating = int(candidates[0],2)
    
    candidates = numbers.copy()
    co_rating = 0
    for i in range(12):
        ep = bin(~int(gamma(candidates), 2) & int('1'*12, 2))[2:].zfill(12)
        candidates = list(filter(lambda x: x[i] == ep[i], candidates))
        if len(candidates) == 1:
            co_rating = int(candidates[0],2)
    return oxy_rating * co_rating


with open('day3.txt') as f:
    numbers = [line.rstrip() for line in f]
    print(part_one(numbers))
    print(part_two(numbers))
