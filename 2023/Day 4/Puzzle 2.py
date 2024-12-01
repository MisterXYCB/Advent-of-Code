#Advent of Code 2023 Day 4 Puzzle 2
import re

cards = []
score = 0
scores = []
result = 0

with open("2023/Day 4/data.txt") as f:
    for line in f:
        cards.append(re.sub("Card .+: ", "", line).replace("\n", "").split(" | "))


for card in cards:
    numbers = card[0].split(" ")
    
    winning_numbers = [int(ele) for ele in numbers if ele != "" and ele != " "]

    numbers = card[1].split(" ")

    your_numbers = [int(ele) for ele in numbers if ele != "" and ele != " "]

    for number in your_numbers:
        if number in winning_numbers:
            score += 1

    scores.append([1, score])
    score = 0

for i, data in enumerate(scores):

    count, score = data

    for j in range(score):

        if i + score - j >= len(scores):
            continue

        scores[i + score - j][0] = scores[i + score - j][0] + 1 * count

    result += int(count)

print(result) #7185540