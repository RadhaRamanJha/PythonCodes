import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fruits = ["Apple", "BlueBerry", "Cherry", "Orange"]
counts = [45,100,45,30]
bar_label = ["red", "blue", "_red", "orange"]
bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange"]
ax.bar(fruits, counts, label = bar_label, color = bar_colors)
ax.set_title("Fruits counts by color",fontsize = 24)
ax.set_ylabel("Fruit Count",fontsize = 14)
ax.legend(title = "Fruit Color")
plt.show()