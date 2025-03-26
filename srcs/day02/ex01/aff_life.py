import matplotlib.pyplot as plt
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "srcs/day02"))
from ex00.load_csv import load

def draw_my_country(country:str = "Germany"):
    data = load("life_expectancy_years.csv")
    for row in data:
        if row[0] == country:
            fig, ax = plt.subplots()
            t = range(100)
            x = float(row[1:])
            lines = ax.plot(t,x)
            ax.xlabel("Year")
            ax.ylabel("Life Expectancy")
            ax.title("Germany Life Expectancy Projections")
            ax.legend()
            ax.grid()

draw_my_country()