from sys import stdin

# Day 06

def star1(buffer):
    return find_start_of_message(buffer, 4)

def star2(buffer):
    return find_start_of_message(buffer, 14)

def find_start_of_message(buffer, n):
    for i in range(len(buffer) - n):
        if len(set(buffer[i:i+n])) == n:
            return i + n
    return -1

### Input etc.

buffer = stdin.read()
print(f"06_1: {star1(buffer)}")
print(f"06_2: {star2(buffer)}")
