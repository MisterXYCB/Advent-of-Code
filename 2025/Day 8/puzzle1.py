import sys
import math

sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2025, 8, DataType.SPLITLINES)

distances = []

for i, a in enumerate(data[:-1]):
    x1, y1, z1 = a.split(",")
    x1 = int(x1)
    y1 = int(y1)
    z1 = int(z1)
    for b in data[i+1:]:
        x2, y2, z2 = b.split(",")
        x2 = int(x2)
        y2 = int(y2)
        z2 = int(z2)
        distances.append((math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2)), (a, b)))

networks = []

distances = sorted(distances)
distances = distances[:1000]

for distance in distances:
    left = distance[1][0]
    right = distance[1][1]
    leftNetwork = -1
    rightNetwork = -1
    for i, network in enumerate(networks):
        if(left in network):
            leftNetwork = i
        if(right in network):
            rightNetwork = i
    if(leftNetwork == -1 and rightNetwork == -1):
        networks.append([left, right])
    elif(leftNetwork == rightNetwork):
        continue
    elif(leftNetwork == -1):
        networks[rightNetwork].append(left)
    elif(rightNetwork == -1):
        networks[leftNetwork].append(right)
    else:
        networks[leftNetwork] += networks[rightNetwork]
        networks[rightNetwork] = []

networks = sorted(networks, key=len, reverse=True)
sum = len(networks[0]) * len(networks[1]) * len(networks[2])
print(sum)