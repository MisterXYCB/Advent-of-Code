#Advent of Code 2015 Day 3 Puzzle 2

with open('2015/Day 3/data.txt') as f:
    input = f.readline()

santa_input = []
robo_input = []

for i in range(len(input)):

    if i%2 == 0:
        santa_input.append(input[i])
    
    else:
        robo_input.append(input[i])

def getCoordsFromInput(inputs):
    coords = [[0, 0]]
    
    for input in inputs:
        if input == "<":
            coords.append([coords[-1][0], coords[-1][1] - 1])

        if input == ">":
            coords.append([coords[-1][0], coords[-1][1] + 1])
        
        if input == "v":
            coords.append([coords[-1][0] - 1, coords[-1][1]])

        if input == "^":
            coords.append([coords[-1][0] + 1, coords[-1][1]])

    return coords

coords = getCoordsFromInput(santa_input) + getCoordsFromInput(robo_input)

unique_coords = []
unique_coords_count = 0

for coord in coords:
    if coord not in unique_coords:
        unique_coords_count += 1
        unique_coords.append(coord)


print(unique_coords_count) #2360