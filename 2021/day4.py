"""Day One"""

import itertools
import functools


def check_board(numbers: set, board):
    row_win = any([set(row).issubset(numbers) for row in board])
    columns = [{row[i] for row in board} for i in range(5)]
    column_win = any([column.issubset(numbers) for column in columns])
    return row_win or column_win


def score_board(numbers: set, board):
    return sum({x for row in board for x in row}.difference(numbers))


def part_one(numbers, boards):
    called_numbers = set()
    for number in numbers:
        called_numbers.add(number)
        for board in boards:
            if check_board(called_numbers, board):
                return score_board(called_numbers, board) * number


def part_two(numbers, boards):
    called_numbers = set(numbers)
    called_numbers = set(numbers)
    for number in numbers[::-1]:
        called_numbers.remove(number)
        for board in boards:
            if not check_board(called_numbers, board):
                called_numbers.add(number)
                return score_board(called_numbers, board) * number


with open('input4.txt') as f:
    numbers = [int(n) for n in f.readline().split(',')]
    board_lines = map(lambda s: list(map(int, s.split())), filter(
        lambda line: line != '\n', f))
    boards = [x for x in itertools.zip_longest(*[board_lines]*5)]

    print(part_one(numbers, boards))
    print(part_two(numbers, boards))
