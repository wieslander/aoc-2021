"""Advent of Code - 2021 Day 21"""

from collections import Counter
from functools import cache
from itertools import cycle, product


class Player:
    def __init__(self, position, score=0):
        self.position = position
        self.score = score

    def clone(self):
        return Player(self.position, self.score)

    def tuple(self):
        return (self.position, self.score)

    def move(self, steps):
        self.position += steps
        self.position = (self.position - 1) % 10 + 1
        self.score += self.position

    def __hash__(self):
        return hash(self.tuple())

    def __eq__(self, other):
        return self.tuple() == other.tuple()


def parse_player(line):
    _, position = line.split(':')
    return Player(int(position))


def parse_input(input):
    return tuple(input.lines(parse_player))


def part1(input):
    players = parse_input(input)
    die = cycle(range(1, 101))
    player_iter = cycle(players)
    roll_count = 0

    while max(p.score for p in players) < 1000:
        player = next(player_iter)
        steps = next(die) + next(die) + next(die)
        roll_count += 3
        player.move(steps)

    min_score = min(p.score for p in players)
    return min_score * roll_count


dice_outcomes = list(product((1,2,3), repeat=3))
outcome_counts = Counter(sum(rolls) for rolls in dice_outcomes)


@cache
def calculate_wins(players, current_player, universes):
    wins = [0, 0]

    for steps, outcomes in outcome_counts.items():
        player = players[current_player].clone()
        player.move(steps)
        total_outcomes = universes * outcomes

        if player.score >= 21:
            wins[current_player] += total_outcomes
        else:
            new_players = list(players)
            new_players[current_player] = player
            next_player = (current_player + 1) % 2
            p1, p2 = calculate_wins(tuple(new_players), next_player, total_outcomes)
            wins[0] += p1
            wins[1] += p2

    return tuple(wins)


def part2(input):
    players = parse_input(input)
    return max(calculate_wins(players, 0, 1))
