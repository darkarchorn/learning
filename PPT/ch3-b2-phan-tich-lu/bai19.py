import numpy as np

# Define the matrix A
A = np.array([
    [4, 2, 4, 0],
    [2, 2, 3, 2],
    [4, 3, 6, 3],
    [0, 2, 3, 9]
], dtype=float)

# Create an augmented matrix [A | I]
n = A.shape[0]
I = np.eye(n)
AI = np.hstack((A, I))

# Perform Gauss-Jordan elimination
for i in range(n):
    # Make the diagonal contain all 1's
    AI[i] = AI[i] / AI[i, i]
    # Make the other rows contain 0's
    for j in range(n):
        if i != j:
            AI[j] = AI[j] - AI[j, i] * AI[i]

# Extract the inverse matrix
A_inv = AI[:, n:]

print("Inverse of A:")
print(A_inv)
