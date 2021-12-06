"""Advent of Code - 2021 Day 6"""

from collections import deque

def solve(input, days):
    timers = deque([0] * 9)

    for timer in input.data().split(','):
        pos = int(timer)
        timers[pos] += 1

    for day in range(days):
        reproducing = timers.popleft()
        timers[6] += reproducing
        timers.append(reproducing)

    return sum(timers)


def part1(input):
    return solve(input, 80)


def part2(input):
    return solve(input, 256)
