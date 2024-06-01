import numpy as np
from scipy.linalg import lu

# Define the matrix A and vector b
A = np.array([
    [0.01, 0, 0.03],
    [0, 0.16, 0.08],
    [0.03, 0.08, 0.14]
])

b = np.array([0.14, 0.16, 0.54])

# Perform LU decomposition
P, L, U = lu(A)

print("L matrix:")
print(L)
print("U matrix:")
print(U)

# Solve the system using LU decomposition
# Forward substitution to solve L * y = b
y = np.linalg.solve(L, np.dot(P, b))

# Backward substitution to solve U * x = y
x = np.linalg.solve(U, y)

print("Solution x:")
print(x)
