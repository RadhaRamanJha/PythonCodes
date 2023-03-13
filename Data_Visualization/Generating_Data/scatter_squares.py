import matplotlib.pyplot as plt
#input values and relations
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
# plot of the input
plt.style.use('ggplot')
fig, ax = plt.subplots()

ax.scatter(x_values,y_values,c= y_values,cmap= plt.cm.Greens,edgecolors= 'none' ,s=20)

#Title and axis labels
ax.set_title("Square of numbers",fontsize = 24)
ax.set_xlabel("Number",fontsize = 14)
ax.set_ylabel("Square",fontsize = 14)

# set size of tick labels
ax.tick_params(axis = 'both', labelsize = 14)

# set the range of each axis
ax.axis([0,1100,0,1100000])
plt.show()