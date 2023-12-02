#Advent of Code 2015 Day 4 Puzzle 1

import hashlib

input = "bgvyzdsv"
result = ""

for i in range(100_000_000):
    result = hashlib.md5(str(input + str(i)).encode())

    if result.hexdigest().startswith("00000"):
        print(i) #254575
        break

print(result.hexdigest()) #000004b30d481662b9cb0c105f6549b2