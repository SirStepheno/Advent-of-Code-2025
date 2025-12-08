from itertools import combinations
from math import prod

class Box():
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x,y,z
        self.group = None
    def __repr__(self):
        return str(hash(self)) + " " + str(self.__dict__)

class Group():
    def __init__(self, id):
        self.id = id
        self.boxes = []
    def print_boxes(self):
        for b in self.boxes:
            print(b)
    def __repr__(self):
        return str(self.id) + " " + str(len(self.boxes))

class Graph():
    def __init__(self, lines):
        self.boxes = []
        self.groups = []
        for line in lines:
            x,y,z = [int(coord) for coord in line.split(",")]
            self.boxes.append(Box(x,y,z))
    
    def connect(self, p1: Box, p2: Box):
        if p1.group == p2.group and p1.group is not None:
            pass # Already in same group
        elif p1.group and not p2.group:
            p2.group = p1.group
            p1.group.boxes.append(p2)
        elif p2.group and not p1.group:
            p1.group = p2.group
            p2.group.boxes.append(p1)
        elif p1.group != p2.group:
            # Delete old group by removing reference in self.groups
            self.groups.remove(p2.group)

            # Transport all from p2 to p1
            p1.group.boxes += p2.group.boxes
            for box in p2.group.boxes:
                box.group = p1.group 

        elif p1.group == p2.group and p1.group is None:
            g = Group(len(self.groups))
            g.boxes += [p1, p2]
            p1.group = p2.group = g
            self.groups.append(g)
        else:
            raise ValueError(f"Unknown situation {p1, p2}")        
    
    def get_distances(self):
        r = []
        combis = list(combinations(self.boxes, 2))
        for combi in combis:
            p1, p2 = combi
            d = ((p1.x - p2.x)**2  + (p1.y - p2.y)**2  + (p1.z - p2.z)**2 )**0.5
            r.append([p1, p2, d])
        
        r.sort(key=lambda x: x[2]) # Sort on distance

        return r
    
    def __repr__(self):
        return "\n".join([str(box) for box in self.boxes])
    


with open("Day 8/input.txt") as f:
    lines = [line[:-1] for line in f.readlines()]

def part_one():
    g = Graph(lines)
    d = g.get_distances()
    for x in range(1000):
        p1, p2, distance = d[x]
        g.connect(p1,p2)
    return prod(sorted(list(set([len(group.boxes) for group in g.groups])), reverse=True)[:3])
    

def part_two():
    g = Graph(lines)
    d = g.get_distances()
    i = -1
    while True:
        i += 1
        p1, p2, distance = d[i]
        g.connect(p1,p2)

        if len(g.groups) == 1 and i > 1 and len(g.groups[0].boxes) == len(g.boxes):
            break

    print(f"Done after {i} iterations")
    print(g.groups)
    p1, p2, distance = d[i]
    return p1.x * p2.x

import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")
print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))