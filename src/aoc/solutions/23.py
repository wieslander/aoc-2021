"""Advent of Code - 2021 Day 23"""

from aoc.geometry import Grid, Point
from aoc.search import a_star


empty_grid = [
    '#############',
    '#...........#',
    '###.#.#.#.###',
    '  #.#.#.#.#  ',
    '  #########  ']

goal_positions = {
    'A': (Point(3, 2), Point(3, 3), Point(3, 4), Point(3, 5)),
    'B': (Point(5, 2), Point(5, 3), Point(5, 4), Point(5, 5)),
    'C': (Point(7, 2), Point(7, 3), Point(7, 4), Point(7, 5)),
    'D': (Point(9, 2), Point(9, 3), Point(9, 4), Point(9, 5)),
}

step_costs = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}


def print_grid(amphipods, cost):
    grid = Grid.from_rows(empty_grid)
    for kind, pos, has_moved in amphipods:
        if has_moved:
            grid[pos] = kind
        else:
            grid[pos] = kind.lower()
    print(f"Cost: {cost}")
    print(grid)
    print()


def print_path(path):
    for amphipods, cost in path:
        print_grid(amphipods, cost)



def is_in_hallway(pos):
    return pos.y == 1


def get_valid_destinations(kind, pos, has_moved, grid):
    room = [p for p in goal_positions[kind] if p in grid and grid[p] != '#']

    if is_in_hallway(pos):
        if any(grid[p] not in ('.', kind) for p in room):
            return

        empty_cells = [p for p in room if grid[p] == '.']
        target = empty_cells[-1]

        valid = False
        if target.x > pos.x:
            valid = all(grid[Point(x, 1)] == '.'
                        for x in range(pos.x + 1, target.x + 1))
        elif target.x < pos.x:
            valid = all(grid[Point(x, 1)] == '.'
                        for x in range(target.x, pos.x))
        if valid:
            yield target
    elif not has_moved:
        above = pos - Point(0, 1)

        if grid[above] != '.':
            return

        for x in range(pos.x, 12):
            target = Point(x, 1)
            if grid[target] != '.':
                break
            elif x in (3, 5, 7, 9):
                continue
            yield target

        for x in range(pos.x, 0, -1):
            target = Point(x, 1)
            if grid[target] != '.':
                break
            elif x in (3, 5, 7, 9):
                continue
            yield target


def next_states(amphipods):
    grid = Grid.from_rows(empty_grid)
    for kind, pos, has_moved in amphipods:
        grid[pos] = kind

    for index, (kind, pos, has_moved) in enumerate(amphipods):
        for dest_pos in get_valid_destinations(kind, pos, has_moved, grid):
            next_state = list(amphipods)
            next_state[index] = (kind, dest_pos, True)
            next_state = tuple(sorted(next_state))
            distance = pos.manhattan_distance(dest_pos)
            yield next_state, distance * step_costs[kind]


def is_goal(amphipods):
    return all(pos in goal_positions[kind] for kind, pos, _ in amphipods)


def h(amphipods):
    return sum(
        min(pos.manhattan_distance(goal_pos) * step_costs[kind]
            for goal_pos in goal_positions[kind])
        for kind, pos, _ in amphipods)


def solve(grid):
    path, total_cost = a_star(grid, next_states, is_goal, h)
    print_path(path)
    return total_cost


def find_amphipods(grid):
    amphipods = []
    for pos, value in grid.items():
        if value in 'ABCD':
            amphipods.append((value, pos, False))
    return tuple(sorted(amphipods))


def part1(input):
    grid = Grid.from_rows(input.lines())
    amphipods = find_amphipods(grid)
    return solve(amphipods)


def part2(input):
    extra_lines = [
      '  #D#C#B#A#',
      '  #D#B#A#C#'
    ]
    extra_empty_lines = [
      '  #.#.#.#.#  ',
      '  #.#.#.#.#  '
    ]
    lines = input.lines()
    lines[3:3] = extra_lines
    empty_grid[3:3] = extra_empty_lines
    grid = Grid.from_rows(lines)
    amphipods = find_amphipods(grid)
    return solve(amphipods)
