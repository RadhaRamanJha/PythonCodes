import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    # make a random walk for pollen grain
    rw = RandomWalk(5000)
    rw.fill_walk()
    
    # ploting the path of pollen grain
    plt.style.use('seaborn-v0_8-dark-palette')
    # fig, ax = plt.subplots(figsize =(10,6), dpi = 128) # altering the size of plot
    fig, ax = plt.subplots()
    # point_numbers = range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values, linewidth = .25, c= "orange")
    # ax.plot(0,0, c = 'green') -- to be used in ax.scatter()
    # ax.plot(rw.x_values[-1],rw.y_values[-1],c='red')
    
    # Remove the axes
    ax.set_title("Pollen Grain Path",fontsize = 24)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    keep_running = input("Make another walk for pollen grain (y/n): ")
    if keep_running == 'n':
        break