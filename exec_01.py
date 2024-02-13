import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax = plt.subplots()
x_values = range(1, 5000)
# x_values = range(1, 5)
y_values = [x**3 for x in x_values]

# ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=25)
ax.set_xlabel("Value", fontsize=15)
ax.set_ylabel("Square of Value", fontsize=15)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=15)

# Set the range for each axis.
ax.axis([0, 60, 0, 50000])
# ax.axis([0, 12, 0, 80])
#plt.show()
# plt.savefig('exe1.png', bbox_inches='tight')
# plt.savefig('exe2.png', bbox_inches='tight')
#plt.savefig('exe3.png', bbox_inches='tight')