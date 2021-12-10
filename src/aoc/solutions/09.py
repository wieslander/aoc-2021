"""Advent of Code - 2021 Day 9"""

import curses
import random
import time

from aoc.curses import visualize, Color
from aoc.geometry import Grid, Point


char_width = 2
height_map = {
    8: Color.BLUE,
    7: Color.BLUE,
    6: Color.CYAN,
    5: Color.GREEN,
    4: Color.YELLOW,
    3: Color.YELLOW,
    2: Color.MAGENTA,
    1: Color.MAGENTA,
    0: Color.RED,
}


def render_grid(grid, window):
    for pos, height in grid.items():
        s = str(height) * char_width
        attr = curses.color_pair(Color.BLACK) | curses.A_BOLD
        window.addstr(pos.y, pos.x * char_width, s, attr)
    window.refresh()


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
                    attr = curses.color_pair(height_map[height])
                    s = str(height) * char_width
                    window.addstr(c.y, c.x * char_width, s, attr)
                    window.refresh()
                    time.sleep(0.004)

        yield basin


def part1(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    low_points = get_low_points(grid)
    risk_levels = [height + 1 for _, height in low_points]
    return sum(risk_levels)


def part2(input, window=None):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    if window:
        render_grid(grid, window)
    basins = sorted(get_basins(grid, window), key=lambda b: -len(b))
    return len(basins[0]) * len(basins[1]) * len(basins[2])


def part2_visualization(input):
    return visualize(part2, input)
