import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
k1 = 3
k2 = 0.002
k3 = 0.0006
k4 = 0.5

# Define the initial conditions
x1_0 = 1000
x2_0 = 500

# Define the time parameters
t0 = 0
t_end = 4
h = 0.01  # step size
t_values = np.arange(t0, t_end + h, h)

# Initialize arrays to store the results
x1_values = np.zeros(len(t_values))
x2_values = np.zeros(len(t_values))
x1_values[0] = x1_0
x2_values[0] = x2_0

# Define the system of differential equations
def dx1_dt(x1, x2):
    return k1 * x1 - k2 * x1 * x2

def dx2_dt(x1, x2):
    return k3 * x1 * x2 - k4 * x2

# Euler's method to solve the system of equations
for i in range(1, len(t_values)):
    x1 = x1_values[i - 1]
    x2 = x2_values[i - 1]
    
    x1_values[i] = x1 + h * dx1_dt(x1, x2)
    x2_values[i] = x2 + h * dx2_dt(x1, x2)

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t_values, x1_values, label='Prey Population (x1)', color='blue')
plt.plot(t_values, x2_values, label='Predator Population (x2)', color='red')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Population Dynamics of Prey and Predators')
plt.legend()
plt.grid(True)
plt.show()

# Stability analysis
# Find the equilibrium points
equilibrium_x1 = k4 / k3
equilibrium_x2 = k1 / k2

print(f"Equilibrium points: x1 = {equilibrium_x1}, x2 = {equilibrium_x2}")

# Stability of equilibrium points
# If both x1 and x2 are positive at equilibrium, the solution is stable.
if equilibrium_x1 > 0 and equilibrium_x2 > 0:
    print("The solution is stable.")
else:
    print("The solution is not stable.")
