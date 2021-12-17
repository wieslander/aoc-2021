"""Advent of Code - 2021 Day 17"""

from aoc.geometry import Point, Rectangle


def parse_input(input):
    _, target_coords = input.data().split(': ')
    x_range, y_range = target_coords.split(', ')
    min_x, max_x = parse_range(x_range)
    min_y, max_y = parse_range(y_range)
    topleft = Point(min_x, max_y)
    bottomright = Point(max_x, min_y)
    return Rectangle(topleft, bottomright)


def parse_range(range_spec):
    _, r = range_spec.split('=')
    coords = [int(number) for number in r.split('..')]
    return min(coords), max(coords)


def will_hit(vel, target):
    pos = Point(0, 0)

    while True:
        if target.includes(pos):
            return True
        elif pos.x > target.bottomright.x or pos.y < target.bottomright.y:
            return False

        pos += vel
        vel.y -= 1
        if vel.x != 0:
            vel.x -= abs(vel.x) // vel.x

def part1(input):
    target = parse_input(input)
    initial_velocity = -target.bottomright.y - 1
    return (initial_velocity * (initial_velocity + 1)) // 2


def part2(input):
    target = parse_input(input)
    min_y_velocity = target.bottomright.y
    max_y_velocity = -target.bottomright.y - 1
    max_x_velocity = target.bottomright.x

    hits = 0
    for x_vel in range(max_x_velocity + 1):
        for y_vel in range(min_y_velocity, max_y_velocity + 1):
            vel = Point(x_vel, y_vel)
            if will_hit(vel, target):
                hits += 1

    return hits
