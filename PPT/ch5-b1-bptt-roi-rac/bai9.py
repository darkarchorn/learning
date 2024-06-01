import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Combine the data into two lists
act_scores = np.array([28, 25, 28, 27, 28, 33, 28, 29, 23, 27, 29, 28, 27, 29, 21, 28, 28, 26, 30, 24])
gpa = np.array([3.84, 3.21, 3.23, 3.63, 3.75, 3.20, 3.41, 3.38, 3.53, 2.03, 3.75, 3.65, 3.87, 3.75, 1.66, 3.12, 2.96, 2.92, 3.10, 2.81])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(act_scores, gpa)

# Equation of the least squares line
def regression_line(x):
    return slope * x + intercept

# Plot the data points
plt.scatter(act_scores, gpa, color='blue', label='Data points')

# Plot the regression line
x_values = np.linspace(min(act_scores), max(act_scores), 100)
plt.plot(x_values, regression_line(x_values), color='red', label='Least squares line')

# Add labels and title
plt.xlabel('ACT Score')
plt.ylabel('Grade-point Average')
plt.title('ACT Score vs. Grade-point Average')
plt.legend()

# Display the plot
plt.show()

# Print the equation of the least squares line
print(f"The equation of the least squares line is: y = {slope:.4f}x + {intercept:.4f}")
