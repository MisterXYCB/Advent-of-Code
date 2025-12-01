operands = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 30118712,
    5: 0,
    6: 0
}

with open("Day 17/data.txt") as f:
    registers, program = f.read().split("\n\n")
    program = program.replace("Program: ", "")
    program = program.split(",")

instructions = [int(x) for x in program]

out = []
i = 0
while i < len(instructions):
    match (instructions[i]):
        case 0:
            operands[4] = int(operands[4] / pow(2, operands[instructions[i+1]]))
            i += 2
        case 1:
            operands[5] = operands[5] ^ instructions[i+1]
            i += 2
        case 2:
            operands[5] = operands[instructions[i+1]] % 8
            i += 2
        case 3:
            if operands[4] == 0:
                i += 2
            else:
                i = instructions[i+1]
        case 4:
            operands[5] = operands[5] ^ operands[6]
            i += 2
        case 5:
            out.append(str(operands[instructions[i+1]] % 8))
            i += 2
        case 6:
            operands[5] = int(operands[4] / pow(2, operands[instructions[i+1]]))
            i +=2
        case 7:
            operands[6] = int(operands[4] / pow(2, operands[instructions[i+1]]))
            i += 2

print(",".join(out))