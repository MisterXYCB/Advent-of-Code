letters = []
count = 0

with open("Day 4/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        letters.append(list(line))
        
for i, line in enumerate(letters):
    for j, letter in enumerate(line):
        if(letter == "A"):
            if(j < len(line) - 1 and j > 0):
                if(i < len(letters) - 1 and i > 0):
                    if(((letters[i-1][j-1] == "M" and letters[i+1][j+1] == "S") or (letters[i-1][j-1] == "S" and letters[i+1][j+1] == "M")) and  ((letters[i+1][j-1] == "M" and letters[i-1][j+1] == "S") or (letters[i+1][j-1] == "S" and letters[i-1][j+1] == "M"))):
                            count += 1

print(count)