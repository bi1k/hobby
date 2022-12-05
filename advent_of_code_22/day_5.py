# https://adventofcode.com/2022/day/5
# Part 1: After the rearrangement procedure [9000] completes, what crate ends up on top of each stack?
# Part 2: After the rearrangement procedure [9001] completes, what crate ends up on top of each stack?

advent_input_location = ""  # insert location of input file

# the tops of the stacks (lists) are to right (index -1)
stacks_9000 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
stacks_9001 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
top_crates_9000 = ""
top_crates_9001 = ""

with open(advent_input_location, "r") as f:
    for line in f:
        # for all move instructions from the input file:
        if "move" in line:
            # instruction[0] = number of moves. instruction[1] = stack taken from. instruction[2] = stack placed on.
            instruction = line.lstrip("move ").replace("from ", "").replace(" to", "").rstrip("\n").split(" ")
            # 9001: add group of crates to next stack
            stacks_9001[int(instruction[2])]\
                .extend(stacks_9001[int(instruction[1])][len(stacks_9001[int(instruction[1])])-int(instruction[0]):])
            # for each "move":
            # 9000: add a crate to the next stack while removing a crate from the previous stack
            # 9001: (continued from line 19), remove the crates from the previous stack
            for move in range(int(instruction[0])):
                stacks_9000[int(instruction[2])].append(stacks_9000[int(instruction[1])].pop())
                stacks_9001[int(instruction[1])].pop()
        # for all starting crate configurations from the input file:
        elif "[" in line:
            crate_stack = 1
            for position in range(1, len(line), 4):
                if line[position] != " " and line[position] != "\n":
                    stacks_9000[crate_stack].insert(0, line[position])
                    stacks_9001[crate_stack].insert(0, line[position])
                crate_stack += 1
for key in stacks_9000.keys():
    top_crates_9000 += stacks_9000[key][-1]
    top_crates_9001 += stacks_9001[key][-1]
    
print('The top crates of each stack using the CrateMover 9000 are: {}'.format(top_crates_9000))
print('The top crates of each stack using the CrateMover 9001 are: {}'.format(top_crates_9001))
