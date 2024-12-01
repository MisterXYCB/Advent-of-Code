#Advent of Code 2023 Day 6 Puzzle 1
import re

rounds = []
result = 1

with open("2023/Day 6/data.txt") as f:
    string = re.sub(r" {1,}", " ", f.read().replace("Time:        ", "").replace("Distance:   ", ""))

inputs = string.split("\n")
times = inputs[0].split(" ")
length = inputs[1].split(" ")

for i in range(4):

    rounds.append([int(times[i]), int(length[i])])


for round in rounds:

    for i in range(int(round[0])):

        if i * (round[0] - i) > round[1]:

            result = result * (round[0] - 2 * i + 1)
            break

print(result) # 1710720
