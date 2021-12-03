"""Advent of Code - 2021 Day 3"""


def part1(input):
    lines = input.lines(tuple)
    gamma_bits = []
    epsilon_bits = []

    for bits in zip(*lines):
        ones = len([b for b in bits if b == '1'])
        zeroes = len([b for b in bits if b == '0'])

        if ones > zeroes:
            gamma_bits.append('1')
            epsilon_bits.append('0')
        else:
            gamma_bits.append('0')
            epsilon_bits.append('1')

    gamma = bits_to_int(gamma_bits)
    epsilon = bits_to_int(epsilon_bits)

    return gamma * epsilon


def part2(input):
    lines = input.lines(tuple)
    oxygen_generator_rating = get_oxygen_generator_rating(lines)
    co2_scrubber_rating = get_co2_scrubber_rating(lines)
    return oxygen_generator_rating * co2_scrubber_rating


def get_oxygen_generator_rating(lines):
    bits = filter_candidates(lines, most_common=True)
    return bits_to_int(bits)


def get_co2_scrubber_rating(lines):
    bits = filter_candidates(lines, most_common=False)
    return bits_to_int(bits)


def filter_candidates(candidates, most_common):
    pos = 0

    while len(candidates) > 1:
        filter_bit = get_filter_bit(candidates, pos, most_common=most_common)
        candidates = list(filter(lambda line: line[pos] == filter_bit, candidates))
        pos += 1

    return candidates[0]


def get_filter_bit(candidates, pos, most_common):
    bits = [line[pos] for line in candidates]
    ones = len([b for b in bits if b == '1'])
    zeroes = len([b for b in bits if b == '0'])

    if most_common:
        return '1' if ones >= zeroes else '0'
    else:
        return '0' if zeroes <= ones else '1'


def bits_to_int(bits):
    return int(''.join(bits), 2)
