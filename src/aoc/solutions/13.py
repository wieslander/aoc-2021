"""Advent of Code - 2021 Day 13"""

from aoc.geometry import Grid, Point


def parse_input(input):
    grid = Grid(lambda: '.')
    folds = []

    for line in input.lines():
        if line.startswith("fold along"):
            folds.append(parse_fold(line))
        elif line:
            p = Point.from_csv(line)
            grid[p] = '#'

    return grid, folds


def parse_fold(line):
    fold_text = line.replace('fold along ', '')
    axis, pos = fold_text.split('=')
    return axis, int(pos)


def fold(grid, axis, line):
    for pos in list(grid):
        mirror_pos = None
        if axis == 'x' and pos.x > line:
            mirror_x = line * 2 - pos.x
            mirror_pos = Point(mirror_x, pos.y)
        elif axis == 'y' and pos.y > line:
            mirror_y = line * 2 - pos.y
            mirror_pos = Point(pos.x, mirror_y)

        if mirror_pos:
            del grid[pos]
            grid[mirror_pos] = '#'


def part1(input):
    grid, folds = parse_input(input)
    axis, fold_line = folds[0]

    fold(grid, axis, fold_line)

    return len(grid)


def part2(input):
    grid, folds = parse_input(input)

    for axis, fold_line in folds:
        fold(grid, axis, fold_line)

    return grid
