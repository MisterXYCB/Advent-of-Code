import sys
from collections import Counter

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2022, 1, DataType.WHOLE)

elves = []
for elv in data.split("\n\n"):
    elves.append(sum([int(i) for i in elv.split("\n")]))

elves.sort(reverse=True)

print(sum(elves[:3]))