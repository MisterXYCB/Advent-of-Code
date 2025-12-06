import sys

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 5, DataType.WHOLE).split("\n\n")

fresh = 0

freshIDs = data[0].split("\n")
ingredients = data[1].split("\n")

for ingredient in ingredients:
    ingredient = int(ingredient)
    for freshID in freshIDs:
        freshID = freshID.split("-")
        start = int(freshID[0])
        end = int(freshID[1])
        if (start <= ingredient <= end):
            fresh += 1
            break

print(fresh)
