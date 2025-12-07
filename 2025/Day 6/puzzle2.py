import sys
import re
import math

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 6, DataType.SPLITLINES)

num = 0

row1 = data[0]

row2 = data[1]
row3 = data[2]

row4 = data[3]

row5 = data[4]


result = [row1[i] + row2[i] + row3[i] + row4[i] + row5[i] for i in range(len(row1))]
result = "".join(result).replace("+", "+ ").replace("*", "* ").split("     ")
toSum = 0

result = [item for item in result if item != ""]
for r in result:
    print(r)
    r = re.sub(" *\+", "+", r)
    r = re.sub(" *\*", "*", r)
    r = r.strip().split(" ")
    toDO = r[0][-1]
    r[0] = r[0][:-1]
    r = [item for item in r if item != ""]
    r = [int(i) for i in r]
    print(r)
    match toDO:
        case '*':
            num += math.prod(r)
        case '+':
            num += sum(r)

print(num)