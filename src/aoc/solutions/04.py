"""Advent of Code - 2021 Day 4"""

import curses
import functools
import itertools
import time

from aoc.curses import Color
from aoc.geometry import Point


class Board:
    def __init__(self, rows, index):
        self.rows = [[(n, False) for n in row] for row in rows]
        self.index = index

    def check(self, n):
        self.rows = [
            [(x, checked or x == n) for x, checked in row]
            for row in self.rows
        ]

    def has_bingo(self):
        if any(all(checked for _, checked in row) for row in self.rows):
            return True

        for col in range(5):
            if all(row[col][1] for row in self.rows):
                return True

        return False

    def unmarked_numbers(self):
        return [n for n, checked in itertools.chain(*self.rows) if not checked]

    def is_bingo_square(self, pos):
        row = self.rows[pos.y]
        try:
            n, checked = row[pos.x]
        except Exception as e:
            print(row)
            print(pos.x)
            raise e

        if all(checked for _, checked in row):
            return True
        elif all(squares[pos.x][1] for squares in self.rows):
            return True

        return False

    def render(self, window, current_number):
        board_offset = self.get_board_offset(window)

        for row, squares in enumerate(self.rows):
            for col, (n, checked) in enumerate(squares):
                x = board_offset.x + col * 3
                y = board_offset.y + row
                s = f'{n:>2d}'

                color = Color.BLUE

                if self.is_bingo_square(Point(col, row)):
                    color = Color.RED
                elif self.has_bingo():
                    color = Color.WHITE
                elif checked:
                    color = Color.YELLOW

                attr = curses.color_pair(color)
                if n == current_number:
                    attr |= curses.A_REVERSE
                window.addstr(y, x, s, attr)

    def get_board_offset(self, window):
        global_offset = Board.get_global_offset(window)
        local_offset = self.get_local_offset()
        return global_offset + local_offset

    def get_local_offset(self):
        x = (self.index // 10) * 17
        y = (self.index % 10) * 6
        return Point(x, y)

    @staticmethod
    def get_global_offset(window):
        total_width = 167
        total_height = 59
        max_y, max_x = window.getmaxyx()
        x_offset = (max_x - total_width) // 2
        y_offset = (max_y - total_height) // 2
        return Point(x_offset, y_offset)


def parse_bingo_boards(lines):
    boards = []
    index = 0

    while len(lines) >= 1:
        rows = [[int(n) for n in line.split()] for line in lines[:5]]
        boards.append(Board(rows, index=index))
        lines[:6] = []
        index += 1

    return boards


def part1(input, window=None):
    lines = input.lines()
    numbers = [int(n) for n in lines[0].split(',')]
    boards = parse_bingo_boards(lines[2:])

    score = None

    for n in numbers:
        for board in boards:
            board.check(n)
            if board.has_bingo():
                score = sum(board.unmarked_numbers()) * n

            if window:
                board.render(window, n)

            if score is not None:
                break

        if window:
            window.refresh()
            time.sleep(0.1)

        if score is not None:
            break

    return score


def part2(input, window=None):
    lines = input.lines()
    numbers = [int(n) for n in lines[0].split(',')]
    boards = parse_bingo_boards(lines[2:])
    last_score = None

    for n in numbers:
        for index, board in enumerate(boards):
            if board.has_bingo():
                continue

            board.check(n)
            if board.has_bingo():
                last_score = sum(board.unmarked_numbers()) * n

            if window:
                board.render(window, n)

        if window:
            window.refresh()
            time.sleep(0.1)

    return last_score
