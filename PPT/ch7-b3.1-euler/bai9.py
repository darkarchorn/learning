import numpy as np
from scipy.interpolate import interp1d

# Define the differential equation
def f(t, y):
    return (2/t) - y + t**2 * np.exp(t)

# Exact solution
def y_exact(t):
    return t**2 * (np.exp(t) - np.exp(1))

# Euler's method
def euler_method(f, y0, t0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros_like(t_values)
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]
        y_values[i] = y + h * f(t, y)
    
    return t_values, y_values

# Initial conditions
t0 = 1
y0 = 0
h = 0.1
t_end = 2

# Part a: Euler's method with h = 0.1
t_values, y_values = euler_method(f, y0, t0, t_end, h)

# Part b: Linear interpolation for specified points
interp_points = [1.04, 1.55, 1.97]
linear_interp = interp1d(t_values, y_values)
interp_values = linear_interp(interp_points)

# Exact values for comparison
exact_values = [y_exact(t) for t in interp_points]

# Part c: Compute the necessary step size h
# Use the formula for the local truncation error to estimate h

# Display results
print("Part a: Euler's method with h = 0.1")
for t_val, y_approx in zip(t_values, y_values):
    print(f"t = {t_val:.2f}, y_approx = {y_approx:.6f}, y_exact = {y_exact(t_val):.6f}")

print("\nPart b: Linear interpolation")
for t_val, y_interp, y_exact_val in zip(interp_points, interp_values, exact_values):
    print(f"t = {t_val:.2f}, y_approx = {y_interp:.6f}, y_exact = {y_exact_val:.6f}")

# Error calculation to determine h
def compute_h(f, y0, t0, t_end, error_threshold):
    h = 0.1
    while True:
        t_values, y_values = euler_method(f, y0, t0, t_end, h)
        max_error = max(abs(y_exact(t) - y) for t, y in zip(t_values, y_values))
        if max_error <= error_threshold:
            break
        h /= 2
    return h

error_threshold = 0.1
necessary_h = compute_h(f, y0, t0, t_end, error_threshold)

print(f"\nPart c: Necessary step size h for error <= 0.1: {necessary_h:.6f}")
