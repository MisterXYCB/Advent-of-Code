roboX = 0
roboY = 0

def getGpsSum(map: list) -> int:
    sum = 0
    
    for y, row in enumerate(map):
        for x, pos in enumerate(row):
            if(pos == "["):
                sum += 100 * y + x
    
    return sum

def moveBox(direction, posY, posX):
    match (direction):
        case "^":
            if map[posY - 1][posX] == "." and map[posY - 1][posX + 1] == ".":
                pass
            elif map[posY - 1][posX] == "[":
                moveBox("^", posY - 1, posX)
            elif map[posY - 1][posX] == "]" and map[posY - 1][posX + 1] == ".":
                moveBox("^", posY - 1, posX - 1)
            elif map[posY - 1][posX] == "]" and map[posY - 1][posX + 1] == "[":
                moveBox("^", posY - 1, posX - 1) 
                moveBox("^", posY - 1, posX + 1)
            elif map[posY - 1][posX + 1] == "[":
                moveBox("^", posY - 1, posX + 1)
            map[posY - 1][posX] = "["
            map[posY - 1][posX + 1] = "]"
            map[posY][posX] = "."
            map[posY][posX + 1] = "."
        
        case "v":
            if map[posY + 1][posX] == "." and map[posY + 1][posX + 1] == ".":
                pass
            elif map[posY + 1][posX] == "[":
                moveBox("v", posY + 1, posX)
            elif map[posY + 1][posX] == "]" and map[posY + 1][posX + 1] == ".":
                moveBox("v", posY + 1, posX - 1)
            elif map[posY + 1][posX] == "]" and map[posY + 1][posX + 1] == "[":
                moveBox("v", posY + 1, posX - 1)
                moveBox("v", posY + 1, posX + 1)
            elif map[posY + 1][posX + 1] == "[":
                moveBox("v", posY + 1, posX + 1)
            map[posY + 1][posX] = "["
            map[posY + 1][posX + 1] = "]"
            map[posY][posX] = "."
            map[posY][posX + 1] = "."

        case "<":
            map[posY][posX - 1] = "["
            map[posY][posX] = "]"
            map[posY][posX + 1] = "."
        
        case ">":
            map[posY][posX + 1] = "["
            map[posY][posX + 2] = "]"
            map[posY][posX] = "."



def canMove(direction, posY, posX, player):
    match (direction):
        case "^":
            if player:
                if map[posY - 1][posX] == "#":
                    return False
                if map[posY - 1][posX] == ".":
                    return True
                elif map[posY - 1][posX] == "[":
                    if(canMove("^", posY - 1, posX, False)):
                        moveBox("^", posY - 1, posX)
                        return True
                elif map[posY - 1][posX] == "]":
                    if(canMove("^", posY - 1, posX - 1, False)):
                        moveBox("^", posY - 1, posX - 1)
                        return True
            else:
                toReturn = False
                if map[posY - 1][posX] == "#" or map[posY - 1][posX + 1] == "#":
                    return False
                elif map[posY - 1][posX] == "." and map[posY - 1][posX + 1] == ".":
                    toReturn = True
                elif map[posY - 1][posX] == "[":
                    toReturn = canMove("^", posY - 1, posX, False)
                elif map[posY - 1][posX] == "]" and map[posY - 1][posX + 1] == ".":
                    toReturn = canMove("^", posY - 1, posX - 1, False)
                elif map[posY - 1][posX] == "]" and map[posY - 1][posX + 1] == "[":
                    toReturn = canMove("^", posY - 1, posX - 1, False) and canMove("^", posY - 1, posX + 1, False)
                elif map[posY - 1][posX + 1] == "[":
                    toReturn = canMove("^", posY - 1, posX + 1, False)
                if(toReturn):
                    return True
                else:
                    return False
                
        case "v":
            if player:
                if map[posY + 1][posX] == "#":
                    return False
                if map[posY + 1][posX] == ".":
                    return True
                elif map[posY + 1][posX] == "[":
                    if(canMove("v", posY + 1, posX, False)):
                        moveBox("v", posY + 1, posX)
                        return True
                elif map[posY + 1][posX] == "]":
                    if(canMove("v", posY + 1, posX - 1, False)):
                        moveBox("v", posY + 1, posX - 1)
                        return True
            else:
                toReturn = False
                if map[posY + 1][posX] == "#" or map[posY + 1][posX + 1] == "#":
                    return False
                elif map[posY + 1][posX] == "." and map[posY + 1][posX + 1] == ".":
                    return True
                elif map[posY + 1][posX] == "[":
                    toReturn = canMove("v", posY + 1, posX, False)
                elif map[posY + 1][posX] == "]" and map[posY + 1][posX + 1] == ".":
                    toReturn = canMove("v", posY + 1, posX - 1, False)
                elif map[posY + 1][posX] == "]" and map[posY + 1][posX + 1] == "[":
                    toReturn = canMove("v", posY + 1, posX - 1, False) and canMove("v", posY + 1, posX + 1, False)
                elif map[posY + 1][posX + 1] == "[":
                    toReturn = canMove("v", posY + 1, posX + 1, False)
                if(toReturn):
                    return True
                else:
                    return False
                
        case "<":
            if player:
                if map[posY][posX - 1] == "#":
                    return False
                if map[posY][posX - 1] == ".":
                    return True
                elif map[posY][posX - 1] == "]":
                    return canMove("<", posY, posX - 2, False)
            else:
                if map[posY][posX - 1] == "#":
                    return False
                elif map[posY][posX - 1] == ".":
                    moveBox("<", posY, posX)
                    return True
                elif map[posY][posX - 1] == "]":
                    if canMove("<", posY, posX - 2, False):
                        moveBox("<", posY, posX)
                        return True
                    else:
                        return False
        
        case ">":
            if player:
                if map[posY][posX + 1] == "#":
                    return False
                if map[posY][posX + 1] == ".":
                    return True
                elif map[posY][posX + 1] == "[":
                    return canMove(">", posY, posX + 1, False)
            else:
                if map[posY][posX + 2] == "#":
                    return False
                elif map[posY][posX + 2] == ".":
                    moveBox(">", posY, posX)
                    return True
                elif map[posY][posX + 2] == "[":
                    if canMove(">", posY, posX + 2, False):
                        moveBox(">", posY, posX)
                        return True
                    else: 
                        return False
                
def move(direction, posY, posX):
    global roboY
    global roboX

    match (direction):
        case "^":
            if canMove(direction, posY, posX, True):
                roboY -= 1
                map[posY - 1][posX] = map[posY][posX]
                map[posY][posX] = "."
       
        case "v":
            if canMove(direction, posY, posX, True):
                roboY += 1
                map[posY + 1][posX] = map[posY][posX]
                map[posY][posX] = "."
        
        case "<":
            if canMove(direction, posY, posX, True):
                roboX -= 1
                map[posY][posX - 1] = map[posY][posX]
                map[posY][posX] = "."
       
        case ">":
            if canMove(direction, posY, posX, True):
                roboX += 1
                map[posY][posX + 1] = map[posY][posX]
                map[posY][posX] = "."

with open("Day 15/data.txt") as f:
    map, instructions = f.read().split("\n\n")

instructions = list(instructions.replace("\n", ""))
map = map.split("\n")

for i, row in enumerate(map):
    row = row.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
    if("@" in row):
        roboX = row.index("@")
        roboY = i
    map[i] = list(row)

for instruction in instructions:
    move(instruction, roboY, roboX)
for row in map:
    print("".join(row))


print(getGpsSum(map))