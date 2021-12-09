"""Day One"""

import collections
import itertools

def sliding_window(iterable, n):
    # it = iter(iterable)
    window = collections.deque(itertools.islice(iterable, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in iterable:
        window.append(x)
        yield tuple(window)

def part_one(measurements):
    """Part One Solution"""
    lst = list(sliding_window(measurements, 2))
    return len([True for (x,y) in lst if x < y])

def part_two(measurements):
    """Part Two Solution"""
    lst = sliding_window(sliding_window(measurements, 3),2)
    return len([True for (x,y) in lst if sum(x) < sum(y)])


with open('day1.txt') as f:
    numbers = map(int, list(f))
    one, two = itertools.tee(numbers)
    print(part_one(one))
    print(part_two(two))