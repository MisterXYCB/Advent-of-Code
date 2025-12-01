import re

steps = 1
rows = []
facing = 0
guardY = 0
guardX = 0
guardInMap = False


with open("Day 6/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        rows.append(list(line))

for i, row in enumerate(rows):
    if("^" in row):
        guardY = i
        guardX = row.index("^")
        guardInMap = True
        row[guardX] = "X"

print(guardX, guardY)

while guardInMap:
    match facing:
        case 0:
            if(guardY < 1):
                guardInMap = False
            elif(rows[guardY - 1][guardX] != "#"):
                guardY -= 1
                if(rows[guardY][guardX] != "X"):
                    steps += 1
                    rows[guardY][guardX] = "X"
            else:
                facing += 1
        case 1:
            if(guardX > len(rows[guardY]) - 2):
                guardInMap = False
            elif(rows[guardY][guardX + 1] != "#"):
                guardX += 1
                if(rows[guardY][guardX] != "X"):
                    steps += 1
                    rows[guardY][guardX] = "X"
            else:
                facing += 1
        case 2:
            if(guardY > len(rows) - 2):
                guardInMap = False
            elif(rows[guardY + 1][guardX] != "#"):
                guardY += 1
                if(rows[guardY][guardX] != "X"):
                    steps += 1
                    rows[guardY][guardX] = "X"
            else:
                facing += 1
        case 3:
            if(guardX < 1):
                guardInMap = False
            elif(rows[guardY][guardX - 1] != "#"):
                guardX -= 1
                if(rows[guardY][guardX] != "X"):
                    steps += 1
                    rows[guardY][guardX] = "X"
            else:
                facing = 0

for row in rows:
    print("".join(row))

print(steps)