"""Advent of Code - 2021 Day 8"""

import sys


def part1(input):
    count = 0

    for line in input.lines():
        _, outputs = line.split(" | ")

        for output in outputs.split():
            length = len(output)
            if length in (2, 3, 4, 7):
                count += 1

    return count


def part2(input):
    total = 0

    for line in input.lines():
        patterns, outputs = line.split(" | ")
        patterns = [tuple(sorted(pattern)) for pattern in patterns.split()]
        outputs = [tuple(sorted(output)) for output in outputs.split()]
        pattern_map = {}
        digit_map = {}

        # Do the trivial cases first
        for p in patterns:
            length = len(p)
            if length == 2:
                pattern_map[p] = 1
                digit_map[1] = p
            elif length == 3:
                pattern_map[p] = 7
                digit_map[7] = p
            elif length == 4:
                pattern_map[p] = 4
                digit_map[4] = p
            elif length == 7:
                pattern_map[p] = 8
                digit_map[8] = p

        # Non-trivial cases
        for p in patterns:
            length = len(p)
            if length == 5:
                # 2, 3 or 5
                if all(segment in p for segment in digit_map[1]):
                    pattern_map[p] = 3
                    digit_map[3] = p
                else:
                    overlap_with_four = [s for s in p if s in digit_map[4]]
                    if len(overlap_with_four) == 2:
                        pattern_map[p] = 2
                        digit_map[2] = p
                    else:
                        pattern_map[p] = 5
                        digit_map[5] = p
            if length == 6:
                # 0, 6 or 9
                missing = [c for c in 'abcdefg' if c not in p][0]
                if missing not in digit_map[4]:
                    pattern_map[p] = 9
                    digit_map[9] = p
                elif missing not in digit_map[1]:
                    pattern_map[p] = 0
                    digit_map[0] = p
                else:
                    pattern_map[p] = 6
                    digit_map[6] = p

        output_chars = [str(pattern_map[output]) for output in outputs]
        output = int(''.join(output_chars))
        total += output

    return total
