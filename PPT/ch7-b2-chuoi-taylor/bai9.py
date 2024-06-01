import numpy as np
import sympy as sp
from scipy.interpolate import interp1d, CubicHermiteSpline

# Define the variables
t = sp.symbols('t')
y = sp.Function('y')(t)

# Given differential equation
f = (2/t) - y + t**2 * sp.exp(t)
f_prime = sp.diff(f, t) + sp.diff(f, y) * f
f_double_prime = sp.diff(f_prime, t) + sp.diff(f_prime, y) * f
f_triple_prime = sp.diff(f_double_prime, t) + sp.diff(f_double_prime, y) * f

# Exact solution
y_exact = t**2 * (sp.exp(t) - sp.exp(1))

# Convert exact solution to a numerical function
y_exact_func = sp.lambdify(t, y_exact, 'numpy')

# Initial conditions and parameters
t0 = 1
y0 = 0
h = 0.1
N = int((2 - 1) / h)  # Number of steps

# Arrays to store results
t_values = np.arange(t0, 2 + h, h)
y_taylor2 = np.zeros(len(t_values))
y_taylor2[0] = y0

# Taylor's method of order two
for i in range(1, len(t_values)):
    t_n = t_values[i-1]
    y_n = y_taylor2[i-1]
    f_n = (2/t_n) - y_n + t_n**2 * np.exp(t_n)
    f_prime_n = (2/t_n**2) + t_n**2 * np.exp(t_n) - 1 - f_n
    y_taylor2[i] = y_n + h * f_n + (h**2 / 2) * f_prime_n

# Linear interpolation for part b
linear_interp = interp1d(t_values, y_taylor2, kind='linear')

# Taylor's method of order four
y_taylor4 = np.zeros(len(t_values))
y_taylor4[0] = y0

for i in range(1, len(t_values)):
    t_n = t_values[i-1]
    y_n = y_taylor4[i-1]
    f_n = (2/t_n) - y_n + t_n**2 * np.exp(t_n)
    f_prime_n = (2/t_n**2) + t_n**2 * np.exp(t_n) - 1 - f_n
    f_double_prime_n = (4/t_n**3) + t_n**2 * np.exp(t_n) - f_prime_n
    f_triple_prime_n = (8/t_n**4) + t_n**2 * np.exp(t_n) - f_double_prime_n
    y_taylor4[i] = y_n + h * f_n + (h**2 / 2) * f_prime_n + (h**3 / 6) * f_double_prime_n + (h**4 / 24) * f_triple_prime_n

# Cubic Hermite interpolation for part d
cubic_interp = CubicHermiteSpline(t_values, y_taylor4, np.gradient(y_taylor4, h))

# Points to interpolate
interp_points = [1.04, 1.55, 1.97]

# Compute exact values at the interpolation points
exact_values = y_exact_func(np.array(interp_points))

# Interpolated values
linear_interp_values = linear_interp(interp_points)
cubic_interp_values = cubic_interp(interp_points)

# Display results
print("Part a: Taylor's method of order two with h = 0.1")
for i, t_val in enumerate(t_values):
    print(f"t = {t_val:.2f}, y_approx = {y_taylor2[i]:.6f}, y_exact = {y_exact_func(t_val):.6f}")

print("\nPart b: Linear interpolation")
for t_val, y_interp, y_exact in zip(interp_points, linear_interp_values, exact_values):
    print(f"t = {t_val:.2f}, y_approx = {y_interp:.6f}, y_exact = {y_exact:.6f}")

print("\nPart c: Taylor's method of order four with h = 0.1")
for i, t_val in enumerate(t_values):
    print(f"t = {t_val:.2f}, y_approx = {y_taylor4[i]:.6f}, y_exact = {y_exact_func(t_val):.6f}")

print("\nPart d: Cubic Hermite interpolation")
for t_val, y_interp, y_exact in zip(interp_points, cubic_interp_values, exact_values):
    print(f"t = {t_val:.2f}, y_approx = {y_interp:.6f}, y_exact = {y_exact:.6f}")
