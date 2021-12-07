"""Advent of Code - 2021 Day 7"""

from collections import Counter, defaultdict


def part1(input):
    positions = input.csv_line()
    min_pos = min(positions)
    max_pos = max(positions)

    fuel_requirements = defaultdict(int)
    pos_counts = Counter(positions)

    for target_pos in range(min_pos, max_pos + 1):
        for crab_pos, crab_count in pos_counts.items():
            distance = abs(crab_pos - target_pos)
            fuel_requirements[target_pos] += distance * crab_count

    return min(fuel_requirements.values())


def part2(input):
    positions = input.csv_line()
    min_pos = min(positions)
    max_pos = max(positions)

    fuel_requirements = defaultdict(int)
    pos_counts = Counter(positions)

    for target_pos in range(min_pos, max_pos + 1):
        for crab_pos, crab_count in pos_counts.items():
            distance = abs(crab_pos - target_pos)
            fuel_required = int((distance + 1) * (distance / 2))
            fuel_requirements[target_pos] += fuel_required * crab_count

    return min(fuel_requirements.values())
