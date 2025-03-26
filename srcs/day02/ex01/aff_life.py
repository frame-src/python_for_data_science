import matplotlib.pyplot as plt

from srcs.day02.

def draw_my_country(country:str = "Germany"):
    data = load("life_expectancy_years.csv")
    for row in data:
        if row[0] == country:
            fig, ax = plt.subplots()
            t = range(100)
            x = float(row[1:])
            lines = ax.plot(t,x)

