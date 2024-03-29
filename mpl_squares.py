import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=25)
ax.set_xlabel("Value", fontsize=15)
ax.set_ylabel("Square of Value", fontsize=15)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=15)

plt.show()
