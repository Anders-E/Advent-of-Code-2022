from sys import stdin

def star1(inventories):
    sums = [sum(inventory) for inventory in inventories]
    return max(sums)

def star2(inventories):
    sums = sorted([sum(inventory) for inventory in inventories])
    return sum(sums[-1:-4:-1])


input = stdin.read()
inventories = [[int(item) for item in inventory.split('\n')] for inventory in input.split("\n\n")]
print(f"01_1: {star1(inventories)}")
print(f"01_2: {star2(inventories)}")
