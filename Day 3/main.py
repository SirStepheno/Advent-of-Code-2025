with open("Day 3/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

def get_highest_number(bank):
    return sorted(bank, reverse=True)[0]

def get_bateries(bank: str, num: int):
    r = ""
    for j in reversed(range(num)):
        # Compensate for the fact that for the first number, we can't pick the last one, because than we could not pick enough numbers
        highest = get_highest_number(bank[:len(bank) - j])
        r += highest
        index = bank.index(highest)
        bank = bank[index + 1:]
    return int(r)

def part_one():   
    return sum([get_bateries(bank, 2) for bank in lines])

def part_two():
    return sum([get_bateries(bank, 12) for bank in lines])

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))