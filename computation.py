import matplotlib.pyplot as plt

# Example data for energy consumption
ddlo_data = [50, 45, 48, 42, 47] # Distributed Deep Learning-based Offloading data
drl_data = [60, 57, 63, 61, 59] # Deep Reinforcement Learning data
x = [1, 2, 3, 4, 5] # x-axis values

# Create a figure and axis object
fig, ax = plt.subplots()

# Plot the data using a bar graph
ax.bar(x, ddlo_data, width=0.4, label='Distributed Deep Learning-based Offloading')
ax.bar([i + 0.4 for i in x], drl_data, width=0.4, label='Deep Reinforcement Learning')

# Add x-axis and y-axis labels
ax.set_xlabel('Experiment Number')
ax.set_ylabel('Energy Consumption (J)')

# Add a title and legend
ax.set_title('Distributed Deep Learning-based Offloading vs Deep Reinforcement Learning')
ax.legend()

# Show the plot
plt.show()
