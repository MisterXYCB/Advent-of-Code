#Advent of Code 2015 Day 5 Puzzle 1

import re

input = []
result = 0

with open("2015/Day 5/data.txt") as f:
    for line in f:
        input.append(line.replace("\n", ""))

for string in input:
    isNice = True

    for option in ["ab", "cd", "pq", "xy"]:
        if re.search(option, string=string) is not None:
            isNice = False
            continue
        continue

    if re.search(r"(\w)\1{1,}", string=string) is None:
        isNice = False
        continue

    if re.search(r"[aeiou].*[aeiou].*[aeiou]", string=string) is None:
        isNice = False
        continue
    
    if isNice:
        print(string)
        result += 1

print(result) #238
