import sys
sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *


from collections import Counter
sum = 0

data = getData(2025, 2, DataType.LINE).split(",")

def allEqualCommon(counter: Counter):
    count = -1
    for j, k in counter.most_common():
        if(count == -1):
            count = k
        elif(count % k != 0):
            return False
    return True

def allEven(counter: Counter):
    for j, k in counter.most_common():
        if(k % 2 != 0):
            return False
    return True

for ids in data:
    start, end = ids.split("-")
    for i in range (int(start), int(end)+1):
        string = str(i)
        counter = Counter(string)
        _, count = counter.most_common()[-1]
        if(not allEqualCommon(counter) or count < 2):
            if(allEven(counter)):
                invalid = True
                halfLength = len(string) // 2
                for j in range(0, halfLength):
                    current = string[j]
                    k = j + halfLength
                    while(k < len(string)):
                        if(current != string[k]):
                            invalid = False
                            break
                        k += halfLength
                    if(not invalid):
                        break
                if(invalid):
                    sum += i
            continue
        halfLength = len(string) // count
        invalid = True 
        for j in range(0, halfLength):
            current = string[j]
            k = j + halfLength
            while(k < len(string)):
                if(current != string[k]):
                    invalid = False
                    break
                k += halfLength
            if(not invalid):
                break
        if(invalid):
            sum += i
            continue

print(sum)
