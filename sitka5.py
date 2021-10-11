import matplotlib.pyplot as plt
import csv 
from datetime import datetime

open_file = open("death_valley_2018_simple.csv","r")

open_file2 = open("sitka_weather_2018_simple.csv","r")

csv_file = csv.reader(open_file, delimiter = ",")

csv_file2 = csv.reader(open_file2, delimiter = ",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

print(type(header_row))
print(type(header_row2))

for index, column_header in enumerate (header_row):
    print(index, column_header)

for index, column_header in enumerate (header_row2):
    print(index, column_header)

highs = []
dates =[]
lows = []
highs2 = []
lows2 = []
dates2 = []

#Testing the datetime strptime function
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
#print(mydate)
#print(type(mydate))

for rec in csv_file:     #Death Valley Graph
    try:
        the_date = datetime.strptime(rec[2], '%Y-%m-%d')
       
        high = int(rec[4])                     
        low = int(rec[5])                      
        
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(high)
        dates.append(the_date)
        lows.append(low)                        #This is still a loop, it will do this for every record, if no error then it goes from try to else then LOOP

for rec in csv_file2:    #Sitka Graph
    try:
        the_date = datetime.strptime(rec[2], '%Y-%m-%d')
       
        high = int(rec[5])                     
        low = int(rec[6])                      
        
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs2.append(high)
        dates2.append(the_date)
        lows2.append(low)         




fig = plt.figure()

plt.subplot(2,1,2) #Death Valley
plt.plot(dates,highs,c="red",alpha = .5)
plt.plot(dates,lows,c="blue",alpha = .5)
plt.title("Death Valley, CA US")
plt.xlabel('',fontsize = 12)
#plt.ylabel('Temp (F)', fontsize = 12)
plt.tick_params(axis = "both", which ="both", labelsize = 11)
fig.autofmt_xdate()
plt.fill_between(dates, highs, lows, facecolor = "blue", alpha =.1)

#ALASKA

plt.subplot(2,1,1) #2 rows, 1 column, 1 to choose 1st row
plt.plot(dates2,highs2,c="red", alpha = .5)
plt.plot(dates2,lows2,c="blue", alpha =.5)
plt.title("Sitka Airport, AK US")

plt.xlabel('', fontsize = 12)
#plt.ylabel('Temp (F)', fontsize =12)
plt.tick_params(axis = "both", which = "both", labelsize = 11) 
fig.autofmt_xdate()
plt.suptitle('Temperature Comparison Between Sitka Airport, AK US and Death Valley, CA US', fontsize = 11)
plt.fill_between(dates2, highs2, lows2, facecolor ='blue', alpha =.1)





plt.show() #Will not show second graph until we close out first

