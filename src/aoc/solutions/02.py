"""Advent of Code - 2021 Day 2"""

import sys


class Command:
    def __init__(self, line):
        self.command, self.distance = line.split()
        self.distance = int(self.distance)


def part1(input):
    course = input.lines(Command)
    horizontal = sum(c.distance for c in course if c.command == "forward")
    down = sum(c.distance for c in course if c.command == "down")
    up = sum(c.distance for c in course if c.command == "up")

    return horizontal * (down - up)


def part2(input):
    course = input.lines(Command)
    aim = 0
    depth = 0
    horizontal = 0

    for cmd in course:
        if cmd.command == "down":
            aim += cmd.distance
        elif cmd.command == "up":
            aim -= cmd.distance
        elif cmd.command == "forward":
            horizontal += cmd.distance
            depth += cmd.distance * aim
        else:
            print(f"Invalid command: {cmd.command}", file=sys.stderr)
            sys.exit(1)

    return horizontal * depth
