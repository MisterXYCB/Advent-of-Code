import sys
sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

zeroPos = 0
position = 50
wasZero = False

data = getData(2025, 1, DataType.SPLITLINES)

for instruction in data:
    direction = instruction[0]
    steps = int(instruction[1:])
    match direction:
        case 'L':
            zeroPos += ((-position % 100) + steps) // 100
            position -= steps
        case "R":
            position += steps
            zeroPos += position//100
  
    position = position % 100

print(zeroPos)