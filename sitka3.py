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

plt.title("Daily High Temperatures, July 2018", fontsize = 16)    #THIS IS YOUR HOMEWORK... but you want highs and lows for 
                                                                  #sitka and death valley, you should be able to use either file
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperature (F)", fontsize = 12)
plt.tick_params(axis="both", which = "both", labelsize = 12)

plt.plot(dates, highs, c="red",alpha=0.5) #alpha indicates darkness of lines
plt.plot(dates,lows, c="blue", alpha=0.5)
fig.autofmt_xdate() #auto format the x axis with the dates

plt.fill_between(dates, highs, lows, facecolor ="blue", alpha = 0.1)

plt.show()

plt.subplot(2,1,1) #2 rows, 1 column, 1 to choose 1st row
plt.plot(dates,highs,c="red")
plt.title("Highs")
 
plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")

plt.show() #Will not show second graph until we close out first