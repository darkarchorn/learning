import numpy as np

# Define the system of equations
def gauss_seidel(A, b, x0, num_iterations):
    n = len(b)
    x = x0.copy()
    
    for iteration in range(num_iterations):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x0[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        x0 = x.copy()
        print(f"Iteration {iteration + 1}: x = {x}")
    return x

# Coefficient matrix
A = np.array([
    [5, 1, 2],
    [1, 4, -2],
    [2, 3, 8]
], dtype=float)

# Right-hand side vector
b = np.array([19, -2, 39], dtype=float)

# Initial guess
x0 = np.array([1, 1, 1], dtype=float)

# Number of iterations
num_iterations = 5

# Perform Gauss-Seidel iteration
x = gauss_seidel(A, b, x0, num_iterations)
