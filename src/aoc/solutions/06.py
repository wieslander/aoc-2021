"""Advent of Code - 2021 Day 6"""

def solve(input, days):
    timers = {}

    for timer in input.data().split(','):
        t = int(timer)
        timers.setdefault(t, 0)
        timers[t] += 1

    for day in range(days):
        new_timers = {}
        for timer, count in timers.items():
            if timer == 0:
                new_timers[8] = count
                new_timers.setdefault(6, 0)
                new_timers[6] += count
            else:
                t = timer - 1
                new_timers.setdefault(t, 0)
                new_timers[t] += count

        timers = new_timers

    return sum(timers.values())


def part1(input):
    return solve(input, 80)


def part2(input):
    return solve(input, 256)
