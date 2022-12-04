# https://adventofcode.com/2022/day/4
# Part 1: In how many assignment pairs does one range fully contain the other?
# Part 2: In how many assignment pairs do the ranges overlap?

advent_input_location = ""  # insert location of input file

full_overlaps = 0
part_overlaps = 0

with open(advent_input_location, "r") as f:
    for pair in f:
        assignments = pair.rstrip("\n").split(",")
        assignment_1 = {*range(int(assignments[0].split("-")[0]), int(assignments[0].split("-")[1]) + 1)}
        assignment_2 = {*range(int(assignments[1].split("-")[0]), int(assignments[1].split("-")[1]) + 1)}
        if len(assignment_1.intersection(assignment_2)) == len(assignment_1) \
                or len(assignment_2.intersection(assignment_1)) == len(assignment_2):
            full_overlaps += 1
            part_overlaps += 1
        elif len(assignment_1.intersection(assignment_2)) > 0:
            part_overlaps += 1

print('Number of fully overlapped assignments: {}'.format(full_overlaps))
print('Number of partially overlapped assignments: {}'.format(part_overlaps))
