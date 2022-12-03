# https://adventofcode.com/2022/day/2
# Raw input file: https://raw.githubusercontent.com/nick426/hobby/master/advent%20of%20code%202022/input_day_2
# Part 1: What would your total score be if everything goes exactly according to your strategy guide?
# Part 2: Following the Elf's instructions for the second column, what would your total score be if everything goes
# exactly according to your strategy guide?

advent_input_location = ""  # insert location of input file
total_score_1 = 0
total_score_2 = 0

# rock, paper, scissors values
rps = {"X": 1, "Y": 2, "Z": 3}
# lose, draw or win result of the round (ABC = opponent, XYZ = you)
ldw1 = {"A": {"X": 3, "Y": 6, "Z": 0},
        "B": {"X": 0, "Y": 3, "Z": 6},
        "C": {"X": 6, "Y": 0, "Z": 3}}
# value of the move to make to lose, draw or win + result of the round
ldw2 = {"X": {"A": rps["Z"], "B": rps["X"], "C": rps["Y"], "Result": 0},
        "Y": {"A": rps["X"], "B": rps["Y"], "C": rps["Z"], "Result": 3},
        "Z": {"A": rps["Y"], "B": rps["Z"], "C": rps["X"], "Result": 6}}

with open(advent_input_location, "r") as f:
    for xround in f:
        # value of the move + result of the round
        total_score_1 += rps[xround[2]] + ldw1[xround[0]][xround[2]]
        total_score_2 += ldw2[xround[2]][xround[0]] + ldw2[xround[2]]["Result"]

print('Part 1 strategy guide total score: {}'.format(total_score_1))
print('Part 2 strategy guide total score: {}'.format(total_score_2))
