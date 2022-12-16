from collections import defaultdict, namedtuple
from copy import deepcopy
import re
from sys import stdin

# Day 05

Move = namedtuple('Move', ["n", "source", "destination"])

def star1(crates, moves):
    crates = deepcopy(crates)
    for n, source, destination in moves:
        move(crates, n, source, destination)
    return ''.join([str(crate[-1]) for crate in crates.values()])

def star2(crates, moves):
    crates = deepcopy(crates)
    for n, source, destination in moves:
        pancake_move(crates, n, source, destination)
    return ''.join([str(crate[-1]) for crate in crates.values()])

def move(crates, n, source, destination):
    crates_to_move = crates[source][-n:]
    crates[source] = crates[source][:-n]
    crates[destination].extend(reversed(crates_to_move))

def pancake_move(crates, n, source, destination):
    crates_to_move = crates[source][-n:]
    crates[source] = crates[source][:-n]
    crates[destination].extend(crates_to_move)

### Input etc.

def parse_input(input):
    input = input[::-1]
    crates = read_crates(input)
    input.pop()
    moves = [read_move_line(line) for line in input[::-1]]
    return crates, moves

def read_crates(reversed_input):
    crate_lines = []
    while reversed_input[-1] !=  "":
        line = reversed_input.pop()
        crate_lines.append(parse_crate_line(line))

    crates = defaultdict(list)
    for crate_line in reversed(crate_lines):
        for i, crate in enumerate(crate_line, 1):
            if crate != " " and not crate.isnumeric():
                crates[i].append(crate)
    return crates

def read_move_line(line):
    pattern = r"move (\d+) from (\d) to (\d)"
    match = [int(match) for match in re.match(pattern, line).groups()] # type: ignore
    return Move(*match)

    
def parse_crate_line(line):
    return [c for c in list(line[1::4])]

lines = [line.rstrip() for line in stdin.readlines()]
crates, moves = parse_input(lines)
print(f"05_1: {star1(crates, moves)}")
print(f"05_2: {star2(crates, moves)}")
