from itertools import combinations

with open("Day 10/test.txt") as f:
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
    combinations = set([tuple([button]) for button in buttons])
    while True:
        print(combinations)
        new_combinations = set()
        for combi in combinations:
            for add_button in buttons:
                combi_test = combi + tuple((add_button,1))
                print(combi_test)
                joltage_test = [0 for _ in range(len(joltage))]

                # Do combination and check if lights_test equals lights
                for button in combi_test:
                    for x in button:
                        joltage_test[x] += 1
                
                print(combi_test, joltage, joltage_test)
                if joltage_test == joltage:
                    return len(combi_test)
                
                # If one of the joltages is to high, don't add them to next round
                print([(j - j_test) >= 0 for j, j_test in zip(joltage, joltage_test)])
                if all([(j - j_test) >= 0 for j, j_test in zip(joltage, joltage_test)]):
                    new_combinations.add(sorted(combi_test))
    
        combinations = new_combinations
        print(combinations)


def part_one():
    r = 0
    for lights, buttons, joltage in machines:
        r += get_fewest_clicks_lights(lights, buttons)
    return r

def part_two():
    r = 0
    for lights, buttons, joltage in machines:
        r += get_fewest_clicks_joltage(buttons, joltage)
    return r

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))