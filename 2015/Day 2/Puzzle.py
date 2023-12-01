#Advent of Code 2015 Day 2 Puzzle 2

inputs = []
result = 0

with open('2015/Day 2/data.txt') as f:
    for line in f:
        inputs.append(line.replace("\n", "").split("x"))

for input in inputs:
    
    clean_input = [int(i) for i in input]
    clean_input.sort()
    
    ribbon = 2 * clean_input[0] + 2 * clean_input[1] + clean_input[0] * clean_input[1] * clean_input[2] # 2 two times the two shortest + all of them multiplied
    result += ribbon

print(result) #3737498