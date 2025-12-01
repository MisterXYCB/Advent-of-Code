from Robot import Robot
from collections import defaultdict

quadrants = defaultdict(int)
robots = []

with open("Day 14/data.txt") as f:
    for y, line in enumerate(f):
        line = line.replace("\n", "").replace("p=", "")
        position, velocity = line.split(" v=")
        x, y = position.split(",")
        velocityX, velocityY = velocity.split(",")
        robots.append(Robot(x, y, velocityX, velocityY))

for robot in robots:
    robot.calculateNewPosition()
    quadrants[robot.getQuadrant()] += 1
    print(quadrants)

safetyFactor = 1
for i in range(4):
    print(quadrants[i])
    safetyFactor *= quadrants[i]

print(safetyFactor) # 224413254 < x < 227876880
