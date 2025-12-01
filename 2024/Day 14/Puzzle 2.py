import png
from Robot import Robot
from collections import defaultdict

robots = []

with open("Day 14/data.txt") as f:
    for y, line in enumerate(f):
        line = line.replace("\n", "").replace("p=", "")
        position, velocity = line.split(" v=")
        x, y = position.split(",")
        velocityX, velocityY = velocity.split(",")
        robots.append(Robot(x, y, velocityX, velocityY))


for i in range(10_000):
    positions = []
    for robot in robots:
        robot.calculateNextPosition()
        positions.append(robot.getPos())
    img = []
    for y in range(103):
        row = ()
        for x in range(101):
            row = row + ((255, 255, 255) if [x, y] in positions else (0, 0, 0))
        img.append(row)

    with open("Day 14/images/" + str(i) + ".png", 'wb') as f:
        w = png.Writer(101, 103, greyscale=False)
        w.write(f, img)
