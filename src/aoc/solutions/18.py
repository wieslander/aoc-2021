"""Advent of Code - 2021 Day 18"""

import functools
import itertools
import json
import operator

from aoc.tree import BinaryTree

class Pair(BinaryTree):
    @staticmethod
    def from_json(s):
        return Pair.from_list(json.loads(s))

    @staticmethod
    def from_list(pairs):
        left, right = pairs
        left = Pair.autodetect(left)
        right = Pair.autodetect(right)
        return Pair(left, right)

    @staticmethod
    def autodetect(item):
        if isinstance(item, list):
            return Pair.from_list(item)
        else:
            return Pair.leaf(item)

    @staticmethod
    def leaf(value):
        return Pair(None, None, value)

    def clone(self):
        left = self.left.clone() if self.left else None
        right = self.right.clone() if self.right else None
        return Pair(left, right, self.value)

    def __add__(self, other):
        p = Pair(self.clone(), other.clone())
        p.reduce()
        return p

    def split(self):
        left = self.value // 2
        right = (self.value + 1) // 2
        self.left = Pair.leaf(left)
        self.right = Pair.leaf(right)
        self.value = None

    def reduce(self):
        while self.explode_first() or self.split_first():
            pass

    def explode_first(self):
        prev_leaf = None
        exploded_right = None

        for node, depth in self.traverse_depth_first():
            if exploded_right is not None and node.is_leaf():
                v = node.value
                node.value += exploded_right
                return True

            if depth >= 4 and not node.is_leaf() and exploded_right is None:
                if prev_leaf and node.left:
                    prev_leaf.value += node.left.value
                exploded_right = node.right.value
                node.left = None
                node.right = None
                node.value = 0
            elif node.is_leaf():
                prev_leaf = node

        return False

    def split_first(self):
        for node, _ in self.traverse_depth_first():
            if node.is_leaf() and node.value >= 10:
                node.split()
                return True
        return False

    def magnitude(self):
        if self.value is not None:
            return self.value
        else:
            return self.left.magnitude() * 3 + self.right.magnitude() * 2


def part1(input):
    pairs = input.lines(Pair.from_json)
    final_pair = functools.reduce(operator.add, pairs)
    return final_pair.magnitude()


def part2(input):
    pairs = input.lines(Pair.from_json)
    max_magnitude = 0

    for p1, p2 in itertools.permutations(pairs, 2):
        p = p1 + p2
        max_magnitude = max(max_magnitude, p.magnitude())

    return max_magnitude
