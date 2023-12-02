#Advent of Code 2015 Day 4 Puzzle 2

import hashlib

input = "bgvyzdsv"
result = ""

for i in range(100_000_000):
    result = hashlib.md5(str(input + str(i)).encode())

    if result.hexdigest().startswith("000000"):
        print(i) #1038736
        break

print(result.hexdigest()) #000000b1b64bf5eb55aad89986126953