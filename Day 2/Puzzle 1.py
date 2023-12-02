#Advent of Code 2023 Day 2 Puzzle 1
import re

games = []
result = 0

with open("Day 2/data.txt") as f:
    for line in f:
        games.append(re.sub("Game .+: ", "", line).replace("\n", "").split("; "))


for i in range(len(games)):

    pulls = []
    possible = True
    
    for round in games[i]:
        
        if "," in round:

            for pull in round.split(", "):
                
                pulls.append(pull)        

        else:
            
            pulls.append(round)

    for pull in pulls:

        amount, color = pull.split(" ")

        if color == "red" and int(amount) > 12:
            possible = False
            break
            
        elif color == "blue" and int(amount) > 14:
            possible = False
            break

        elif color == "green" and int(amount) > 13:
            possible = False
            break
    
    if possible:
        result  += i + 1


print(result) #Result is 2541
