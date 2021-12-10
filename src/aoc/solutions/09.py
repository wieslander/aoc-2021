"""Advent of Code - 2021 Day 9"""

import curses
import random
import time

from aoc.curses import visualize, Color
from aoc.geometry import Grid, Point


class OutputChar:
    def __init__(self, output, color, bold=False):
        self.output = output
        self.color = color
        self.bold = bold

    @property
    def attr(self):
        attr = curses.color_pair(self.color)
        if self.bold:
            attr |= curses.A_BOLD
        return attr


height_map = {
    8: OutputChar(".", Color.BLACK, bold=True),
    7: OutputChar("-", Color.MAGENTA, bold=True),
    6: OutputChar("+", Color.CYAN, bold=False),
    5: OutputChar("*", Color.YELLOW, bold=True),
    4: OutputChar('=', Color.GREEN, bold=True),
    3: OutputChar('#', Color.GREEN, bold=False),
    2: OutputChar('$', Color.YELLOW, bold=False),
    1: OutputChar("&", Color.MAGENTA, bold=False),
    0: OutputChar("@", Color.RED, bold=True),
}


def get_low_points(grid):
    for pos, value in grid.items():
        if all(grid[n] is None or grid[n] > value for n in pos.neighbors()):
            yield pos, value


def get_basins(grid, window=None):
    low_points = list(get_low_points(grid))
    random.shuffle(low_points)

    for pos, value in low_points:
        basin = set()
        candidates = set([pos])

        while candidates:
            c = candidates.pop()
            if c in basin:
                continue

            height = grid[c]
            if height is not None and height < 9:
                basin.add(c)
                candidates.update(c.neighbors())

                if window:
                    char = height_map[height]
                    window.addstr(c.y, c.x * 2, char.output * 2, char.attr)
                    window.refresh()
                    time.sleep(0.005)

        yield basin


def part1(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    low_points = get_low_points(grid)
    risk_levels = [height + 1 for _, height in low_points]
    return sum(risk_levels)


def part2(input, window=None):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    basins = sorted(get_basins(grid, window), key=lambda b: -len(b))
    return len(basins[0]) * len(basins[1]) * len(basins[2])


def part2_visualization(input):
    return visualize(part2, input)
