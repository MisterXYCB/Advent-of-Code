#Advent of Code 2023 Day 2 Puzzle 2
import re

games = []
result = 0

with open("2023/Day 2/data.txt") as f:
    for line in f:
        games.append(re.sub("Game .+: ", "", line).replace("\n", "").split("; "))


for i in range(len(games)):

    pulls = []
    minRed = 0
    minBlue = 0
    minGreen = 0
    
    for round in games[i]:
        
        if "," in round:

            for pull in round.split(", "):
                
                pulls.append(pull)        

        else:
            
            pulls.append(round)

    for pull in pulls:

        amount, color = pull.split(" ")

        if color == "red" and int(amount) > minRed:
            minRed = int(amount)
            
        if color == "blue" and int(amount) > minBlue:
            minBlue = int(amount)

        if color == "green" and int(amount) > minGreen:
            minGreen = int(amount)
    
    result  += minRed * minBlue * minGreen


print(result) #Result is 66016
