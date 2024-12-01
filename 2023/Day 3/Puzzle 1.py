#Advent of Code 2023 Day 3 Puzzle 1

from string import digits

result = 0
numbers = []
symbols = []

with open("2023/Day 3/data.txt") as f:
    for x, line in enumerate(f):
        
        number_str = ""
        number_coords = []

        for y, char in enumerate(line.replace("\n", "")):

            if char in digits:

                number_str += char
                number_coords.append([x, y])

            elif number_str:

                numbers.append([int(number_str), number_coords])
                number_str = ""
                number_coords = []
            
            if char not in digits and char != ".":

                symbols.append([x, y])
        
        if number_str:

            numbers.append([int(number_str), number_coords])
            number_str = ""
            number_coords = []

        
adjacent_coords = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1]
]

for number, coords in numbers:

    is_adjacent = False
    
    for coord in coords:

        for adjacent in adjacent_coords:

            adjacent_coord = [coord[0] + adjacent[0], coord[1] + adjacent[1]]

            if adjacent_coord in symbols:
                
                result += number
                is_adjacent = True
                break

        if is_adjacent:
            break
            
print(result) #527369
