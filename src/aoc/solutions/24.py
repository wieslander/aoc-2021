"""Advent of Code - 2021 Day 24"""

from functools import cache


def parse_instruction(line):
    instruction, *operands = line.split()
    try:
        operands[-1] = int(operands[-1])
    except ValueError:
        pass
    return (instruction, tuple(operands))


def parse_program(input):
    instructions = input.lines(parse_instruction)
    section = []
    sections = []

    for instruction, operands in instructions:
        if instruction == 'inp':
            section = [(instruction, operands)]
            sections.append(section)
        else:
            section.append((instruction, operands))

    return tuple(tuple(s) for s in sections)


@cache
def run(program_section, digit, **kwargs):
    inputs = [digit]
    registers = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    registers.update(kwargs)

    def val(operand):
        return registers.get(operand, operand)

    for instruction, operands in program_section:
        match instruction:
            case 'inp':
                target = operands[0]
                registers[target] = inputs.pop()
            case 'add':
                a, b = operands
                registers[a] += val(b)
            case 'mul':
                a, b = operands
                registers[a] *= val(b)
            case 'div':
                a, b = operands
                registers[a] = int(registers[a] / val(b))
            case 'mod':
                a, b = operands
                registers[a] %= val(b)
            case 'eql':
                a, b = operands
                registers[a] = int(registers[a] == val(b))

    return registers['z']


def find_model_number(sections, largest=False):
    @cache
    def find_suffix(length, z):
        if length == 0:
            if z == 0:
                return tuple()
            else:
                return None
        else:
            section = sections[-length]
            next_digits = range(9, 0, -1) if largest else range(1, 10)
            for d in next_digits:
                next_z = run(section, d, z=z)
                suffix = find_suffix(length - 1, next_z)
                if suffix is not None:
                    return (d, *suffix)

    result = find_suffix(14, 0)
    return int(''.join(str(d) for d in result))


def part1(input):
    sections = parse_program(input)
    return find_model_number(sections, largest=True)


def part2(input):
    sections = parse_program(input)
    return find_model_number(sections, largest=False)
