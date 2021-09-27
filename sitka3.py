import matplotlib.pyplot as plt
import csv 
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter = ",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate (header_row):
    print(index, column_header)

highs = []
dates =[]
lows = []
#Testing the datetime strptime function
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(mydate)
print(type(mydate))

for rec in csv_file:
    highs.append(int(rec[5]))
    the_date = datetime.strptime(rec[2], '%Y-%m-%d')
    dates.append(the_date)
    lows.append(int(rec[6]))
    
print(highs)
print(dates)

print(lows)
fig = plt.figure()

plt.title("Daily High Temperatures, July 2018", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis="both", which = "both", labelsize = 12)

plt.plot(dates, highs, c="red",alpha=0.5) #alpha indicates darkness of lines
plt.plot(dates,lows, c="blue", alpha=0.5)
fig.autofmt_xdate() #auto format the x axis with the dates

plt.fill_between(dates, highs, lows, facecolor ="blue", alpha = 0.1)

plt.show()
