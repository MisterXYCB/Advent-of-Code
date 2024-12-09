import copy

data = []

with open("Day 9/data.txt") as f:
    for y, line in enumerate(f):
        line = line.replace("\n", "")
        data = list(line)

def inputToMemoryAllocation(inputArr: list) -> list:
    freeSpace = False
    id = 0
    memoryAllocation = []
    for element in inputArr:
        if(freeSpace):
            toAllocate = [int(element), "."]
        else:
            toAllocate = [int(element), id]
            id += 1
        memoryAllocation.append(toAllocate)
        freeSpace = not freeSpace
    
    return memoryAllocation

def compact(toCompact: list) -> None:
    reversedList = copy.deepcopy(toCompact)
    reversedList.reverse()
    elementsAdded = 0
    for i, element in enumerate(reversedList):
        print(str(round(i / len(reversedList), 10)) + " progress, length of to compact =", len(toCompact), end="\r")
        j = 0
        if(element[1] == "."):
            continue
        while j < len(toCompact):
            if(toCompact[j][1] == "."):
                if(toCompact[j][0] == element[0]):
                    index = toCompact.index(element)
                    if(index <= j):
                        break
                    toCompact[index][1] = "."
                    toCompact[j][1] = element[1]
                    j += 1
                    break
                elif(toCompact[j][0] > element[0]):
                    index = toCompact.index(element)
                    if(index <= j):
                        break
                    toCompact[index][1] = "."
                    toCompact[j][0] = toCompact[j][0] - element[0]
                    toCompact.insert(j, copy.copy(element))
                    elementsAdded += 1
                    break
                else:
                    j += 1
                    continue
            else:
                j += 1
                continue
    


def calculateCheckSum(placeholder: list) -> int:
    checkSum = 0
    i = 0
    for element in placeholder:
        if(element[1] == "."):
            i += element[0]
            continue
        for _ in range(0, element[0]):
            checkSum += i * int(element[1])
            i += 1
    return checkSum


data = inputToMemoryAllocation(data)
compact(data)
print("\n")
print(calculateCheckSum(data))