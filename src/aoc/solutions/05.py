"""Advent of Code - 2021 Day 5"""


from aoc.geometry import Line, Point, Grid


def parse_line(s):
    start_string, end_string = s.split(' -> ')
    start = Point.from_csv(start_string)
    end = Point.from_csv(end_string)
    return Line(start, end)


def part1(input):
    lines = input.lines(parse_line)
    grid = Grid()

    for line in lines:
        if line.start.x == line.end.x or line.start.y == line.end.y:
            for pos in line.points():
                line_count = grid.get(pos, 0) + 1
                grid.set(pos, line_count)

    overlapping_points = [v for v in grid.values() if v >= 2]
    return len(overlapping_points)


def part2(input):
    lines = input.lines(parse_line)
    grid = Grid()

    for line in lines:
        for pos in line.points():
            line_count = grid.get(pos, 0) + 1
            grid.set(pos, line_count)

    overlapping_points = [v for v in grid.values() if v >= 2]
    return len(overlapping_points)
