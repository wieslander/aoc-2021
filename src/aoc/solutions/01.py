"""Advent of Code - 2021 Day 1"""

from collections import deque


def depth_increase_count(depths, window_size):
    count = 0
    prev_window = None

    for window_start in range(0, len(depths) - window_size + 1):
        window_end = window_start + window_size
        window = sum(depths[window_start:window_end])

        if prev_window and window > prev_window:
            count += 1

        prev_window = window

    return count


def part1(input):
    depths = input.lines(int)
    return depth_increase_count(depths, 1)


def part2(input):
    depths = input.lines(int)
    return depth_increase_count(depths, 3)
