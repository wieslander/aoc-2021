"""Advent of Code - 2021 Day 11"""

from aoc.geometry import Grid


def simulate_step(grid):
    flash_stack = []

    for pos in grid:
        grid[pos] += 1
        if grid[pos] > 9:
            flash_stack.append(pos)

    while flash_stack:
        pos = flash_stack.pop()

        for n in pos.neighbors(diagonal=True):
            if n in grid and grid[n] <= 9:
                grid[n] += 1
                if grid[n] > 9:
                    flash_stack.append(n)

    flash_count = 0
    for pos in grid:
        if grid[pos] > 9:
            grid[pos] = 0
            flash_count += 1

    return flash_count


def part1(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    return sum(simulate_step(grid) for _ in range(100))


def part2(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    step = 0
    while True:
        step += 1
        flash_count = simulate_step(grid)
        if flash_count == len(grid):
            return step
