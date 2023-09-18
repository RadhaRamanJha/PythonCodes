# module imports
import csv
from datetime import datetime
import matplotlib.pyplot as plt

file_name = "Data\\sample_csv_files\\sitka_weather_07-2018_simple.csv"

# Header information at 
# https://github.com/ehmatthes/pcc_2e/blob/master/chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv
# stored as a list

with open(file_name) as f:
    reader = csv.reader(f) 
    header_row = next(reader)

    """ To Realize Which item is at Which position"""
    for index,column_header in enumerate(header_row):
        print(index, column_header)
    
#     Get maximum temprature from the file
    dates,high_tempratures = [],[]
    for row in reader:
        temp =  float(row[5])
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        dates.append(current_date)
        high_tempratures.append(temp)

    
"""Plotting the high temprature data for july 2018"""
plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,high_tempratures, c = 'red')

# Formating The plot
plt.title("Daily high temperatures, July 2018",fontsize = 24)
plt.xlabel(" ", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temp (F)", fontsize = 16)
plt.tick_params(axis="both",which = 'major',labelsize = 16)
plt.show()