from enum import Enum

class DataType(Enum):
    LINE = "line"
    SPLITLINES = "splitlines"
    GRID = "grid"

def getData(year: int = 2024, day: int = 1, dataType: DataType = DataType.LINE):
    with open(f"data/{year}/{day}.txt") as f:
        match dataType:
            case DataType.LINE:
                line = f.readline()
                line = line.replace("\n", "")
                return line

            case DataType.SPLITLINES:
                lines = []
                for line in f:
                    line = line.replace("\n", "")
                    lines.append(line)
                return lines
            
            case DataType.GRID:
                grid = []
                for line in f:
                    line = line.replace("\n", "")
                    row = list(line)
                    grid.append(row)
                return grid