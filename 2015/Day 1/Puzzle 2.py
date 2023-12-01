#Advent of Code 2015 Day 1 Puzzle 2

with open('2015/Day 1/data.txt') as f:
    str = f.readline()

char_list = list(str)

level = 0
result = 1

for i in range(len(char_list)):
    if(char_list[i] == "("):
        level += 1
    
    elif(char_list[i] == ")"):
        level += -1

    if(level == -1):
        result += i
        break

print(result) #1771