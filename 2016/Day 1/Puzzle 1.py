import sys
sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2016, 1, DataType.LINE)

data = data.split(", ")

direction = 0
north = 0
east = 0
south = 0
west = 0

for instruction in data:
    match instruction[0]:
        case "L":
            direction -= 1
        case "R":
            direction += 1
    
    direction = direction % 4

    match direction:
        case 0:
            north += int(instruction[1:])
        case 1:
            east += int(instruction[1:])
        case 2:
            south += int(instruction[1:])
        case 3:
            west += int(instruction[1:])

print(abs(north - south) + abs(east - west))
