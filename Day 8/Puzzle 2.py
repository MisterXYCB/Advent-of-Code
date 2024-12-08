antennas = []
antinodes = []
with open("Day 8/data.txt") as f:
    for y, line in enumerate(f):
        line = line.replace("\n", "")
        for x, char in enumerate(line):
            if(char != "."):
                antennas.append([y, x, char])

for antenna in antennas:
    for secondAntenna in antennas:
        if(antenna[2] == secondAntenna[2] and antenna[0] != secondAntenna[0] and antenna[1] != secondAntenna[1]):
            distanceY = antenna[0] - secondAntenna[0]
            distanceX = antenna[1] - secondAntenna[1]
            i = 0
            while (antenna[0] + i * distanceY >= 0) and (antenna[0] + i * distanceY < 50) and (antenna[1] + i * distanceX >= 0) and (antenna[1] + i * distanceX < 50): 
                antinode = [antenna[0] + i * distanceY, antenna[1] + i * distanceX]
                if(antinode not in antinodes):
                    antinodes.append(antinode)
                i += 1
            i = 0
            while (secondAntenna[0] - i * distanceY) >= 0 and (secondAntenna[0] - i * distanceY) < 50 and (secondAntenna[1] - i * distanceX >= 0) and (secondAntenna[1] - i * distanceX < 50): 
                antinode = [secondAntenna[0] - i * distanceY, secondAntenna[1] - i * distanceX]
                if(antinode not in antinodes):
                    antinodes.append(antinode)
                i += 1

print(antinodes)
print(len(antinodes))