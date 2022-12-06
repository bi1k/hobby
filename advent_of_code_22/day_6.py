# https://adventofcode.com/2022/day/6
# Part 1: How many characters need to be processed before the first start-of-packet marker is detected?
# Part 2: How many characters need to be processed before the first start-of-message marker is detected?

advent_input_location = ""  # insert location of input file

result_1 = 0
result_2 = 0
incr = 0

with open(advent_input_location, "r") as f:
    stream = f.readline()
for num in range(len(stream)):
    window_4 = {stream[incr], stream[incr + 1], stream[incr + 2], stream[incr + 3]}
    window_14 = {stream[incr], stream[incr + 1], stream[incr + 2], stream[incr + 3],
                 stream[incr + 4], stream[incr + 5], stream[incr + 6], stream[incr + 7],
                 stream[incr + 8], stream[incr + 9], stream[incr + 10], stream[incr + 11],
                 stream[incr + 12], stream[incr + 13]}
    if len(window_4) == 4 and result_1 == 0:
        result_1 = incr + 4
    if len(window_14) == 14:
        result_2 = incr + 14
        break
    else:
        incr += 1

print('Characters that need to be processed before the first start-of-packet marker: {}'.format(result_1))
print('Characters that need to be processed before the first start-of-message marker: {}'.format(result_2))
