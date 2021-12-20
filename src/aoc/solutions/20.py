"""Advent of Code - 2021 Day 20"""

from itertools import cycle
from aoc.geometry import Grid, Point


def parse_input(input):
    lines = input.lines()
    enhancement_map = lines[0]
    grid = Grid.from_rows(lines[2:], lambda: '.')
    return enhancement_map, grid


def enhance_grid(grid, enhancement_map, default):
    top_left = grid.top_left()
    bottom_right = grid.bottom_right()
    output_grid = Grid(lambda: default)

    for x in range(top_left.x - 1, bottom_right.x + 2):
        for y in range(top_left.y - 1, bottom_right.y + 2):
            p = Point(x, y)
            enhancement_index = get_enhancement_index(grid, p)
            output_grid[p] = enhancement_map[enhancement_index]

    return output_grid


def get_enhancement_index(grid, pos):
    enhancement_index = 0

    for y in range(pos.y - 1, pos.y + 2):
        for x in range(pos.x - 1, pos.x + 2):
            enhancement_index = enhancement_index << 1
            p = Point(x, y)
            if grid[p] == '#':
                enhancement_index += 1

    return enhancement_index


def part1(input):
    enhancement_map, grid = parse_input(input)

    for _ in range(2):
        grid = enhance_grid(grid, enhancement_map)

    return sum([v =='#' for v in grid.values()])


def part2(input):
    enhancement_map, grid = parse_input(input)
    if enhancement_map[0] == '#':
        defaultvalues = cycle([enhancement_map[0], enhancement_map[-1]])
        defaultfactory = lambda: next(defaultvalues)
    else:
        defaultfactory = lambda: None

    for _ in range(50):
        default = defaultfactory()
        grid = enhance_grid(grid, enhancement_map, default)

    return sum([v =='#' for v in grid.values()])
