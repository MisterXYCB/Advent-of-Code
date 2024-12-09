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
            toAllocate = ["."]
        else:
            toAllocate = [id]
            id += 1
        memoryAllocation.extend(toAllocate * int(element))
        freeSpace = not freeSpace
    
    return memoryAllocation

def compact(toCompact: list) -> None:
    while "." in toCompact:
        if(toCompact[-1] == "."):
            toCompact.pop(-1)
        else:
            index = toCompact.index(".")
            toCompact.pop(index)
            toCompact.insert(index, toCompact.pop(-1))

def calculateCheckSum(placeholder: list) -> int:
    checkSum = 0 
    for i, element in enumerate(placeholder):
        checkSum += i * int(element)
    return checkSum


data = inputToMemoryAllocation(data)
compact(data)
print(calculateCheckSum(data))