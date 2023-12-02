#Advent of Code 2015 Day 5 Puzzle 2

import re

input = []
result = 0

with open("2015/Day 5/data.txt") as f:
    for line in f:
        input.append(line.replace("\n", ""))

for string in input:
    isNice = True

    if re.search(r"(\w).\1{1,}", string=string) is None:
        isNice = False
        continue

    if re.search(r"(\w\w).*\1{1,}", string=string) is None:
        isNice = False
        continue
    
    if isNice:
        result += 1

print(result) #69
