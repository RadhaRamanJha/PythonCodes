from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die
# Creating instance of die
die = Die()
# making  rolls for the die storing result
results = []
for roll_num in range(5000):
    result = die.roll()
    results.append(result)
# analyze the result
frequencies = [] 
for value in range(1,die.num_sides+1):
    occurance = results.count(value)
    frequencies.append(occurance)
print(frequencies)

# Visualize the results
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_configration = {'title': 'Result'}
y_axis_configation = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling a D6 5000 times',xaxis=x_axis_configration,yaxis=y_axis_configation)
offline.plot({'data':data,'layout':my_layout}, filename='d6.html')