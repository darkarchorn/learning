import numpy as np
import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the functions
phi_0 = sp.sympify(1)
phi_1 = x
phi_2 = x**2
phi_3 = x**3

# List of functions
functions = [phi_0, phi_1, phi_2, phi_3]

# Gram-Schmidt Process to orthogonalize the functions
def gram_schmidt(functions, x, interval):
    orthogonal_functions = []
    for i in range(len(functions)):
        # Start with the current function
        fi = functions[i]
        # Subtract the projection onto each of the previous orthogonal functions
        for j in range(i):
            fj = orthogonal_functions[j]
            # Compute the inner product <fi, fj>
            inner_product_fi_fj = sp.integrate(fi * fj, (x, interval[0], interval[1]))
            # Compute the inner product <fj, fj>
            inner_product_fj_fj = sp.integrate(fj * fj, (x, interval[0], interval[1]))
            # Subtract the projection
            fi = fi - (inner_product_fi_fj / inner_product_fj_fj) * fj
        # Add the orthogonalized function to the list
        orthogonal_functions.append(fi)
    return orthogonal_functions

# Define the interval
interval = [0, 1]

# Apply Gram-Schmidt Process
orthogonal_functions = gram_schmidt(functions, x, interval)

# Normalize the orthogonal functions
normalized_functions = [fi / sp.sqrt(sp.integrate(fi * fi, (x, interval[0], interval[1]))) for fi in orthogonal_functions]

# Define the target function (example f(x) = e^x, can be replaced with any target function)
f = sp.exp(x)

# Compute the coefficients for the least squares polynomial
coefficients = [sp.integrate(f * fi, (x, interval[0], interval[1])) for fi in normalized_functions]

# Construct the least squares polynomial
least_squares_poly = sum(c * fi for c, fi in zip(coefficients, normalized_functions))

print(f"Least squares polynomial of degree 3 for f(x) = e^x on [0, 1]: {sp.simplify(least_squares_poly)}")
