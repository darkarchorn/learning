import numpy as np

# Define the matrix A
A = np.array([
    [10, 1, 1],
    [1, 10, 1],
    [1, 1, 10]
], dtype=float)

# Norm (9): Maximum absolute column sum norm (L1 norm)
# This norm measures the maximum sum of absolute values of columns.
# It reflects how "spread out" the values are in the columns.
norm_1 = np.max(np.sum(np.abs(A), axis=0))

# Norm (10): Frobenius norm
# This norm measures the "energy" of the matrix, summing up the squares of all entries and taking the square root.
# It gives a sense of the overall magnitude of all entries combined.
norm_F = np.sqrt(np.sum(A**2))

# Norm (11): Maximum absolute row sum norm (L-infinity norm)
# This norm measures the maximum sum of absolute values of rows.
# It reflects how "spread out" the values are in the rows.
norm_inf = np.max(np.sum(np.abs(A), axis=1))

# Output the computed norms
print(f"Norm (9) - Maximum absolute column sum norm (L1 norm): {norm_1}")
print(f"Norm (10) - Frobenius norm: {norm_F}")
print(f"Norm (11) - Maximum absolute row sum norm (L-infinity norm): {norm_inf}")

# Explanation of differences:
# These norms can differ greatly based on the distribution of the matrix entries.
# If the matrix has a few large entries and many small ones, the Frobenius norm will be significantly influenced by the large entries.
# The L1 and L-infinity norms will be influenced by the maximum sums in their respective dimensions (columns and rows).
