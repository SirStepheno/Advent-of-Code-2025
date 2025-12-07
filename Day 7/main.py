from copy import deepcopy

class Item:
    def __init__(self, type, x, y):
        self.type = type
        self.x, self.y = x, y
    
    def __repr__(self):
        return self.type

class Grid:
    def __init__(self, grid, active):
        self.split_count = 0
        self.grid = grid
        self.active = active

    def check_coords(self, x, y):
        if x >= 0 and y >= 0 and x < len(self.grid[0]) and y < len(self.grid):
            return True
        return False
    
    def get_item(self, x, y):
        if self.check_coords(x,y):
            return self.grid[y][x]
        return None
    
    def make_item_active_part_1(self, x, y):
        if item := self.get_item(x,y):
            item.type = "|"
            self.active.append(item)

    def step_part_1(self):
        active_copy = self.active
        self.active = []
        for item in active_copy:
            if (lower_item := self.get_item(item.x, item.y + 1)) is None:
                continue

            if lower_item.type == ".":
                self.make_item_active_part_1(item.x, item.y + 1)
            elif lower_item.type == "^":
                self.make_item_active_part_1(item.x + 1, item.y + 1)
                self.make_item_active_part_1(item.x - 1, item.y + 1)
                self.split_count += 1
            elif lower_item.type == "|":
                pass # Ignore because it is already passed
            else:
                raise ValueError(f"Unknown item {lower_item}")
    
    def make_item_active_part_2(self, x, y):
        if item := self.get_item(x,y):
            # item.type = "|"
            self.active.append(item)
        
    def step_part_2(self):
        active_copy = self.active
        self.active = []
        for item in active_copy:
            if (lower_item := self.get_item(item.x, item.y + 1)) is None:
                continue

            if lower_item.type == ".":
                self.make_item_active_part_2(item.x, item.y + 1)
            elif lower_item.type == "^":
                self.make_item_active_part_2(item.x + 1, item.y + 1)
                self.make_item_active_part_2(item.x - 1, item.y + 1)
            elif lower_item.type == "|":
                pass # Ignore because it is already passed
            else:
                raise ValueError(f"Unknown item {lower_item}")
    
    def __repr__(self):
        r = str(self.active) + "\n"
        for row in self.grid:
            row = [str(x) for x in row]
            r += "".join(row) + "\n"
        return r


with open("Day 7/test.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    active, grid = [], []
    for y, row in enumerate(lines):
        grid.append([])
        for x, item in enumerate(row):
            if item == "S":
                active = [Item("|", x, y)]
                grid[-1].append(active[0])
            else:
                grid[-1].append(Item(item, x, y))

def part_one():
    g = Grid(deepcopy(grid), deepcopy(active))
    while g.active:
        g.step_part_1()
    return g.split_count

def part_two():
    c = 0
    g = Grid(grid, active)
    timelines = active
    while timelines:
        new_timelines = []
        for timeline in timelines:
            g.active = [timeline]
            g.step_part_2()

            if g.active:
                new_timelines += g.active
            else:
                c += 1 # Count every dieing timeline, because this is an alternative one
            
        timelines = new_timelines

        print(len(timelines))
    return c

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))