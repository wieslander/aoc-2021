"""Advent of Code main entry point.

Read day and optional part as positional command-line arguments and
start the actual AoC runner.

"""

import sys

import aoc


def help():
    print("Usage: run.py day [part]", file=sys.stderr)


def main():
    if len(sys.argv) < 2:
        help()
        sys.exit(1)

    day = int(sys.argv[1])
    part = 1

    if len(sys.argv) > 2:
        part = int(sys.argv[2])

    aoc.run(day=day, part=part)


if __name__ == '__main__':
    main()
