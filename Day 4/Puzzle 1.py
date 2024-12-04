letters = []
count = 0

with open("Day 4/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        letters.append(list(line))
        
for i, line in enumerate(letters):
    for j, letter in enumerate(line):
        if(letter == "X"):
            if(j < len(line) - 3):
                if(line[j + 1] == "M" and line[j + 2] == "A" and line[j + 3] == "S"):
                    count += 1
                if(i < len(letters) - 3):
                    if(letters[i+1][j+1] == "M" and letters[i+2][j+2] == "A" and letters[i+3][j+3] == "S"):
                        count += 1
                if(i > 2):
                    if(letters[i-1][j+1] == "M" and letters[i-2][j+2] == "A" and letters[i-3][j+3] == "S"):
                        count += 1
            if(j > 2):
                if(line[j - 1] == "M" and line[j - 2] == "A" and line[j - 3] == "S"):
                    count += 1
                if(i < len(letters) - 3):
                    if(letters[i+1][j-1] == "M" and letters[i+2][j-2] == "A" and letters[i+3][j-3] == "S"):
                        count += 1
                if(i > 2):
                    if(letters[i-1][j-1] == "M" and letters[i-2][j-2] == "A" and letters[i-3][j-3] == "S"):
                        count += 1
            if(i < len(letters) - 3):
                if(letters[i+1][j] == "M" and letters[i+2][j] == "A" and letters[i+3][j] == "S"):
                    count += 1
            if(i > 2):
                if(letters[i-1][j] == "M" and letters[i-2][j] == "A" and letters[i-3][j] == "S"):
                    count += 1

print(count)