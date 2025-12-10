from itertools import combinations

with open("Day 9/test.txt") as f:
    lines = [line[:-1] for line in f.readlines()]
    corners = [tuple(map(int, line.split(","))) for line in lines]

def part_one():
    r = 0
    for combi in combinations(corners, 2):
        p1, p2 = combi
        if (d := abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)) > r:
            r = d
    return r

def check_every_tile(p1,p2,tiles_v, tiles_h, tiles):
    # Check every tile
    x1,y1 = p1
    x2,y2 = p2
    coords = [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]

    # Check if corners are inside
    for p in coords:
        if p in tiles:
            continue
        
        if not is_point_in_path(p[0], p[1], corners):
            return False
    
    # Check if one of the tiles between corners
    for i in range(len(coords)):
        p1,p2 = coords[i-1], coords[i]
        if p1[1] == p2[1]:
            # Vertical, check horizontal lines
            coords_col = {c for c in tiles_h if c[0] == p1[0] and c[1] in range(min(p1[1], p2[1])+1, max(p1[1], p2[1]))}
            if len(coords_col) > 0:
                print(coords_col)
                return False
        elif p1[0] == p2[0]:
            # Horizontal, check vertical lines
            coords_row = {c for c in tiles_v if c[1] == p1[1] and c[0] in range(min(p1[0], p2[0])+1, max(p1[0], p2[0]))}
            if len(coords_row) > 0:
                print(coords_row)
                return False
    return True

def is_point_in_path(x: int, y: int, poly: list[tuple[int, int]]) -> bool:
    """Determine if the point is on the path, corner, or boundary of the polygon

    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is in the path or is a corner or on the boundary"""
    c = False
    for i in range(len(poly)):
        ax, ay = poly[i]
        bx, by = poly[i - 1]
        if (x == ax) and (y == ay):
            # point is a corner
            return True
        if (ay > y) != (by > y):
            slope = (x - ax) * (by - ay) - (bx - ax) * (y - ay)
            if slope == 0:
                # point is on boundary
                return True
            if (slope < 0) != (by < ay):
                c = not c
    return c

def part_two():
    tiles_v = set()
    tiles_h = set()
    # Add last first corner to the end, because list wraps
    c = corners + [corners[0]]
    for i in range(len(c)-1):
        p1, p2 = c[i], c[i+1]
        if p1[1] == p2[1]:
            # Horizontal
            for x in range(abs(p1[0] - p2[0]) + 1):
                tiles_h.add((min(p1[0], p2[0]) + x, p1[1]))
        elif p1[0] == p2[0]:
            # Vertical
            for y in range(abs(p1[1] - p2[1]) + 1):
                tiles_v.add((p1[0], min(p1[1], p2[1]) + y))
        else:
            raise ValueError(f"Diagonal? {p1, p2}")
        
    # Sanity check, all tiles in both sets must be corners
    if set(corners) != tiles_h.intersection(tiles_v):
        raise ValueError(f"Should be the same: {set(corners), tiles_h.intersection(tiles_v)}")
    
    # Calculate all distances, sort highest to lowest
    combis = []
    for combi in combinations(corners, 2):
        p1, p2 = combi
        combis.append((p1,p2,abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)))

    combis = sorted(combis, key=lambda x: x[2], reverse=True)

    # Combine all tiles
    tiles = tiles_h.union(tiles_v)
    # tiles_v = tiles_v.difference(set(corners))
    # tiles_h = tiles_h.difference(set(corners))
    
    r = 0
    # Calculate areas and check if all spaces are inside
    for p1,p2,d in combis:
        area = abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1)

        # Check if area could be bigger
        if area <= r:
            continue
        
        if not check_every_tile(p1,p2,tiles_v, tiles_h, tiles):
            continue

        return d


import time
startTime = time.time()
print(f"Part one: {part_one()}")
print('Execution time part one in seconds: ' + str((time.time() - startTime)))

startTime1 = time.time()
print(f"Part two: {part_two()}")

# 4581338553

print('Execution time part two in seconds: ' + str((time.time() - startTime1)))
print('Execution time both parts: ' + str((time.time() - startTime)))