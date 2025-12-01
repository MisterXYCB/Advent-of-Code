import sys
sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

zeroPos = 0
position = 50

data = getData(2025, 1, DataType.SPLITLINES)

for instruction in data:
    direction = instruction[0]
    steps = instruction[1:]
    match direction:
        case 'L':
            position -= int(steps)
        case "R":
            position += int(steps)
    
    position = position % 100
    if(position == 0):
        zeroPos += 1

print(zeroPos)