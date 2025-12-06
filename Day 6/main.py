from math import prod

with open("Day 6/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

def calculate_result(sums):
    r = 0
    for s in sums:
        operator = s.pop().strip()
        s = [int(x.strip()) for x in s if x.strip()]
        
        if operator == "+":
            r += sum(s)
        elif operator == "*":
            r += prod(s)
        else:
            raise ValueError(f"Unknown operator {operator}")
    return r

def rotate_matrix(matrix):
    # Rotate matrix
    sums = []
    for i in range(len(matrix[0])):
        sums.append([])
        for j in range(len(matrix)):
            sums[-1].append(matrix[j][i])  

    return sums 

def part_one():
    l = [[number for number in line.split(" ") if number] for line in lines]

    # Rotate matrix
    sums = rotate_matrix(l)

    return calculate_result(sums)

def part_two():
    # Find all common whitespaces
    common_i = [i for i, x in enumerate(lines[0]) if x == " "]
    for i in range(1, len(lines)):
        indices = [i for i, x in enumerate(lines[i]) if x == " "]
        common_i = list(set(common_i).intersection(indices))
    
    # Add first index and sort list
    common_i = sorted([0] + common_i)

    l = []
    # Split strings on the common whitespaces
    for line in lines:
        l.append([line[i:j] for i,j in zip(common_i, common_i[1:]+[None])])
    
    # Rotate matrix
    sums = rotate_matrix(l)

    rotated_sums = []
    # Rotate numbers
    for sum in sums:
        operator = sum.pop()
        rotated_sums.append(["" for _ in range(len(sum[0]))])
        for number in sum:
            for i in range(len(number)):
                rotated_sums[-1][i] += number[i]
        rotated_sums[-1] += [operator]

    return calculate_result(rotated_sums)

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))