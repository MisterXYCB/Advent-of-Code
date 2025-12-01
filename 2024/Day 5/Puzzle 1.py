sum = 0
lines1 = []
lines2 = []


with open("Day 5/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        if ("|" in line):
            lines1.append(line.split("|"))
        else:
            lines2.append(line.split(","))

for update in lines2:
    allowed = True
    for instructions in lines1:
        if((instructions[0] in update and instructions[1] in update) and (update.index(instructions[0]) > update.index(instructions[1]))):
            allowed = False
            continue
    if allowed:
        sum += int(update[int(len(update) //2 )])

print(sum)