from collections import defaultdict
from heapq import heappop, heappush
from math import inf


def backtrack(came_from, current, total_cost):
    path = [(current, total_cost)]
    while current in came_from:
        current, cost = came_from[current]
        path.append((current, cost))
    path.reverse()
    return path


def a_star(start, next_states, is_goal, h):
    f_costs = defaultdict(lambda: inf)
    g_costs = defaultdict(lambda: inf)
    f_costs[start] = h(start)
    g_costs[start] = 0
    open_set = [(g_costs[start], start)]
    came_from = {}

    while open_set:
        cost, current = heappop(open_set)
        if is_goal(current):
            total_cost = g_costs[current]
            path = backtrack(came_from, current, total_cost)
            return path, total_cost

        possible_moves = 0
        considered_moves = 0
        for neighbor, edge_cost in next_states(current):
            possible_moves += 1
            tentative_cost = g_costs[current] + edge_cost
            if tentative_cost < g_costs[neighbor]:
                considered_moves += 1
                g_costs[neighbor] = tentative_cost
                f_costs[neighbor] = tentative_cost + h(neighbor)
                came_from[neighbor] = (current, g_costs[current])
                heappush(open_set, (f_costs[neighbor], neighbor))
