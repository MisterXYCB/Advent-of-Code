sum = 0
lines1 = []
lines2 = []
perfect_list = {}
not_allowed = []


with open("Day 5/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        if ("|" in line):
            lines1.append(line.split("|"))
        else:
            lines2.append(line.split(","))

for instructions in lines1:
    if(instructions[1] not in perfect_list):
        perfect_list[instructions[1]] = [int(instructions[1])]
    if(instructions[0] not in perfect_list):
        perfect_list[instructions[0]] = [int(instructions[0])]
        tmp = perfect_list[instructions[0]].copy()
        tmp.append(int(instructions[1]))
        perfect_list[instructions[0]] = tmp.copy()
    else:
        tmp = perfect_list[instructions[0]].copy()
        tmp.append(int(instructions[1]))
        perfect_list[instructions[0]] = tmp.copy()

for update in lines2:
    allowed = True
    for instructions in lines1:
        if((instructions[0] in update and instructions[1] in update) and (update.index(instructions[0]) > update.index(instructions[1]))):
            allowed = False
            not_allowed.append(update)
            break

for ele in not_allowed:
    i = 0
    while i + 1 < len(ele):
        if(int(ele[i]) in perfect_list[ele[i + 1]]):
            ele.insert(i+1, ele.pop(i))
            if i > 0:
                i -= 1
        elif(int(ele[i + 1]) in perfect_list[ele[i]]):
            i += 1
        else:
            pass
            
    sum += int(ele[len(ele)//2])

print(sum)