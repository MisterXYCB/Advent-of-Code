import sys

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 3, DataType.SPLITLINES)

maxJoltage = 0

for line in data:
    leftJoltage = int(line[0])
    rightJoltage = int(line[1])
    for char in line[2:]:
        char = int(char)
        if(leftJoltage * 10 + char < rightJoltage * 10 + char):
            leftJoltage = rightJoltage
            rightJoltage = char
        elif(rightJoltage <  char):
            rightJoltage = char
    maxJoltage += leftJoltage * 10 + rightJoltage
        

print(maxJoltage)