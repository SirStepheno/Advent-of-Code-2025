with open("Day 2/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()][0]
    combinations = lines.split(",")
    combinations = [(int(a),int(b)) for a,b in [combination.split("-") for combination in combinations]]

def part_one():
    r = 0
    for combination in combinations:
        for i in range(combination[0], combination[1] + 1):
            s = str(i)
            first_half, second_half = s[:int(len(s)/2)], s[int(len(s)/2):]
            if first_half == second_half:
                r += i
    return r

def part_two():
    r = 0
    for combination in combinations:
        for i in range(combination[0], combination[1] + 1):
            s = str(i)
            for j in range(1, int(len(s)/2) + 1):
                first_part = s[:j]
                if s.count(first_part) * len(first_part) == len(s):
                    r += i
                    break
    return r

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))