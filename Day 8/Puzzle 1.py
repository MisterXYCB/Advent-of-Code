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
            antinode1 = [antenna[0] + distanceY, antenna[1] + distanceX]
            antinode2 = [secondAntenna[0] - distanceY, secondAntenna[1] - distanceX]
            if(antinode1[0] >= 0 and antinode1[0] < 50 and antinode1[1] >= 0 and antinode1[1] < 50 and antinode1 not in antinodes):
                antinodes.append(antinode1)
            if(antinode2[0] >= 0 and antinode2[0] < 50 and antinode2[1] >= 0 and antinode2[1] < 50 and antinode2 not in antinodes):
                antinodes.append(antinode2)

print(len(antinodes))