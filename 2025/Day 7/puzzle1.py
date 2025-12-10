import sys

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 7, DataType.GRID)

splits = 0

for i in range(1, len(data)):
    for y in range(0, len(data[i])):
        if(data[i-1][y] == "S"):
            data[i][y] = "|"
        if(data[i-1][y] == "|"):
            if(data[i][y] == "^"):
                data[i][y-1] = "|"
                data[i][y+1] = "|"
                splits += 1
            else:
                data[i][y] = "|"

for line in data:
    print("".join(line))

print(splits)