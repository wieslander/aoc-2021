import importlib
import sys

from aoc.input import Input

def run(day, part, input_file=None, visualize=False):
    pkg = importlib.import_module(f"aoc.solutions.{day:02d}")

    input = Input(day, input_file)

    if part == 1:
        if visualize and hasattr(pkg, 'part1_visualization'):
            print(pkg.part1_visualization(input))
        else:
            print(pkg.part1(input))
    elif part == 2:
        if visualize and hasattr(pkg, 'part2_visualization'):
            print(pkg.part2_visualization(input))
        else:
            print(pkg.part2(input))
    else:
        print("Invalid part", file=sys.stderr)
        sys.exit(1)
