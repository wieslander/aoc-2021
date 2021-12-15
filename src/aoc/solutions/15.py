"""Advent of Code - 2021 Day 15"""

from heapq import heappop, heappush

from aoc.geometry import Grid, Point


def find_lowest_risk_path(grid, start, end):
    min_risks = {}
    pos = start
    min_risks[start] = 0
    candidates = [(0, start)]

    while candidates:
        risk, candidate = heappop(candidates)
        if candidate == end:
            return risk

        for n in grid.neighbors(candidate):
            total_risk = risk + grid[n]
            if n not in min_risks or total_risk < min_risks[n]:
                min_risks[n] = total_risk
                heappush(candidates, (total_risk, n))


def part1(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    start = grid.topleft()
    end = grid.bottomright()
    return find_lowest_risk_path(grid, start, end)


def part2(input):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    width = grid.width()
    height = grid.height()

    for p, risk in list(grid.items()):
        for x in range(5):
            for y in range(5):
                new_pos = p + Point(x * width, y * height)
                new_risk = (risk + x + y) % 9
                if new_risk == 0:
                    new_risk = 9
                grid[new_pos] = new_risk

    start = grid.topleft()
    end = grid.bottomright()
    return find_lowest_risk_path(grid, start, end)
