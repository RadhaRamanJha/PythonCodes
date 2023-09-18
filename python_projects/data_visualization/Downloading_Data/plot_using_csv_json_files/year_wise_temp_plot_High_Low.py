# module imports
import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_name = "Data\\sample_csv_files\\sitka_weather_2018_simple.csv"

# Header information at 
# https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv
# stored as a list

with open(file_name) as f:
    reader = csv.reader(f) 
    header_row = next(reader)

    """ To Realize Which item is at Which position"""
    for index,column_header in enumerate(header_row):
        print(index, column_header)
    
#     Get maximum and minimum temprature from the file
    dates,high_tempratures,low_tempratues = [],[],[]
    for row in reader:
        high_temp =  float(row[5])
        low_temp = float(row[6])
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        dates.append(current_date)
        high_tempratures.append(high_temp)
        low_tempratues.append(low_temp)

    
"""Plotting the high and low temprature data"""
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,high_tempratures, c = 'red', alpha = 0.5)
ax.plot(dates,low_tempratues, c = 'blue', alpha = 0.5)
plt.fill_between(dates,high_tempratures,low_tempratues,facecolor = "red", alpha = 0.1)

# Formating The plot
plt.title("Daily high and low temperatures for 2018",fontsize = 25)
plt.xlabel(" ", fontsize = 15)
fig.autofmt_xdate()
plt.ylabel("Temp (F)", fontsize = 15)
plt.tick_params(axis="both",which = 'major',labelsize = 15)
plt.show()