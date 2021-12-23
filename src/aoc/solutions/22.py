"""Advent of Code - 2021 Day 22"""

from aoc.geometry import Cuboid, parse_range


def parse_axis(axis_spec):
    axis_name, axis_range = axis_spec.split('=')
    return parse_range(axis_range)


def parse_instruction(s):
    state, cuboid_spec = s.split()
    x_spec, y_spec, z_spec = cuboid_spec.split(',')
    min_x, max_x = parse_axis(x_spec)
    min_y, max_y = parse_axis(y_spec)
    min_z, max_z = parse_axis(z_spec)
    return Cuboid(min_x, max_x, min_y, max_y, min_z, max_z), state


def parse_input(input):
    return input.lines(parse_instruction)


def update_active_cuboids(cuboids, update_region, state):
    result = []

    if state == 'on':
        result.extend(cuboids)
        new_regions = [update_region]

        for c in cuboids:
            regions = []
            for r in new_regions:
                regions.extend(r.difference(c))
            new_regions = regions
            if not new_regions:
                break

        result.extend(new_regions)
    else:
        for c in cuboids:
            diff = c.difference(update_region)
            result.extend(diff)

    return result


def part1(input):
    instructions = parse_input(input)
    active_cuboids = []
    initialization_area = Cuboid(-50, 50, -50, 50, -50, 50)

    for cuboid, state in instructions:
        cuboid = cuboid.intersection(initialization_area)
        if cuboid:
            active_cuboids = update_active_cuboids(active_cuboids, cuboid, state)

    return sum(c.size() for c in active_cuboids)


def part2(input):
    instructions = parse_input(input)
    active_cuboids = []

    for cuboid, state in instructions:
        active_cuboids = update_active_cuboids(active_cuboids, cuboid, state)

    return sum(c.size() for c in active_cuboids)
