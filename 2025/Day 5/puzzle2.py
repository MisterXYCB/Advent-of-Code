import sys

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 5, DataType.WHOLE).split("\n\n")

fresh = 0

freshIDs = data[0].split("\n")
freshIDs = [tuple(map(int, row.split('-'))) for row in freshIDs]
freshIDs = sorted(freshIDs)

for i, (start, end) in enumerate(freshIDs):
    for (start2, end2) in freshIDs[:i]:
        if(start2 <= start <= end2 and start2 <= end <= end2):
            break
        elif(start2 <= start <= end2):
            start = end2 + 1
        elif(start2 <= end <= end2):
            end = start2 - 1
    else:
        fresh += end - start + 1 

print(fresh)
