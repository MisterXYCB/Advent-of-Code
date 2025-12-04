import sys

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2022, 1, DataType.WHOLE)

elves = []
for elv in data.split("\n\n"):
    elves.append(sum([int(i) for i in elv.split("\n")]))

print(max(elves))