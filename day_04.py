import re
from sys import stdin

# Day 04

def star1(section_ids):
    return sum([fully_contains(*pair) for pair in section_ids])

def star2(section_ids):
    return sum([overlaps(*pair) for pair in section_ids])

def fully_contains(a, b, c, d):
    return (a <= c and b >= d) or (c <= a and d >= b)

def overlaps(a, b, c, d):
    return b >= c and d >= a

### Input etc.

def parse_line(line):
    pattern = r"(\d+)-(\d+).(\d+)-(\d+)"
    return [int(x) for x in re.match(pattern, line).groups()] # type: ignore

section_ids = [parse_line(line.rstrip()) for line in stdin.readlines()]
print(f"03_1: {star1(section_ids)}")
print(f"03_2: {star2(section_ids)}")
