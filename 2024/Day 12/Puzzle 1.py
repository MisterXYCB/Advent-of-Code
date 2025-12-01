from collections import defaultdict

map = []
areas = {}
areaNeighbors = defaultdict(int)
areasArea = defaultdict(int)
differentAreas = 0

with open("Day 12/data.txt") as f:
    for y, line in enumerate(f):
        line = line.replace("\n", "")
        map.append(list(line))

def getNeighbors(y, x, type):
    neighbors = []
    if(y > 0):
        if(map[y-1][x] == type):
            neighbors.append([y-1, x])
    if(x > 0):
        if(map[y][x-1] == type):
            neighbors.append([y, x-1])
    if(y < len(map) - 1):
        if(map[y+1][x] == type):
            neighbors.append([y+1, x])
    if(x < len(line) - 1):
        if(map[y][x+1] == type):
            neighbors.append([y, x+1])
    
    return neighbors

def findUniqueAreas():
    global differentAreas
    knowPlaces = []
    for y, line in enumerate(map):
        for x, space in enumerate(line):
            if([y,x] not in knowPlaces):
                knowNeighbors = [[y,x]]
                neighbors = getNeighbors(y, x, space)
                knowNeighbors.extend(neighbors)
                knowPlaces.extend(knowNeighbors)

                areaName = "Area" + str(differentAreas)
                areas[str(y)+str(x)] = areaName
                areaNeighbors[areaName] += len(neighbors)
                areasArea[areaName] += 1

                while len(neighbors) > 0:
                    newNeighbors = []
                    newNeighbors2 = []
                    for neighbor in neighbors:
                        areas[str(y)+str(x)] = areaName
                        areaNeighbors[areaName] += len(getNeighbors(neighbor[0], neighbor[1], space))
                        areasArea[areaName] += 1
                        newNeighbors.extend(getNeighbors(neighbor[0], neighbor[1], space))
                    for neighbor in newNeighbors:
                        if(neighbor not in knowNeighbors):
                            knowNeighbors.append(neighbor)
                            newNeighbors2.append(neighbor)
                    if(len(newNeighbors2) == 0):
                        break

                    knowPlaces.extend(newNeighbors2)
                    knowNeighbors.extend(newNeighbors2)
                    neighbors = newNeighbors2
                
                differentAreas += 1

findUniqueAreas()

sum = 0
for i in range(differentAreas):
    perimeter = areasArea["Area"+str(i)] * 4 - areaNeighbors["Area"+str(i)]
    print(perimeter, areasArea["Area"+str(i)], areaNeighbors["Area"+str(i)])
    sum += perimeter * areasArea["Area"+str(i)]
    
print(sum)