import matplotlib.pyplot as plt
# Input values
values = range(1,5001)
cube_values = [value**3 for value in values]
# Plot of input
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(values,cube_values,c=cube_values,cmap = plt.cm.Reds ,s=10)
# Title and axis labelling
ax.set_title('Cubes upto 5000',fontsize = 24)
ax.set_xlabel('Values',fontsize = 14)
ax.set_ylabel('Cube_Values',fontsize = 14)
# Set the size of tick labels
ax.tick_params(axis='both',which = 'major',labelsize =  14)
# Set Range of axis
ax.axis = [0,5100,0,126000000]
# save the plot
plt.savefig('cube_of_fivethousand.png',bbox_inches = 'tight')