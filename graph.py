import matplotlib.pyplot as plt

# Data for line 1
x1 = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]

# Data for line 2
x2 = [1, 2, 3, 4, 5]
y2 = [1, 3, 5, 7, 9]

# Data for line 3
x3 = [1, 2, 3, 4, 5]
y3 = [3, 6, 9, 12, 15]

# Plot all lines on the same graph
plt.plot(x1, y1, label='Line 1')
plt.plot(x2, y2, label='Line 2')
plt.plot(x3, y3, label='Line 3')

# Set the x and y axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Set the title of the graph
plt.title('Multiple Lines on the Same Graph')

# Add a legend to the graph
plt.legend()

# Show the graph
plt.show()
