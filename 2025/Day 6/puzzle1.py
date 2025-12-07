import sys
import re

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 6, DataType.SPLITLINES)

sum = 0

row1 = data[0]
row1 = re.sub(' +', ' ', row1)
row1 = row1.strip().split(" ")

row2 = data[1]
row2 = re.sub(' +', ' ', row2)
row2 = row2.strip().split(" ")

row3 = data[2]
row3 = re.sub(' +', ' ', row3)
row3 = row3.strip().split(" ")

row4 = data[3]
row4 = re.sub(' +', ' ', row4)
row4 = row4.strip().split(" ")

row5 = data[4]
row5 = re.sub(' +', ' ', row5)
row5 = row5.strip().split(" ")

for i, y in enumerate(row5):
    match y:
        case '*':
            sum += int(row1[i]) * int(row2[i]) * int(row3[i]) * int(row4[i])
        case '+':
            sum += int(row1[i]) + int(row2[i]) + int(row3[i]) + int(row4[i])
    
print(sum)