"""Advent of Code main entry point.

Read day and optional part as positional command-line arguments and
start the actual AoC runner.

"""

import sys

import aoc


def help():
    print("Usage: run.py day [part] [input]", file=sys.stderr)


def main():
    if len(sys.argv) < 2:
        help()
        sys.exit(1)

    day = int(sys.argv[1])
    part = 1

    if len(sys.argv) > 2:
        part = int(sys.argv[2])

    if len(sys.argv) > 3:
        input_file = sys.argv[3]
    else:
        input_file = None

    aoc.run(day=day, part=part, input_file=input_file)


if __name__ == '__main__':
    main()
