import re

sum = 0
merged_str = ""

with open("Day 3/data.txt") as f:
    data = f.readlines()

for line in data:
    merged_str += line.replace("\n", "")

merged_str = re.sub("don't\(\).*?do\(\)", "", merged_str)

multiplications = re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", merged_str)

for mul in multiplications:
    mul = mul.replace("mul(", "").replace(")", "")

    mul1, mul2 = mul.split(",")

    sum += int(mul1) * int(mul2)

print(sum)