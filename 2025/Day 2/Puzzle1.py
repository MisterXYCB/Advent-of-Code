import sys
sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

sum = 0

data = getData(2025, 2, DataType.LINE).split(",")

for ids in data:
    start, end = ids.split("-")
    for i in range (int(start), int(end)+1):
        string = str(i)
        length = len(string)
        if(length % 2 != 0):
            continue
        halfLength = length // 2
        invalid = True 
        for j in range(0, halfLength):
            if(string[j] != string[j + halfLength]):
                invalid = False
                break
        if(invalid):
            sum += i
            print(i)

print(sum)