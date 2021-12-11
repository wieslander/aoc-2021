import importlib
import sys

from aoc.input import Input
import aoc.curses

def run(day, part, input_file=None, visualize=False):
    pkg = importlib.import_module(f"aoc.solutions.{day:02d}")

    input = Input(day, input_file)

    if part == 1:
        if visualize:
            print(aoc.curses.visualize(pkg.part1, input))
        else:
            print(pkg.part1(input))
    elif part == 2:
        if visualize:
            print(aoc.curses.visualize(pkg.part2, input))
        else:
            print(pkg.part2(input))
    else:
        print("Invalid part", file=sys.stderr)
        sys.exit(1)
