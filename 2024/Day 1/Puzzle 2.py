left_list = []
right_list = []
right_list_sorted = {}
similarity_score = 0

with open("Day 1/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        left_list.append(line.split("   ")[0])
        right_list.append(line.split("   ")[1])

left_list.sort()
right_list.sort()

for _, list_item in enumerate(right_list):
    if(list_item in right_list_sorted):
        right_list_sorted[list_item] += 1
    else:
        right_list_sorted[list_item] = 1

for i, list_item in enumerate(left_list):
    if(list_item in right_list_sorted):
        similarity_score += int(list_item) * right_list_sorted[list_item]

print(similarity_score)