"""Advent of Code - 2021 Day 4"""

import itertools


class Board:
    def __init__(self, rows):
        self.rows = rows

    def check(self, n):
        self.rows = [[x if x != n else 'x' for x in row] for row in self.rows]

    def has_bingo(self):
        if any(all(n == 'x' for n in row) for row in self.rows):
            return True

        for col in range(5):
            if all(row[col] == 'x' for row in self.rows):
                return True

        return False

    def unmarked_numbers(self):
        return [n for n in itertools.chain(*self.rows) if n != 'x']


def parse_bingo_boards(lines):
    boards = []

    while len(lines) >= 1:
        rows = [[int(n) for n in line.split()] for line in lines[:5]]
        boards.append(Board(rows))
        lines[:6] = []

    return boards


def part1(input):
    lines = input.lines()
    numbers = [int(n) for n in lines[0].split(',')]
    boards = parse_bingo_boards(lines[2:])

    for n in numbers:
        for board in boards:
            board.check(n)
            if board.has_bingo():
                return sum(board.unmarked_numbers()) * n


def part2(input):
    lines = input.lines()
    numbers = [int(n) for n in lines[0].split(',')]
    boards = parse_bingo_boards(lines[2:])
    last_score = None

    for n in numbers:
        for board in boards:
            if board.has_bingo():
                continue

            board.check(n)
            if board.has_bingo():
                last_score = sum(board.unmarked_numbers()) * n

    return last_score
