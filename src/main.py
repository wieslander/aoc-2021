"""Advent of Code main entry point.

Read day and optional part as positional command-line arguments and
start the actual AoC runner.

"""

import argparse
import sys

import aoc


def help():
    print("Usage: main.py day [part] [input]", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="Run solutions for Advent of Code 2021")
    parser.add_argument('day', type=int, help="Run the solution to this day's puzzle")
    parser.add_argument('part', type=int, default=1, help="The part of the puzzle to solve")
    parser.add_argument('--input-file', help="Use a custom input file")
    parser.add_argument('--visualize', action=argparse.BooleanOptionalAction, default=False,
                        help="Visualize the solution, if a visualization has been implemented")
    args = parser.parse_args()

    aoc.run(day=args.day, part=args.part, input_file=args.input_file, visualize=args.visualize)


if __name__ == '__main__':
    main()
