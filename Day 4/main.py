with open("Day 4/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

class Item():
    def __init__(self, sign):
        self.type = sign
    
    def __repr__(self):
        return self.type

class Grid():
    def __init__(self, lines):
        self.grid = [[Item(sign) for sign in row] for row in lines]
    
    def find_item(self, item):
        for y, row in enumerate(self.grid):
            for x, p in enumerate(row):
                if p == item:
                    return x,y
        raise ValueError("Item not found")
    
    def get_neighbours_count(self, item):
        x,y = self.find_item(item)
        r = 0
        for x_check in range(x-1, x+2):
            for y_check in range (y-1, y+2):
                # Don't count itself
                if x_check == x and y_check == y:
                    continue

                # Check out of bound
                if x_check < 0 or y_check < 0 or x_check >= len(self.grid[0]) or y_check >= len(self.grid):
                    continue
                
                if self.grid[y_check][x_check].type == "@":
                    r += 1
        return r
    
    def __repr__(self):
        r = ""
        for row in self.grid:
            row = [str(x) for x in row]
            r += " ".join(row) + "\n"
        return r

def part_one():
    g = Grid(lines)
    r = 0
    for row in g.grid:
        for item in row:
            if item.type == "@" and g.get_neighbours_count(item) < 4:
                r += 1
    return r

def part_two():
    g = Grid(lines)
    r, c = 0, 1
    while c > 0:
        c = 0
        for row in g.grid:
            for item in row:
                if item.type == "@" and g.get_neighbours_count(item) < 4:
                    r += 1
                    c += 1
                    item.type = "." # Removes the item
        print(f"Removed {c} rolls!")
    return r

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))