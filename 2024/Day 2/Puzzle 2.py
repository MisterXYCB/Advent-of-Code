safe_reports = 0
reports = []

def is_safe(report):
    direction = ""
    for i in range(1, len(report)):
        if(i == 1):
            if(int(report[0]) - int(report[1]) > 0):
                direction = "dec"
            elif(int(report[0]) - int(report[1]) < 0):
                direction = "inc"
            else:
                return [False, i]
        if(abs((int(report[i - 1]) - int(report[i]))) > 3 or (int(report[i - 1]) - int(report[i])) == 0 or (direction == "inc" and (int(report[i - 1]) - int(report[i])) > 0) or (direction == "dec" and (int(report[i - 1]) - int(report[i])) < 0)):
            return [False, i]
        elif(i == (len(report) - 1)):
            return [True, 1]

with open("Day 2/data.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        reports.append(line.split(" "))

for _, report in enumerate(reports):
    safe, num = is_safe(report)
    alt_report = report.copy()
    if(not safe):
        alt_report.pop(num)
        safe, num = is_safe(alt_report)

    alt_report = report.copy()
    if(not safe):
        alt_report.pop(1)
        safe, num = is_safe(alt_report)

    alt_report = report.copy()
    if(not safe):
        alt_report.pop(0)
        safe, num = is_safe(alt_report)
    
    if(safe):
        safe_reports += 1


print(safe_reports)
