# https://adventofcode.com/2022/day/8
# Part 1: How many trees are visible from outside the grid?
# Part 2: What is the highest scenic score possible for any tree?

advent_input_location = ""  # insert location of input file
tree_stream = ""
best_scenic_score = 1
visible_trees = 0
line_count = 0

with open(advent_input_location, "r") as f:
    for tree_line in f:
        line_length = len(tree_line.rstrip("\n"))
        tree_stream += tree_line.rstrip("\n")
stream_length = len(tree_stream)
for num in range(len(tree_stream)):
    # if a tree is on the outer edge, mark as visible and don't include in scenic scoring
    if num % line_length == 0 or (num + 1) % line_length == 0 or num in range(line_length) or \
            num in range(stream_length, stream_length - line_length, - 1):
        visible_trees += 1
    else:
        # get a list of trees in each direction from the tree being observed
        left = (list(tree_stream[(line_length * line_count): num]))[::-1]
        right = (list(tree_stream[num + 1: (line_length * line_count) + line_length]))
        up = (list(tree_stream[num % line_length: num - 1: line_length]))[::-1]
        down = (list(tree_stream[num + line_length: stream_length: line_length]))
        # get the highest tree in each direction (to later determine whether its visible)
        l_max = max(left)
        r_max = max(right)
        u_max = max(up)
        d_max = max(down)
        scenic_score = 1
        for direction in [left, right, up, down]:
            distance = 0
            for tree in direction:
                distance += 1
                # if tree is obstructing the view, discontinue iterating through the other trees
                if tree_stream[num] <= tree:
                    break
            scenic_score *= distance
        # scenic score will be left distance x right distance x up distance x down distance
        if scenic_score > best_scenic_score:
            best_scenic_score = scenic_score
        # see if tree is visible in any direction from itself
        if tree_stream[num] > l_max or tree_stream[num] > r_max or tree_stream[num] > u_max or tree_stream[num] > d_max:
            visible_trees += 1
    # line_count = to reference a row of trees (or a tree line). line_count 0 is the first row of trees
    if num > 0 and num % line_length == 0:
        line_count += 1

print('The number of visible trees from outside of the grid is: {}'.format(visible_trees))
print('The best scenic score in the grid of trees is: {}'.format(best_scenic_score))
