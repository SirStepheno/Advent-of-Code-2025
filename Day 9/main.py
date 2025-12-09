from itertools import combinations

with open("Day 9/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    corners = [tuple(map(int, line.split(","))) for line in lines]

def part_one():
    r = 0
    for combi in combinations(corners, 2):
        p1, p2 = combi
        if (d := abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)) > r:
            r = d
    return r

def part_two():
    pass

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))