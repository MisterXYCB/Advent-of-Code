#Advent of Code 2023 Day 6 Puzzle 2
import re

result = 1

with open("Day 6/data.txt") as f:
    string = re.sub(r" ", "", f.read().replace("Time:", "").replace("Distance:", ""))

inputs = string.split("\n")

for i in range(int(inputs[0])):

    if i * (int(inputs[0]) - i) > int(inputs[1]):

        result = result * (int(inputs[0]) - 2 * i + 1)
        break

print(result) # 35349468
