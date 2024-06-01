import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f1(x):
    return np.exp(x) - 2

def f2(x):
    return np.cos(np.exp(x) - 2)

# Generate x values
x = np.linspace(0.5, 1.5, 400)

# Generate y values
y1 = f1(x)
y2 = f2(x)

# Plot the functions
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = e^x - 2')
plt.plot(x, y2, label='y = cos(e^x - 2)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of y = e^x - 2 and y = cos(e^x - 2)')
plt.legend()
plt.grid(True)
plt.show()
