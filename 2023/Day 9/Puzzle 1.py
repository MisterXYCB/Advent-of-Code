import sys
sys.path.insert(1, "\\".join(sys.path[0].split("\\")[:4]))

from dataLoader import *

data = getData(2023, 9, DataType.SPLITLINES)
