grid = []
x, y = 0, 0

with open("Day 20/data.txt") as f:
    for i, line in enumerate(f):
        if("E" in line):
            x = i
            y = line.index('E')
        line = line.replace("\n", "")
        row = list(line)
        grid.append(row)

notAtStart = True
i = 0
while notAtStart:
    if(grid[x][y] == "S"): notAtStart = False
    grid[x][y] = i
    if(x < len(grid) - 1 and (grid[x + 1][y] == "." or grid[x + 1][y] == "S")):
        x = x + 1
    elif(x > 0 and (grid[x - 1][y] == "." or grid[x - 1][y] == "S")):
        x = x - 1
    elif(y < len(grid[x]) - 1 and (grid[x][y + 1] == "." or grid[x][y + 1] == "S")):
        y = y + 1
    elif(y > 0 and (grid[x][y - 1] == "." or grid[x][y - 1] == "S")):
        y = y - 1
    i += 1

shortcuts = 0
#cheats = set()
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if(grid[x][y] == "#"):
            continue
        if(x < len(grid) - 2 and grid[x + 1][y] == "#" and grid[x + 2][y] != "#" and int(grid[x][y]) > int(grid[x + 2][y])):
            #cheats.add(((int(grid[x][y]) - int(grid[x + 2][y]) - 2), (x, y), (x + 2, y)))
            if(int(grid[x][y]) - int(grid[x + 2][y]) - 2 > 99):
                shortcuts += 1
        if(x > 1 and grid[x - 1][y] == "#" and grid[x - 2][y] != "#" and int(grid[x][y]) > int(grid[x - 2][y])):
           #cheats.add(((int(grid[x][y]) - int(grid[x - 2][y]) - 2), (x, y), (x - 2, y)))
            if(int(grid[x][y]) - int(grid[x - 2][y]) - 2 > 99):
                shortcuts += 1
        if(y < len(grid[x]) - 2 and grid[x][y + 1] == "#" and grid[x][y + 2] != "#" and int(grid[x][y]) > int(grid[x][y + 2])):
            #cheats.add(((int(grid[x][y]) - int(grid[x][y + 2]) - 2), (x, y), (x, y + 2)))
            if(int(grid[x][y]) - int(grid[x][y + 2]) - 2 > 99):
                shortcuts += 1
        if(y > 1 and grid[x][y - 1] == "#" and grid[x][y - 2] != "#" and int(grid[x][y]) > int(grid[x][y - 2])):
            #cheats.add(((int(grid[x][y]) - int(grid[x][y - 2]) - 2), (x, y), (x, y - 2)))
            if(int(grid[x][y]) - int(grid[x][y - 2]) - 2 > 99):
                shortcuts += 1

print(shortcuts)
