import sys
sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2016, 1, DataType.LINE)

data = data.split(", ")

direction = 0
north = 0
east = 0

placesVisited = [(0, 0)]

for instruction in data:
    match instruction[0]:
        case "L":
            direction -= 1
        case "R":
            direction += 1
    
    direction = direction % 4

    match direction:
        case 0:
            for _ in range(1, int(instruction[1:]) + 1):
                north += 1
                if (north, east) in placesVisited:
                    break
                placesVisited.append((north, east))
        case 1:
            for _ in range(1, int(instruction[1:]) + 1):
                east += 1
                if (north, east) in placesVisited:
                    break
                placesVisited.append((north, east))
        case 2:
            for _ in range(1, int(instruction[1:]) + 1):
                north -= 1
                if (north, east) in placesVisited:
                    break
                placesVisited.append((north, east))
        case 3:
            for _ in range(1, int(instruction[1:]) + 1):
                east -= 1
                if (north, east) in placesVisited:
                    break
                placesVisited.append((north, east))

print(placesVisited)
print(abs(north) + abs(east))
