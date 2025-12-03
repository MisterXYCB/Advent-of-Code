import sys
import itertools

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 3, DataType.SPLITLINES)

maxJoltage = 0

for line in data:
    line = list(line)
    bestList = []
    start = 0
    for i in range(11, 0, -1):
        best = 0
        bestPos = 0
        for pos, char in enumerate(line[start:-i]):
            char = int(char)
            if(char > best):
                best = char
                bestPos = pos + 1
        bestList.append(str(best))
        start += bestPos
    best = 0
    bestPos = 0
    for pos, char in enumerate(line[start:]):
        char = int(char)
        if(char > best):
            best = char
            bestPos = pos + 1
    bestList.append(str(best))
    start += bestPos
    maxJoltage += int("".join(bestList))


print(maxJoltage)
