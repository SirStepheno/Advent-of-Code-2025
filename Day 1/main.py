with open("Day 1/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    print(lines)

class Dial():
    def __init__(self):
        self.state = 50
        self.count = 0
    
    def do_instruction_A(self, instruction: str):
        direction, ticks = instruction[:1], int(instruction[1:])
        if direction == "R":
            self.state += ticks
        elif direction == "L":
            self.state -= ticks
        else:
            raise ValueError(f"Unknown direction {direction}")

        self.state = self.state % 100
        
        if self.state == 0:
            self.count += 1

    def do_instruction_B(self, instruction: str):
        direction, ticks = instruction[:1], int(instruction[1:])
        print(direction, ticks, self.state)
        if direction == "R":
            for _ in range(ticks):
                self.do(1)
        elif direction == "L":
            for _ in range(ticks):
                self.do(-1)
        else:
            raise ValueError(f"Unknown direction {direction}")
        
        print(self.state, self.count)
    
    def do(self, amount):
        self.state += amount
        
        self.state = self.state % 100

        if self.state == 0:
            self.count += 1

def do_instruction_C(self, instruction: str):
        # TODO fix this exact calculation, is off by couple of 100
        state_before = self.state

        direction, ticks = instruction[:1], int(instruction[1:])
        if direction == "R":
            self.state += ticks
        elif direction == "L":
            self.state -= ticks
        else:
            raise ValueError(f"Unknown direction {direction}")
        
        print(direction, ticks, self.state)
        print(self.state // 100)
        amount_0 = self.state // 100

        # Compensate for fact that 0 and going down is counted 2 times
        if amount_0 < 0 and state_before == 0:
            print("Stefna")
            amount_0 += 1
        
        self.count += abs(amount_0)

        if self.state == 0:
            self.count += 1

        self.state = self.state % 100
        print(self.state)
        print(self.count)        

def part_one():
    dial = Dial()
    for line in lines:
        dial.do_instruction_A(line)
    return dial.count

def part_two():
    dial = Dial()
    for line in lines:
        dial.do_instruction_B(line)
    return dial.count

import time
startTime = time.time()

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))