#Advent of Code 2023 Day 4 Puzzle 1
import re

cards = []
score = 0
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
        if number in winning_numbers and score != 0:
            score = 2 * score
        elif number in winning_numbers and score == 0:
            score = 1

    result += score

    score = 0

print(result) #21138