import matplotlib.pyplot as plt
"""pyplot module contains a number of functions that generate charts and plots."""

# background settings of figure
plt_styles_available = plt.style.available
for background in plt_styles_available:
    plt.style.use(background)

    # plot datas
    input_values = range(1,10)
    cubes = [x**3 for x in input_values]

    even_numbers = range(2,10,2)
    even_cubes = [even_number**3 for even_number in even_numbers]
    
    # assignment of tuple returned by subplots() function
    fig,ax = plt.subplots()
    """subplots() function can generates multiple plots in the same figure. The variable "fig" represents the entire figure or collection of plots that
    are generated. The variable "ax" represents a single plot in the figure and is the variable to be used most of the time."""
    
    ax.plot(input_values, cubes, linewidth = 5, color = "yellow")
    ax.scatter(even_numbers,even_cubes,120,"red")
    
    """use the plot() method, which will try to plot the data it is given in a meaningful way."""
    
    # Set chart title and label axis 
    ax.set_title("Cubes", fontsize = 24, color = "Red", ha = "center", weight = "bold")
    ax.set_xlabel("Values", fontsize = 14, color = "green", ha = "left")
    ax.set_ylabel("Value Cubes", fontsize = 14, color = "blue", ha = "right")
    
    ax.plot(input_values, cubes, linewidth = 5, color = "yellow")
    
    plt.show()
    """function plt.show() opens Matplotlib viewer and displays the plot"""