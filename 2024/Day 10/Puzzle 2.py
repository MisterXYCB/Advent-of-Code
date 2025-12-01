map = []
sum = 0

with open("Day 10/data.txt") as f:
    for y, line in enumerate(f):
        line = line.replace("\n", "")
        map.append(list(line))

def getScore(position):
    y, x, height = position
    nextPositions = []
    finalPositions = []
    if(x > 0 and int(map[y][x - 1]) == (height + 1)):
        nextPositions.append([y, x - 1, height + 1])
    if(x < len(map[y]) - 1 and int(map[y][x + 1]) == (height + 1)):
        nextPositions.append([y, x + 1, height + 1])
    if(y > 0 and int(map[y - 1][x]) == (height + 1)):
        nextPositions.append([y - 1, x, height + 1])
    if(y < len(map) - 1 and int(map[y + 1][x]) == (height + 1)):
        nextPositions.append([y + 1, x, height + 1])
    if(height == 8):
        return nextPositions
    for position in nextPositions:
        finalPositions.extend(getScore(position))
    if(height == 0):
        return len(finalPositions)
    return finalPositions


for y, line in enumerate(map):
    for x, height in enumerate(line):
        if(height == "0"):
            position = [y, x, 0]
            sum += getScore(position)

print(sum)