import requests
import os
from vars import COOKIE

def getYear() -> str:
    year = input("Enter the year in which the files should be created. (2015-2025) ")
    if(2014 < int(year) < 2026):
        return year
    print("Not a valid year!")
    return getYear()

def getDay(year: int) -> str:
    match year:
        case 2025:
            day = input("Enter the day. (1-12) (Current year not all days are released!) ")
            if(0 < int(day) < 13):
                return day
            print("Not a valid day!")
            return getDay(year)
        case _:
            day = input("Enter the day. (1-25) ")
            if(0 < int(day) < 26):
                return day
            print("Not a valid day!")
            return getDay(year)

year = getYear()
day = getDay(int(year))

url = f"https://adventofcode.com/{year}/day/{day}/input"
headers = { 'Cookie': COOKIE }
response = requests.get(url, headers=headers)
data = response.text[:-1]

try:
    os.mkdir(f"data/{year}")
except FileExistsError:
    print(f"Data Directory already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create.")
except Exception as e:
    print(f"An error occurred: {e}")  

with open(f"data/{year}/{day}.txt", 'w') as dataFile:
    dataFile.write(data)

try:
    os.mkdir(f"{year}/Day {day}")
except FileExistsError:
    print(f"Directory already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create.")
except Exception as e:
    print(f"An error occurred: {e}")  

with open(f"{year}/Day {day}/puzzle1.py", 'w') as puzzleOneFile:
    puzzleOneFile.write(f'import sys\n\nsys.path.insert(1, "\\\\".join(sys.path[0].split("\\\\")[:4]))\n\nfrom dataLoader import *\n\ndata = getData({year}, {day}, DataType.LINE).split(",")')

with open(f"{year}/Day {day}/puzzle2.py", 'w') as puzzleOneFile:
    puzzleOneFile.write(f'import sys\n\nsys.path.insert(1, "\\\\".join(sys.path[0].split("\\\\")[:4]))\n\nfrom dataLoader import *\n\ndata = getData({year}, {day}, DataType.LINE).split(",")')
