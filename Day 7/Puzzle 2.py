test_values = []
value_list = []
sum = 0

with open("Day 7/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        test_values.append(line.split(": ")[0])
        value_list.append(line.split(": ")[1].split(" "))

test_values = [int(numeric_string) for numeric_string in test_values]

def check_possible(target_value, start_value, values):
    values2 = values.copy()
    values3 = values.copy()
    if(values == None or len(values) == 0):
        return int(target_value) == int(start_value)
    elif(target_value < start_value):
        return False
    else:
        return check_possible(target_value, start_value * int(values.pop(0)), values) or check_possible(target_value, start_value + int(values2.pop(0)), values2) or check_possible(target_value, int(str(start_value) + str(values3.pop(0))), values3)

for i, value in enumerate(test_values):
    if(check_possible(int(value), int(value_list[i].pop(0)), value_list[i].copy())):
        sum += value

print(sum)