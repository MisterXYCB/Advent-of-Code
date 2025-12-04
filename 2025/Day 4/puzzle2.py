import sys

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 4, DataType.GRID)


moveIT = 0
changed = True
while changed:
    changed = False
    for y, line in enumerate(data):
        for x, pos in enumerate(line):
            neighbors = 0
            if(data[y][x] == "."):
                continue
            if(y > 0): #check upper neighbors
                if(x > 0): #upper left
                    if(data[y-1][x-1] != "."):
                        neighbors +=1
                if(data[y-1][x] != "."): #upper middle
                    neighbors +=1
                if(x < len(line) - 1): #upper right
                    if(data[y-1][x+1] != "."):
                        neighbors +=1
            
            if(x > 0): #left
                    if(data[y][x-1] != "."):
                        neighbors +=1
            
            if(x < len(line) - 1): #right
                    if(data[y][x+1] != "."):
                        neighbors +=1

            if(y < len(data) - 1):
                if(x > 0): #lower left
                    if(data[y+1][x-1] != "."):
                        neighbors +=1
                if(data[y+1][x] != "."): #lower middle
                    neighbors +=1
                if(x < len(line) - 1): #lower right
                    if(data[y+1][x+1] != "."):
                        neighbors +=1
            if(neighbors < 4):
                changed = True
                data[y][x] = "."
                moveIT += 1
            else:
                if(str(neighbors) != data[y][x]):
                    changed = True
                data[y][x] = str(neighbors)

print(moveIT)