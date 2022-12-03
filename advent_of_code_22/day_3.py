# https://adventofcode.com/2022/day/3
# Part 1: What is the sum of the priorities of those item types?
# Part 2: What is the sum of the priorities of those [badge] item types?

advent_input_location = ""  # insert location of input file
# get letters (or items) by appending chr(97)-chr(123) and chr(65)-chr(91) to "item_types" using For loops
item_types = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sack_count = 0
priority_sum = 0
group_priority_sum = 0
group_sacks = {1: "", 2: "", 3: ""}

with open(advent_input_location, "r") as f:
    for rucksack in f:
        sack_count = sack_count % 3 + 1
        group_sacks[sack_count] = rucksack.rstrip("\n")
        # intersect the 1st compartment of the sack with the 2nd compartment to get the mishandled item type
        priority = list(set(rucksack[:int(len(rucksack)//2)]).intersection(rucksack[int(len(rucksack)//2):]))[0]
        priority_sum += item_types.index(priority) + 1
        if sack_count == 3:
            # intersect each elf group's rucksacks to get each group's badge item type
            group_priority = list(set(group_sacks[1]).intersection(group_sacks[2]).intersection(group_sacks[3]))[0]
            group_priority_sum += item_types.index(group_priority) + 1

print('Total priority of the mishandled item types: {}'.format(priority_sum))
print('Total priority of the badge item types: {}'.format(group_priority_sum))
