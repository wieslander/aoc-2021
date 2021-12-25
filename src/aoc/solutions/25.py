"""Advent of Code - 2021 Day 25"""

from aoc.geometry import Grid, Point


def move(grid):
    width = grid.width()
    height = grid.height()
    move_east = {}
    move_south = {}

    for pos, value in grid.items():
        if value == '>':
            next_pos = pos + Point(1, 0)
            next_pos.x %= width
            if grid[next_pos] == '.':
                move_east[pos] = next_pos

    for pos, next_pos in move_east.items():
        grid[pos] = '.'
        grid[next_pos] = '>'

    for pos, value in grid.items():
        if value == 'v':
            next_pos = pos + Point(0, 1)
            next_pos.y %= height
            if grid[next_pos] == '.':
                move_south[pos] = next_pos

    for pos, next_pos in move_south.items():
        grid[pos] = '.'
        grid[next_pos] = 'v'

    return bool(move_east) or bool(move_south)


def part1(input):
    grid = Grid.from_rows(input.lines())
    steps = 1
    while move(grid):
        steps += 1
    return steps


def part2(input):
    pass
