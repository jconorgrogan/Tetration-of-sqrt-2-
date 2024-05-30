import matplotlib.pyplot as plt
import numpy as np

# Initial value of sqrt(2)
sqrt_2 = np.sqrt(2)

# Compute 20 iterations of sqrt(2) taken to its own power recursively
lengths = [sqrt_2]
for _ in range(19):
    lengths.append(sqrt_2 ** lengths[-1])

# X coordinates for line starting points (all starting from x=0)
x_start = 0

# Y coordinates for each line (spacing them apart vertically)
y_positions = list(range(len(lengths)))

# Create a figure and axis for plotting
fig, ax = plt.subplots(figsize=(10, 12))

# Add lines to the plot
for i, length in enumerate(lengths):
    ax.plot([x_start, x_start + length], [y_positions[i]] * 2, marker='o')

# Setting graph title and labels
ax.set_title('Visualizing Lines of Increasing Powers of sqrt(2) Over 20 Iterations')
ax.set_ylabel('Iteration number')
ax.set_xlabel('Length in units')
ax.set_yticks(y_positions)
ax.set_ylim(-1, len(lengths))
ax.grid(True)

# Show the plot
plt.show()
