#Advent of Code 2015 Day 1 Puzzle 1

with open('2015/Day 1/data.txt') as f:
    str = f.readline()

up = str.count("(")
down = str.count(")")

print(up - down) #138