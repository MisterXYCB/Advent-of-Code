import copy

steps = 1
rows = []
loops = 0
startFacing = 0
startGuardY = 0
startGuardX = 0

def isInfinite(map, guardX, guardY, facing):
    placesVisited = []
    guardInMap = True
    while guardInMap:
        match facing:
            case 0:
                if(guardY < 1):
                    guardInMap = False
                elif(map[guardY - 1][guardX] != "#"):
                    guardY -= 1
                    if([guardY, guardX, facing] not in placesVisited):
                        placesVisited.append([guardY, guardX, facing])
                    else:
                        return True
                else:
                    facing += 1
            case 1:
                if(guardX > len(map[guardY]) - 2):
                    guardInMap = False
                elif(map[guardY][guardX + 1] != "#"):
                    guardX += 1
                    if([guardY, guardX, facing] not in placesVisited):
                        placesVisited.append([guardY, guardX, facing])
                    else:
                        return True
                else:
                    facing += 1
            case 2:
                if(guardY > len(map) - 2):
                    guardInMap = False
                elif(map[guardY + 1][guardX] != "#"):
                    guardY += 1
                    if([guardY, guardX, facing] not in placesVisited):
                        placesVisited.append([guardY, guardX, facing])
                    else:
                        return True
                else:
                    facing += 1
            case 3:
                if(guardX < 1):
                    guardInMap = False
                elif(map[guardY][guardX - 1] != "#"):
                    guardX -= 1
                    if([guardY, guardX, facing] not in placesVisited):
                        placesVisited.append([guardY, guardX, facing])
                    else:
                        return True
                else:
                    facing = 0
    return False


with open("Day 6/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        rows.append(list(line))

for i, row in enumerate(rows):
    if("^" in row):
        startGuardY = i
        startGuardX = row.index("^")

for i, row in enumerate(rows):
    for j in range(0, len(row)):
        print("Working on: [" + str(i) + "|" + str(j) + "] ", end="\r")
        startMap = copy.deepcopy(rows)
        if(startMap[i][j] != "."):
            continue
        startMap[i][j] = "#"
        if(isInfinite(startMap, startGuardX, startGuardY, startFacing)):
            loops += 1
            
print(str(loops))