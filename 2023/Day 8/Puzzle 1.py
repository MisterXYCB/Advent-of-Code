maps = {}
steps = 0
starts = {}

with open("2023/Day 8/data.txt") as f:
    instructions = f.readline().replace("\n", "")
    for line in f:
        line = line.replace("\n", "").replace("= ", "").replace("(", ")").replace(")", "").replace(",", "")
        where, toL, toR = line.split(" ")
        if(where.endswith("A")):
            starts[where] = where
        maps[where + "_L"] = toL
        maps[where + "_R"] = toR

is_finished = lambda starts: all((starts[start].endswith("Z")) for start in starts)
while not is_finished(starts):    
    for instruction in instructions:
        for start in starts:
            starts[start] = maps[starts[start] + "_" + instruction]
            
        steps += 1
        print(starts)
        #input1 = input("Next step?")
        if(is_finished(starts)):
            print("break")
            break
        

print(steps)