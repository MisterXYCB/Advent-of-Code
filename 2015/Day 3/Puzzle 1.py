#Advent of Code 2015 Day 3 Puzzle 1

coords = [[0, 0]]

with open('2015/Day 3/data.txt') as f:
    input = f.readline()

for i in range(len(input)):
    
    if input[i] == "<":
        coords.append([coords[-1][0], coords[-1][1] - 1])

    if input[i] == ">":
        coords.append([coords[-1][0], coords[-1][1] + 1])
    
    if input[i] == "v":
        coords.append([coords[-1][0] - 1, coords[-1][1]])

    if input[i] == "^":
        coords.append([coords[-1][0] + 1, coords[-1][1]])


unique_coords = []
unique_coords_count = 0

for coord in coords:
    if coord not in unique_coords:
        unique_coords_count += 1
        unique_coords.append(coord)


print(unique_coords_count) #2592