import sys
from pathlib import Path
import os
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "srcs/day02"))

from ex00.load_csv import load

def test_ex_00():
    print(os.getcwd())
    print(load("../docs/life_expectancy_years.csv"))
    print(load("rwerwerw"))
    print(load("../docs/empty.csv"))

test_ex_00()

