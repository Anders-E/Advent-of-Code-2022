from sys import stdin
from enum import IntEnum

### Day 2

class Hand(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @staticmethod
    def hand_from_char(c):
        return {
            "A": Hand.ROCK, "X": Hand.ROCK,
            "B": Hand.PAPER, "Y": Hand.PAPER,
            "C": Hand.SCISSORS, "Z": Hand.SCISSORS
        }[c]

result_scores = { -1 : 6, 2 : 6, 0 : 3, 1: 0}
hand_values = { "A": Hand.ROCK, "B": Hand.PAPER, "C": Hand.SCISSORS, "X": Hand.ROCK, "Y": Hand.PAPER, "Z": Hand.SCISSORS}

def star1(games):
    return sum(map(score, games))

def star2(games):
    return sum(map(score2, games))

def score(hands):
    opponent, me = hands
    result = (opponent - me) % 3
    return result_scores[result] + me + 1

def score2(hands):
    opponent, expected_result = hands
    me = {
        Hand.ROCK:     (opponent - 1) % 3,
        Hand.PAPER:    opponent,
        Hand.SCISSORS: (opponent + 1) % 3,
    }[expected_result]
    return score((opponent, me))

### Input etc.
def parse_input(lines):
    return [[int(item) for item in inventory.split('\n')] for inventory in lines.split("\n\n")]

lines = stdin.readlines()
lines = map(str.rstrip, lines)
games = [[Hand.hand_from_char(c) for c in line.split(" ")] for line in lines]
print(f"02_1: {star1(games)}")
print(f"02_2: {star2(games)}")
