"""Advent of Code - 2021 Day 9"""

from aoc.geometry import Grid, Point

def get_low_points(grid):
    for pos, value in grid.items():
        if all(grid[n] is None or grid[n] > value for n in pos.neighbors()):
            yield pos, value


def get_basins(grid):
    for pos, value in get_low_points(grid):
        basin = set([pos])
        candidates = set(pos.neighbors())

        while candidates:
            c = candidates.pop()
            if c in basin:
                continue

            height = grid[c]
            if height is not None and height < 9:
                basin.add(c)
                candidates.update(c.neighbors())

        yield basin


def part1(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    low_points = get_low_points(grid)
    risk_levels = [height + 1 for _, height in low_points]
    return sum(risk_levels)


def part2(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    basins = sorted(get_basins(grid), key=lambda b: -len(b))
    return len(basins[0]) * len(basins[1]) * len(basins[2])
