roboX = 0
roboY = 0

def getGpsSum(map: list) -> int:
    sum = 0
    
    for y, row in enumerate(map):
        for x, pos in enumerate(row):
            if(pos == "O"):
                sum += 100 * y + x
    
    return sum

def move(direction, posY, posX):
    global roboY
    global roboX

    match (direction):
        case "^":
            if map[posY - 1][posX] == "#":
                return False
            elif map[posY - 1][posX] == "O":
                if(move("^", posY - 1, posX)):
                    if(map[posY][posX] == "@"):
                        roboY -= 1
                    map[posY - 1][posX] = map[posY][posX]
                    map[posY][posX] = "."
                    return True
                else:
                    return False
            elif map[posY - 1][posX] == ".":
                if(map[posY][posX] == "@"):
                    roboY -= 1
                map[posY - 1][posX] = map[posY][posX]
                map[posY][posX] = "."
                return True
        
        case "<":
            if map[posY][posX - 1] == "#":
                return False
            elif map[posY][posX - 1] == "O":
                if(move("<", posY, posX - 1)):
                    if(map[posY][posX] == "@"):
                        roboX -= 1
                    map[posY][posX - 1] = map[posY][posX]
                    map[posY][posX] = "."
                    return True
                else:
                    return False
            elif map[posY][posX - 1] == ".":
                if(map[posY][posX] == "@"):
                    roboX -= 1
                map[posY][posX - 1] = map[posY][posX]
                map[posY][posX] = "."
                return True
        
        case ">":
            if map[posY][posX + 1] == "#":
                return False
            elif map[posY][posX + 1] == "O":
                if(move(">", posY, posX + 1)):
                    if(map[posY][posX] == "@"):
                        roboX += 1
                    map[posY][posX + 1] = map[posY][posX]
                    map[posY][posX] = "."
                    return True
                else:
                    return False
            elif map[posY][posX + 1] == ".":
                if(map[posY][posX] == "@"):
                    roboX += 1
                map[posY][posX + 1] = map[posY][posX]
                map[posY][posX] = "."
                return True
        
        case "v":
            if map[posY + 1][posX] == "#":
                return False
            elif map[posY + 1][posX] == "O":
                if(move("v", posY + 1, posX)):
                    if(map[posY][posX] == "@"):
                        roboY += 1
                    map[posY + 1][posX] = map[posY][posX]
                    map[posY][posX] = "."
                    return True
                else:
                    return False
            elif map[posY + 1][posX] == ".":
                if(map[posY][posX] == "@"):
                    roboY += 1
                map[posY + 1][posX] = map[posY][posX]
                map[posY][posX] = "."
                return True


with open("Day 15/data.txt") as f:
    map, instructions = f.read().split("\n\n")

instructions = list(instructions.replace("\n", ""))
map = map.split("\n")

for i, row in enumerate(map):
    if("@" in row):
        roboX = row.index("@")
        roboY = i
    map[i] = list(row)

for instruction in instructions:
    move(instruction, roboY, roboX)

print(getGpsSum(map))