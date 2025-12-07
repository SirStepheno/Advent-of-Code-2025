class Item:
    def __init__(self, type, x, y):
        self.type = type
        self.x, self.y = x, y
    
    def __repr__(self):
        return self.type

class Grid:
    def __init__(self, lines):
        self.grid = []
        for y, row in enumerate(lines):
            self.grid.append([])
            for x, item in enumerate(row):
                self.grid[-1].append(Item(item, x, y))
    
    def __repr__(self):
        r = ""
        for row in self.grid:
            row = [str(x) for x in row]
            r += "".join(row) + "\n"
        return r