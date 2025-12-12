from itertools import combinations
import pulp as pl

with open("Day 10/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    machines = []
    for line in lines:
        m = []
        x = line.split(" ")
        
        # Lights
        d = {"#": True, ".": False}
        lights = [d[a] for a in x[0] if a in d.keys()]

        # Buttons
        buttons = []
        for b in x[1:len(x)-1]:
            b = b[1:len(b)-1]
            b = b.split(",")
            b = tuple(int(a) for a in b)
            buttons.append(b)

        # Joltage
        joltage = x[-1]
        joltage = joltage[1:len(joltage)-1]
        joltage = joltage.split(",")
        joltage = [int(a) for a in joltage]

        machines.append((lights, buttons, joltage))

def get_fewest_clicks_lights(lights, buttons):
    i = 1
    while True:
        for combi in combinations(buttons, i):
            lights_test = [False for _ in range(len(lights))]

            # Do combination and check if lights_test equals lights
            for button in combi:
                for x in button:
                    lights_test[x] = not lights_test[x]
            
            if lights_test == lights:
                return i
        i +=1

def get_fewest_clicks_joltage(buttons, joltage):
    prob = pl.LpProblem('problem', pl.LpMinimize)

    button_vars = [pl.LpVariable(f"b{i}", lowBound=0, cat=pl.LpInteger) for i, button in enumerate(buttons)]

    button_counters = [[button_vars[i] for i, tup in enumerate(buttons) if jol_i in tup] for jol_i in range(len(joltage))]

    for i, button_counter in enumerate(button_counters):
        prob += sum(button_counter) == joltage[i]

    prob += sum(button_vars)

    prob.solve(pl.PULP_CBC_CMD(msg=0)) # Calculate silent

    return prob.objective.value()

def part_one():
    r = 0
    for lights, buttons, joltage in machines:
        r += get_fewest_clicks_lights(lights, buttons)
    return r

def part_two():
    r = 0
    for lights, buttons, joltage in machines:
        r += get_fewest_clicks_joltage(buttons, joltage)
    return int(r)

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))