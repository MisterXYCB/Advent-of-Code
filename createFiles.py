import requests
import os
from vars import COOKIE

def getYear() -> str:
    year = input("Enter the year in which the files should be created. (2015-2025) ").strip()
    if(2014 < int(year) < 2026):
        return year
    print("Not a valid year!")
    return getYear()

def getDay(year: int) -> str:
    match year:
        case 2025:
            day = input("Enter the day. (1-12) (Current year not all days are released!) ").strip()
            if(0 < int(day) < 13):
                return day
            print("Not a valid day!")
            return getDay(year)
        case _:
            day = input("Enter the day. (1-25) ").strip()
            if(0 < int(day) < 26):
                return day
            print("Not a valid day!")
            return getDay(year)

year = getYear()
day = getDay(int(year))

try:
    os.mkdir(f"data/{year}")
    print(f"Created data directory for Year {year}.")
except FileExistsError:
    print(f"Data Directory already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create.")
except Exception as e:
    print(f"An error occurred: {e}")  

if not os.path.exists(f"data/{year}/{day}.txt"):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = { 'Cookie': COOKIE }
    response = requests.get(url, headers=headers)
    data = response.text[:-1]

    with open(f"data/{year}/{day}.txt", 'w') as dataFile:
        dataFile.write(data)
    print(f"Created data file for Year {year} Day {day}.")
else:
    print(f"Data file already exists.")

try:
    os.mkdir(f"{year}/Day {day}")
    print(f"Created directory for Year {year} Day {day}.")
except FileExistsError:
    print(f"Directory already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create.")
except Exception as e:
    print(f"An error occurred: {e}")

if not os.path.exists(f"{year}/Day {day}/puzzle1.py"):
    with open(f"{year}/Day {day}/puzzle1.py", 'w') as puzzleOneFile:
        puzzleOneFile.write(f'import sys\n\nsys.path.insert(1, "\\\\".join(sys.path[0].split("\\\\")[:4]))\n\nfrom dataLoader import *\n\ndata = getData({year}, {day}, DataType.LINE).split(",")')
    print(f"Created puzzle1.py for Year {year} Day {day}.")
else:
    print(f"puzzle1.py already exists.")

if not os.path.exists(f"{year}/Day {day}/puzzle2.py"):
    with open(f"{year}/Day {day}/puzzle2.py", 'w') as puzzleTwoFile:
        puzzleTwoFile.write(f'import sys\n\nsys.path.insert(1, "\\\\".join(sys.path[0].split("\\\\")[:4]))\n\nfrom dataLoader import *\n\ndata = getData({year}, {day}, DataType.LINE).split(",")')
    print(f"Created puzzle2.py for Year {year} Day {day}.")
else:
    print(f"puzzle2.py already exists.")

if not os.path.exists(f"{year}/Day {day}/description.md"):
    url = f"https://adventofcode.com/{year}/day/{day}"
    headers = { 'Cookie': COOKIE }
    response = requests.get(url, headers=headers)
    data = response.text

    with open(f"{year}/Day {day}/description.md", 'w') as puzzleOneFile:
        puzzleOneFile.write(data)
    print(f"Created description.md for Year {year} Day {day}.")
else:
    print(f"description.md already exists.")

print("All files created!")