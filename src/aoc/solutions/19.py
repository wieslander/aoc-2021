"""Advent of Code - 2021 Day 19"""

from itertools import combinations

from aoc.geometry import Point


def parse_input(input):
    scanners = []
    scanner_id = None
    beacons = []

    for line in input.lines():
        if not line:
            continue
        if 'scanner' in line:
            if beacons:
                scanners.append(beacons)
                beacons = []
        else:
            beacons.append(Point.from_csv(line))

    if beacons:
        scanners.append(beacons)

    return [(index, list(find_all_orientations(beacons)))
            for index, beacons in enumerate(scanners)]


def find_all_orientations(points):
    for axis in ('x', 'y', 'z'):
        for reverse in [False, True]:
            orientation = [p.rotate_up(axis, reverse) for p in points]
            for _ in range(4):
                orientation = set(p.rotate_around('y') for p in orientation)
                yield orientation


def find_overlapping_beacons(beacons, other_beacons):
    beacons = set(beacons)
    for origin in beacons:
        for offset_beacon in other_beacons:
            offset = offset_beacon - origin
            moved_beacons = [b - offset for b in other_beacons]
            matching_beacons = [b for b in moved_beacons if b in beacons]
            if len(matching_beacons) >= 12:
                return matching_beacons, offset

    return None, None


def is_overlapping(orientations, other):
    reference = orientations[0]

    for beacons in other:
        overlap = find_overlapping_beacons(reference, beacons)
        if overlap:
            return True

    return False


def find_starting_scanner(scanners):
    for s0, s1 in combinations(scanners, 2):
        scanner_id, orientations = s0
        _, other_orientations = s1
        if is_overlapping(orientations, other_orientations):
            return (scanner_id, Point(0, 0, 0), orientations)


def realign(reference, orientations):
    for index, orientation in enumerate(orientations):
        _, offset = find_overlapping_beacons(reference, orientation)
        if offset:
            orientations.pop(index)
            orientations.insert(0, set(beacon - offset for beacon in orientation))
            return offset


def find_all_beacons(input):
    beacons = set()
    scanners = set()
    processed_scanners = set()

    all_orientations = parse_input(input)
    starting_scanner = find_starting_scanner(all_orientations)
    open_set = [starting_scanner]

    while open_set:
        scanner_id, scanner_pos, orientations = open_set.pop()
        reference_orientation = orientations[0]
        beacons.update(reference_orientation)
        scanners.add(scanner_pos)

        for other_id, other_orientations in all_orientations:
            if other_id != scanner_id and other_id not in processed_scanners:
                offset = realign(reference_orientation, other_orientations)
                if offset:
                    open_set.append((other_id, -offset, other_orientations))

        processed_scanners.add(scanner_id)

    return beacons, scanners


def part1(input):
    beacons, _ = find_all_beacons(input)
    return len(beacons)


def part2(input):
    _, scanners = find_all_beacons(input)
    return max(s1.manhattan_distance(s2) for s1, s2 in combinations(scanners, 2))
