from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die
# Creating two imstance of die D6
die_1 = Die()
die_2 = Die()
# making  rolls for the die storing result
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# analyze the result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides 
for value in range(2,max_result+1):
    occurance = results.count(value)
    frequencies.append(occurance)

# Visualize the results
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_configration = {'title': 'Result', 'dtick': 1}
y_axis_configation = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling two D6 5000 times',xaxis=x_axis_configration,yaxis=y_axis_configation)
offline.plot({'data':data,'layout':my_layout}, filename='d6_d6.html')