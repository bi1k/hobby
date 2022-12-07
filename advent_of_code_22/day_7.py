# https://adventofcode.com/2022/day/7
# Part 1: What is the sum of the total sizes of those directories?
# Part 2: What is the total size of that directory [the smallest that can be deleted]?

advent_input_location = ""  # insert location of input file

cwd = "/"
files = set()
disk_used = 0
dir_length = 0
total_size = 0
directories = {}
smallest_size_del = 0

with open(advent_input_location, "r") as f:
    for line in f:
        # Handle cd
        if line[2:4] == "cd":
            if line[5:7] == "..":
                cwd = cwd[:- dir_length - 1]
            elif line[5:6] != "/":
                cwd += line[5:].replace("\n", "/")
            dir_length = len(cwd.split("/")[-2])
        # Handle directories
        elif line[:3] == "dir" and cwd + line[4:].replace("\n", "/") not in directories.keys():
            directories[cwd + line[4:].replace("\n", "/")] = 0
        # Handle files
        elif line[0].isdigit():
            file = line.split(" ")[0] + " " + cwd + line.split(" ")[1].rstrip("\n")
            if file not in files:
                files.add(file)
                disk_used += int(line.split(" ")[0])
                for directory in directories.keys():
                    if directory in cwd:
                        directories[directory] += int(line.split(" ")[0])
for size in sorted(directories.items(), key=lambda x: x[1], reverse=True):
    if int(size[1]) <= 100000:
        total_size += int(size[1])
    if 70000000 - 30000000 - disk_used + int(size[1]) >= 0:
        smallest_size_del = size[1]
        
print('The sum of the total sizes of directories under 100000: {}'.format(total_size))
print('The size of the smallest directory that will allow enough space if deleted: {}'.format(smallest_size_del))
