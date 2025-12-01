import re

sum = 0

with open("Day 3/data.txt") as f:
    data = f.readlines()

multiplications = [re.findall("mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)", line) for line in data]

for multiplication in multiplications:
    for mul in multiplication:
        mul = mul.replace("mul(", "").replace(")", "")

        mul1, mul2 = mul.split(",")

        sum += int(mul1) * int(mul2)

print(sum)