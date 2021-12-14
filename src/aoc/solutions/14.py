"""Advent of Code - 2021 Day 14"""

from collections import Counter
import itertools


def parse_input(input):
    lines = list(input.lines())
    polymer = list(lines[0])
    pairs = Counter(itertools.pairwise(polymer))
    rules = parse_rules(lines[2:])
    return polymer, pairs, rules


def parse_rules(lines):
    rules = {}
    for line in lines:
        substring, insertion_element = line.split(' -> ')
        pair = tuple(substring)
        rules[pair] = insertion_element
    return rules


def apply_rules(pairs, rules):
    for pair, count in list(pairs.items()):
        insertion_char = rules.get(pair)
        a, b = pair
        pairs[(a, insertion_char)] += count
        pairs[(insertion_char, b)] += count
        pairs[pair] -= count


def solve(input, steps):
    polymer, pairs, rules = parse_input(input)

    for _ in range(steps):
        apply_rules(pairs, rules)

    c = Counter()
    for (a, b), count in pairs.items():
        c[a] += count
        c[b] += count

    c[polymer[0]] += 1
    c[polymer[-1]] += 1

    counts = c.most_common()
    _, most_common = counts[0]
    _, least_common = counts[-1]

    return most_common // 2 - least_common // 2


def part1(input):
    return solve(input, 10)


def part2(input):
    return solve(input, 40)
