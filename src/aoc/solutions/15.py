"""Advent of Code - 2021 Day 15"""

import curses
from heapq import heappop, heappush
import time

from aoc.curses import Color
from aoc.geometry import Grid, Point


def find_lowest_risk_path(grid, start, end, window=None):
    pos = start
    min_risks = {}
    best_paths = {}
    min_risks[start] = 0
    best_paths[start] = [start]
    candidates = [(start.manhattan_distance(end), 0, start)]

    while candidates:
        estimate, risk, candidate = heappop(candidates)
        if window:
            window.addstr(candidate.y, candidate.x * 2, str(grid[candidate]) * 2, curses.color_pair(Color.YELLOW))
            window.refresh()
            time.sleep(0.0001)
        if candidate == end:
            return risk, best_paths[candidate]

        for n in grid.neighbors(candidate):
            total_risk = risk + grid[n]
            if n not in min_risks or total_risk < min_risks[n]:
                min_risks[n] = total_risk
                best_paths[n] = best_paths[candidate] + [n]
                estimate = total_risk + n.manhattan_distance(end)
                heappush(candidates, (estimate, total_risk, n))
                if window:
                    window.addstr(n.y, n.x * 2, str(grid[n]) * 2, curses.color_pair(Color.RED))
        if window:
            window.refresh()
            time.sleep(0.0001)


def backtrack(path, grid, window):
    while path:
        pos = path.pop()
        risk = grid[pos]
        window.addstr(pos.y, pos.x * 2, "██", curses.color_pair(Color.WHITE))
        window.refresh()
        time.sleep(0.001)


def part1(input, window=None):
    grid = Grid.from_rows(input.lines(lambda l: map(int, l)))
    start = grid.topleft()
    end = grid.bottomright()
    risk, path = find_lowest_risk_path(grid, start, end, window)
    if window:
        backtrack(path, grid, window)
    return risk


def part2(input, window=None):
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
    risk, path = find_lowest_risk_path(grid, start, end, window)
    if window:
        backtrack(path, grid, window)
    return risk
