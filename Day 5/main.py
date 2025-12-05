with open("Day 5/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    sep = lines.index("")
    ranges_input, foods_input = lines[:sep], lines[sep+1:]

def part_one():
    ranges = []
    for r in ranges_input:
        f, t = map(int, r.split("-"))
        ranges.append(range(f,t+1))
    
    res = 0
    for food in foods_input:
        food = int(food)
        for r in ranges:
            if food in r:
                res += 1
                break
    return res

def merge_ranges(ranges):
    new_ranges = []
    c = 0
    # Check if range to add overlaps with existing ones
    for r_to_add in ranges:
        for r_compare in new_ranges:
            merged_r = range(max(r_to_add[0], r_compare[0]), min(r_to_add[-1], r_compare[-1])+1)
            if len(merged_r) > 0:
                new_ranges.append(merged_r)
                print(merged_r)
                c += 1
            else:
                new_ranges.append(r)

    if not c:
        new_ranges.append(input_r)

    return new_ranges

def part_two():
    ranges = []
    for r in ranges_input:
        f, t = map(int, r.split("-"))
        ranges.append(range(f,t+1))
    
    merge_ranges(ranges)

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))