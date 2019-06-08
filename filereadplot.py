import matplotlib.pyplot as plt
import csv


x = []
y = []

with open("weather.csv","r") as csvfile:
    plot = csv.reader(csvfile,delimiter=',')
    for row in plot:
        x.append(int(row[0]))
        y.append(int(row[1]))



plt.plot(x,y)
plt.show()