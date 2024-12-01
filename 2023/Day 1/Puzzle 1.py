#Advent of Code 2023 Day 1 Puzzle 1

lines = []
result = 0

with open("2023/Day 1/data.txt") as f:
    for line in f:
        lines.append(line)

for line in lines:
    
    numbers = []
    
    for _, char in enumerate(line):
        if char.isdigit():
            numbers.append(char)
            
    result += int(numbers[0] + numbers[-1])

print(result) #Result is 54239
