stones = [0]

def getEvolvedStones(stones: list) -> list:
    evolvedStones = []
    for stone in stones:
        if(stone == 0):
            evolvedStones.append(1)
        elif(len(str(stone)) % 2 == 0):
            stoneList = list(str(stone))
            evolvedStones.extend([int("".join(stoneList[:len(stoneList)//2])), int("".join(stoneList[len(stoneList)//2:]))])
        else:
            evolvedStones.append(stone * 2024)
        
    return evolvedStones

for i in range(25):
    stones = getEvolvedStones(stones)

print(len(stones))