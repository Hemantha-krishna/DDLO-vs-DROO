import numpy as np
import matplotlib.pyplot as plt

# Load data from first text file
data1 = np.loadtxt('dataddlo.txt', delimiter='\t', skiprows=1)

# Load data from second text file
data2 = np.loadtxt('datadroo.txt', delimiter='\t', skiprows=1)

# Plot data from both files
plt.plot(data1[:,0], data1[:,1], label='DDLO')
plt.plot(data2[:,0], data2[:,1], label='DROO')
plt.xlabel('Time Frames')
plt.ylabel('Training Loss')
plt.title('Training loss of DDLO and DROO')
plt.legend()

# Show the plot
plt.show()
