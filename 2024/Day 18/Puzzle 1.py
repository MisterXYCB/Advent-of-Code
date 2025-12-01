grid = []
for y in range(71):
    grid.append(["."] * 71)

with open("Day 18/data.txt") as f:
    for y, line in enumerate(f):
        if(y >= 1024):
            break
        line = line.replace("\n", "")
        x, y = line.split(",")
        grid[int(y)][int(x)] = "#"

def walkGrid(y, x, pathUsed: set):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == "#" or (y, x) in pathUsed:
        return float('inf')
    
    if(y == len(grid) - 1 and x == len(grid[0]) - 1):
        return 0

    pathUsed.add((y, x))
    steps = [walkGrid(y-1, x, pathUsed),
             walkGrid(y+1, x, pathUsed),
             walkGrid(y, x-1, pathUsed),
             walkGrid(y, x+1, pathUsed)]
    
    pathUsed.remove((y, x))

    return min(steps) + 1
    
print(walkGrid(0, 0, set()))
for line in grid:
    print("".join(line))
