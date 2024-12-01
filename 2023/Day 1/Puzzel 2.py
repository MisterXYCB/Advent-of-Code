#Advent of Code 2023 Day 1 Puzzle 2

lines = []
result = 0

number_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

with open("2023/Day 1/data.txt") as f:
    for line in f:
        lines.append(line)

def translate_numbers(lines):
    
    new_lines = []

    for line in lines:
        for key, value in number_dict.items():
            line = line.replace(key, key[:int(key.__len__() / 2)] + value + key[int(key.__len__() / 2):])
        
        new_lines.append(line)
    
    return new_lines

for line in translate_numbers(lines):
    
    numbers = []
    
    for _, char in enumerate(line):
        if char.isdigit():
            numbers.append(char)

    result += int(numbers[0] + numbers[-1])



print(result) #Result is 55343
