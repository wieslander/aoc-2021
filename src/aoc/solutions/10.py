"""Advent of Code - 2021 Day 10"""

brace_map = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

syntax_error_score_map = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

autocomplete_score_map = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

def is_opening_brace(ch):
    return ch in brace_map


def is_closing_brace(ch):
    return ch in brace_map.values()


def syntax_error_score(line):
    stack = []
    for ch in line:
        if is_opening_brace(ch):
            stack.append(ch)
        elif is_closing_brace(ch):
            last_opening_brace = stack.pop()
            if ch != brace_map[last_opening_brace]:
                return syntax_error_score_map[ch]

    return 0


def completion_score(line):
    total_score = 0
    for ch in get_autocompletion(line):
        total_score *= 5
        total_score += autocomplete_score_map[ch]
    return total_score


def get_autocompletion(line):
    stack = []
    for ch in line:
        if is_opening_brace(ch):
            stack.append(ch)
        elif is_closing_brace(ch):
            stack.pop()

    return reversed([brace_map[ch] for ch in stack])


def part1(input):
    return sum(syntax_error_score(line) for line in input.lines())


def part2(input):
    incomplete_lines = [l for l in input.lines() if syntax_error_score(l) == 0]
    scores = sorted(completion_score(l) for l in incomplete_lines)
    return scores[len(scores) // 2]
