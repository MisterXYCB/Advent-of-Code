safe_reports = 0
reports = []

with open("Day 2/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        reports.append(line.split(" "))

for _, report in enumerate(reports):
    direction = ""
    for i in range(1, len(report)):
        if(i == 1):
            if(int(report[0]) - int(report[1]) > 0):
                direction = "dec"
            elif(int(report[0]) - int(report[1]) < 0):
                direction = "inc"
            else:
                break
        if(abs((int(report[i - 1]) - int(report[i]))) > 3 or (int(report[i - 1]) - int(report[i])) == 0 or (direction == "inc" and (int(report[i - 1]) - int(report[i])) > 0) or (direction == "dec" and (int(report[i - 1]) - int(report[i])) < 0)):
            break
        elif(i == (len(report) - 1)):
            safe_reports += 1

print(safe_reports)
