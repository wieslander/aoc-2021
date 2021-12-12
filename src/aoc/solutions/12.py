"""Advent of Code - 2021 Day 12"""

from collections import Counter

from aoc.graph import Graph


def node_filter_part_1(graph, path, node):
    return node not in path or node == node.upper()


def node_filter_part_2(graph, path, node):
    if node not in path or node == node.upper():
        return True
    elif node == 'start':
        return False
    else:
        node_counts = Counter(path)
        if node_counts[node] > 1:
            return False

        for n, count in node_counts.items():
            if n == n.lower() and count > 1:
                return False

        return True


def part1(input):
    g = Graph()
    for edge in input.lines():
        nodes = edge.split('-')
        g.add_edge(*nodes)

    paths = g.find_all_paths('start', 'end', node_filter_part_1)
    return len(paths)


def part2(input):
    g = Graph()
    for edge in input.lines():
        nodes = edge.split('-')
        g.add_edge(*nodes)

    paths = g.find_all_paths('start', 'end', node_filter_part_2)
    return len(paths)
