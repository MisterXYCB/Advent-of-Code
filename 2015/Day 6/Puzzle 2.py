#Advent of Code 2015 Day 6 Puzzle 2

import re
import time

t1 = time.time()

grid = []
instructions = []

with open("2015/Day 6/data.txt") as f:
    for line in f:
        instructions.append(line.replace("\n", ""))

for x in range(1000):

    for y in range(1000):

        grid.append(0)


for instruction in instructions:

    tmp = re.split(r" through ", instruction)

    tmp2 = re.split(r" ", tmp[0])

    if len(tmp2) == 3:
        start_x = tmp2[2].split(",")[0]
        start_y = tmp2[2].split(",")[1]
        todo = tmp2[0] + tmp2[1]
    else:
        start_x = tmp2[1].split(",")[0]
        start_y = tmp2[1].split(",")[1]
        todo = tmp2[0]

    final_x = tmp[1].split(",")[0]
    final_y = tmp[1].split(",")[1]

    match todo:

        case "turnon":

            for x in range(int(start_x), int(final_x) + 1):

                for y in range(int(start_y), int(final_y) + 1):
                    
                    grid[1000*x + y] += 1

        case "turnoff":
            
            for x in range(int(start_x), int(final_x) + 1):

                for y in range(int(start_y), int(final_y) + 1):
                    
                    if grid[1000*x + y] != 0:
                        grid[1000*x + y] += -1

        case "toggle":
            
            for x in range(int(start_x), int(final_x) + 1):

                for y in range(int(start_y), int(final_y) + 1):
                    
                    grid[1000*x + y] += 2

result = 0
for lamp in grid:
    result += lamp

print(result)
print("Needed :", time.time() - t1, " seconds")