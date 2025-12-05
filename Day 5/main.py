def merge_ranges(ranges):
    new_ranges = []
    # Add every range to new_range again
    for r_to_add in ranges:
        merged = False
        # Compare new_range to every range already inside, if no overlap, add it to the end, if merge and redo
        for r_i, r_compare in enumerate(new_ranges):
            merged_r = range(max(r_to_add[0], r_compare[0]), min(r_to_add[-1], r_compare[-1])+1)
            if len(merged_r) > 0:
                new_ranges[r_i] = range(min(r_to_add[0], r_compare[0]), max(r_to_add[-1], r_compare[-1])+1)
                new_ranges = merge_ranges(new_ranges)
                merged = True
                break

        if not merged:
            new_ranges.append(r_to_add)
    
    return new_ranges

with open("Day 5/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    sep = lines.index("")
    ranges_input, foods_input = lines[:sep], lines[sep+1:]

    ranges = []
    for r in ranges_input:
        f, t = map(int, r.split("-"))
        ranges.append(range(f,t+1))

    merged_ranges = merge_ranges(ranges)

    foods_input = [int(food) for food in foods_input]

def part_one():
    res = 0
    for food in foods_input:
        for r in merged_ranges:
            if food in r:
                res += 1
                break
    return res

def part_two():
    return sum([len(r) for r in merged_ranges])

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))