# https://adventofcode.com/2022/day/4
# Part 1: In how many assignment pairs does one range fully contain the other?
# Part 2: In how many assignment pairs do the ranges overlap?

advent_input_location = ""  # insert location of input file

full_overlaps = 0
part_overlaps = 0

with open(advent_input_location, "r") as f:
    for pair in f:
        assignments = pair.rstrip("\n").split(",")
        assignment_1 = set([])
        assignment_2 = set([])
        for x in range(int(assignments[0].split("-")[0]), int(assignments[0].split("-")[1]) + 1):
            assignment_1.add(x)
        for y in range(int(assignments[1].split("-")[0]), int(assignments[1].split("-")[1]) + 1):
            assignment_2.add(y)
        if len(assignment_2) > len(assignment_1):
            temp_assignment = assignment_1
            assignment_1 = assignment_2
            assignment_2 = temp_assignment
        total_before = len(assignment_2)
        for num in assignment_1:
            assignment_2.discard(num)
        if len(assignment_2) == 0:
            full_overlaps += 1
        if len(assignment_2) < total_before:
            part_overlaps += 1

print('Number of fully overlapped assignments: {}'.format(full_overlaps))
print('Number of partially overlapped assignments: {}'.format(part_overlaps))
