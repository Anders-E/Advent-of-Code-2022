from sys import stdin

### Day 01

def star1(inventories):
    sums = [sum(inventory) for inventory in inventories]
    return max(sums)

def star2(inventories):
    sums = sorted([sum(inventory) for inventory in inventories])
    return sum(sums[-1:-4:-1])

### Input etc.

def parse_input(input):
    return [[int(item) for item in inventory.split('\n')] for inventory in input.split("\n\n")]

input = stdin.read()
inventories = parse_input(input)
print(f"01_1: {star1(inventories)}")
print(f"01_2: {star2(inventories)}")
