from collections import defaultdict

sum = 0

stones = defaultdict(int)
for stone in [0]:
    stones[stone] += 1

for _ in range(75):
    newStones = defaultdict(int)
    for stone, stoneCount in stones.items():
        if(stone == 0):
            newStones[1] += stoneCount
        elif(len(str(stone)) % 2 == 0):
            stoneList = list(str(stone))
            newNums = [int("".join(stoneList[:len(stoneList)//2])), int("".join(stoneList[len(stoneList)//2:]))]
            
            for num in newNums:
                newStones[num] += stoneCount
        else:
            newStones[stone * 2024] += stoneCount

    stones = newStones

for value in stones.values():
    sum += value

print(sum)
