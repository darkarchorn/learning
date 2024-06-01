import numpy as np
import sympy as sp

# Define the data points for both samples
days = np.array([0, 6, 10, 13, 17, 20, 28])
weights_sample1 = np.array([6.67, 17.33, 42.67, 37.33, 30.10, 29.31, 28.74])
weights_sample2 = np.array([6.67, 16.11, 18.89, 15.00, 10.56, 9.44, 8.89])

# Define the variable
x = sp.symbols('x')

# Function to construct Lagrange interpolating polynomial
def lagrange_interpolating_polynomial(x, x_points, y_points):
    n = len(x_points)
    L = 0
    for i in range(n):
        li = 1
        for j in range(n):
            if i != j:
                li *= (x - x_points[j]) / (x_points[i] - x_points[j])
        L += y_points[i] * li
    return sp.simplify(L)

# Construct the polynomials for both samples
P1 = lagrange_interpolating_polynomial(x, days, weights_sample1)
P2 = lagrange_interpolating_polynomial(x, days, weights_sample2)

# Display the polynomials
print("Lagrange Interpolating Polynomial for Sample 1:")
sp.pretty_print(P1)

print("\nLagrange Interpolating Polynomial for Sample 2:")
sp.pretty_print(P2)

# Find the approximate maximum average weight for each sample
P1_diff = sp.diff(P1, x)
P2_diff = sp.diff(P2, x)

# Find the critical points by solving P'(x) = 0
critical_points_sample1 = sp.solve(P1_diff, x)
critical_points_sample2 = sp.solve(P2_diff, x)

# Evaluate the polynomial at the critical points to find the maximum average weight
max_weight_sample1 = max([P1.evalf(subs={x: cp}) for cp in critical_points_sample1])
max_weight_sample2 = max([P2.evalf(subs={x: cp}) for cp in critical_points_sample2])

print(f"\nApproximate maximum average weight for Sample 1: {max_weight_sample1} mg")
print(f"Approximate maximum average weight for Sample 2: {max_weight_sample2} mg")
