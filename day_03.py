from functools import reduce
import string
from sys import stdin

from util import grouper

### Day 03

item_values = {
    c: i for i, c in enumerate(string.ascii_letters, 1)
}

def star1(rucksacks):
    common_items = [
        set(a) & set(b) for a, b in map(split_string_in_half, rucksacks)
    ]
    return sum(map(lambda x: item_values[''.join(x)], common_items))

def star2(rucksacks):
    common_items = [reduce(lambda a, b: set(a) & set(b), group) for group in grouper(rucksacks, 3)]
    return sum(map(lambda x: item_values[''.join(x)], common_items))

def split_string_in_half(s):
    halfway = len(s) // 2
    return (s[:halfway], s[halfway:])

### Input etc.

rucksacks = [line.rstrip() for line in stdin.readlines()]
print(f"03_1: {star1(rucksacks)}")
print(f"03_2: {star2(rucksacks)}")
