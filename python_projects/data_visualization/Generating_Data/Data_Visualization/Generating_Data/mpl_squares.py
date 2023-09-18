import matplotlib.pyplot as plt

square_values = [value**2 for value in range(0,11)]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(square_values, linewidth = 5)

"""Set Chart title and label axes"""
ax.set_title("Square Numbers",fontsize = 24)
ax.set_xlabel("Value",fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

# Set the size of tick labels
ax.tick_params(axis="both",labelsize =15)

plt.show()