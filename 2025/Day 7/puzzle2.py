import sys

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 7, DataType.GRID)

splits = 0

nums = []

for _ in range(0, len(data)):
    nums.append([0] * len(data[0]))

for i in range(1, len(data)):
    for y in range(0, len(data[i])):
        if(data[i-1][y] == "S"):
            nums[i][y] += 1
            data[i][y] = "|"
        if(data[i-1][y] == "|"):
            if(data[i][y] == "^"):
                nums[i][y-1] += nums[i-1][y]
                nums[i][y+1] += nums[i-1][y]
                data[i][y-1] = "|"
                data[i][y+1] = "|"
                splits += 1
            else:
                nums[i][y] += nums[i-1][y]
                data[i][y] = "|"

for i in range(0, len(nums)):
    print("".join(data[i]))

print(sum(nums[-1]))