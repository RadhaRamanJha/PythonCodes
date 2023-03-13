import matplotlib.pyplot as plt
from modified_random_walk import MdifiedRandomWalk
while True:
    md_rw = MdifiedRandomWalk(10000)
    md_rw.fill_walk()
    plt.style.use('tableau-colorblind10')
    fig,ax = plt.subplots()
    ax.scatter(md_rw.x_values,md_rw.y_values,s=10)
    ax.set_title("Plot for modified random walk",fontsize = 24)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_walking = input("Make another walk(y/n) ? : ")
    if keep_walking == 'n':
        break