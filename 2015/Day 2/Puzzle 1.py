#Advent of Code 2015 Day 2 Puzzle 1

inputs = []
result = 0

with open('2015/Day 2/data.txt') as f:
    for line in f:
        inputs.append(line.replace("\n", "").split("x"))

for input in inputs:
    
    clean_input = [int(i) for i in input]
    clean_input.sort()
    
    wrapping = 2 * clean_input[0] * clean_input[1] + 2 * clean_input[0] * clean_input[2] + 2 * clean_input[1] * clean_input[2] + clean_input[0] * clean_input[1] # 2*l*w + 2*l*h + 2*w*h + two shortest sides multiplied
    result += wrapping

print(result) #1586300