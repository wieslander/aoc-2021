import importlib
import sys

from aoc.input import Input

def run(day, part):
    pkg = importlib.import_module(f"aoc.solutions.{day:02d}")

    input = Input(day)

    if part == 1:
        print(pkg.part1(input))
    elif part == 2:
        print(pkg.part2(input))
    else:
        print("Invalid part", file=sys.stderr)
        sys.exit(1)
