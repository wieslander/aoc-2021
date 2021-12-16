"""Advent of Code - 2021 Day 16"""

import sys

SUM = 0
MUL = 1
MIN = 2
MAX = 3
LIT = 4
GT = 5
LT = 6
EQ = 7

example = 'D2FE28'

class Packet:
    def __init__(self, version, type_id, value, operands):
        self.version = version
        self.type_id = type_id
        self._value = value
        self.operands = operands

    def value(self):
        if self.type_id == LIT:
            return self._value

        values = [o.value() for o in self.operands]

        if self.type_id == SUM:
            return sum(values)
        if self.type_id == MUL:
            value = 1
            for v in values:
                value *= v
            return value
        if self.type_id == MIN:
            return min(values)
        if self.type_id == MAX:
            return max(values)
        if self.type_id == GT:
            return int(values[0] > values[1])
        if self.type_id == LT:
            return int(values[0] < values[1])
        if self.type_id == EQ:
            return int(values[0] == values[1])


def read_value(bitstring, pos, length):
    value = int(bitstring[pos:pos+length], 2)
    pos += length
    return value, pos


def parse_packet(bitstring, pos=0):
    version, type_id, pos = parse_header(bitstring, pos)

    if type_id == LIT:
        value, pos = parse_literal_payload(bitstring, pos)
        packet = Packet(version, type_id, value, [])
        return packet, pos
    else:
        operands, pos = parse_operator_payload(bitstring, pos)
        packet = Packet(version, type_id, None, operands)
        return packet, pos


def parse_literal_payload(bitstring, pos):
    bits = []

    while True:
        keep_reading, pos = read_value(bitstring, pos, 1)
        group = bitstring[pos:pos+4]
        bits.extend(group)
        pos += 4
        if not keep_reading:
            break

    binary_value = ''.join(bits)
    value = int(binary_value, 2)
    return value, pos


def parse_operator_payload(bitstring, pos):
    length_type_id, pos = read_value(bitstring, pos, 1)
    operands = []

    if length_type_id == 0:
        bit_count, pos = read_value(bitstring, pos, 15)
        packet_end = pos + bit_count

        while pos < packet_end:
            packet, pos = parse_packet(bitstring, pos)
            operands.append(packet)

        if pos != packet_end:
            raise Error(f"Payload length mismatch.  Expected end pos {packet_end}, found {pos}")
    else:
        operand_count, pos = read_value(bitstring, pos, 11)
        for _ in range(operand_count):
            packet, pos = parse_packet(bitstring, pos)
            operands.append(packet)

    return operands, pos


def parse_header(bitstring, pos):
    version, pos = read_value(bitstring, pos, 3)
    type_id, pos = read_value(bitstring, pos, 3)
    return version, type_id, pos


def input_to_binary(s):
    bits = []
    for ch in s:
        bits.append(f'{int(ch, 16):04b}')
    return ''.join(bits)


def part1(input):
    hexstring = input.data().strip()
    bitstring = input_to_binary(hexstring)
    packet, _ = parse_packet(bitstring)

    versions = []
    packets = [packet]

    while packets:
        p = packets.pop()
        versions.append(p.version)
        packets.extend(p.operands)

    return sum(versions)


def part2(input):
    hexstring = input.data().strip()
    bitstring = input_to_binary(hexstring)
    packet, _ = parse_packet(bitstring)
    return packet.value()
