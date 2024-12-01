left_list = []
right_list = []
total_distance = 0

with open("Day 1/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        left_list.append(line.split("   ")[0])
        right_list.append(line.split("   ")[1])

left_list.sort()
right_list.sort()

for i, list_item in enumerate(left_list):
    total_distance += abs(int(list_item) - int(right_list[i]))

print(total_distance)