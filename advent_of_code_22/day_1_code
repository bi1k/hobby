# https://adventofcode.com/2022/day/1
# Raw input file: https://raw.githubusercontent.com/nick426/hobby/master/advent%20of%20code%202022/input_day_1
# Part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
# Part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

advent_input_location = ""  # insert location of raw input file
elves = []
calories = 0

with open(advent_input_location, "r") as f:
    advent_input = f.readlines()

for line in advent_input:
    if line.rstrip("\n").isdigit():
        calories += int(line.rstrip("\n"))
    else:
        elves.append(calories)
        calories = 0

elves.sort(reverse=True)
print('Top elf\'s calories: {}'.format(elves[0]))
print('Top three elves\'s calories (total): {}'.format(sum(elves[:3])))
