data = []

with open("Day 13/data.txt") as f:
    data = f.read().split("\n\n")


def minCost(prizes, aValues, bValues):
    divider = aValues[0]*bValues[1] - aValues[1]*bValues[0]
    if divider == 0:
        return 0
    aButtonPresses = (prizes[0]*bValues[1] - prizes[1]*bValues[0]) / divider
    bButtonPresses = (prizes[1]*aValues[0] - prizes[0]*aValues[1]) / divider

    if(aButtonPresses.is_integer() and bButtonPresses.is_integer() and aButtonPresses > -1 and bButtonPresses > -1):
        return (3 * aButtonPresses + bButtonPresses)
    
    return 0

sum = 0
for ele in data:
    inputs = ele.split("\n")
    aValues = [int(x) for x in inputs[0].replace("Button A: X+", "").replace("Y+", "").split(", ")]
    bValues = [int(x) for x in inputs[1].replace("Button B: X+", "").replace("Y+", "").split(", ")]
    prizes = [int(x) for x in inputs[2].replace("Prize: X=", "").replace("Y=", "").split(", ")]
    
    sum += minCost(prizes, aValues, bValues)

print(int(sum))

