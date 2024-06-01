import numpy as np

# Given data
x = np.array([0.0, 0.2, 0.4, 0.6, 0.8])
f = np.array([1.00000, 1.22140, 1.49182, 1.82212, 2.22554])
h = 0.2

# Forward difference table
n = len(f)
forward_diff = np.zeros((n, n))
forward_diff[:, 0] = f

for j in range(1, n):
    for i in range(n - j):
        forward_diff[i, j] = forward_diff[i + 1, j - 1] - forward_diff[i, j - 1]

# Backward difference table
backward_diff = np.zeros((n, n))
backward_diff[:, 0] = f

for j in range(1, n):
    for i in range(n - 1, j - 1, -1):
        backward_diff[i, j] = backward_diff[i, j - 1] - backward_diff[i - 1, j - 1]

# Part a: Newton forward-difference formula to approximate f(0.05)
x0 = x[0]
u = (0.05 - x0) / h
approx_forward = f[0]
factorial = 1

for j in range(1, n):
    factorial *= j
    term = forward_diff[0, j]
    for k in range(j):
        term *= (u - k)
    approx_forward += term / factorial

print(f"Approximation of f(0.05) using Newton forward-difference formula: {approx_forward}")

# Part b: Newton backward-difference formula to approximate f(0.65)
xn = x[-1]
u = (0.65 - xn) / h
approx_backward = f[-1]
factorial = 1

for j in range(1, n):
    factorial *= j
    term = backward_diff[-1, j]
    for k in range(j):
        term *= (u + k)
    approx_backward += term / factorial

print(f"Approximation of f(0.65) using Newton backward-difference formula: {approx_backward}")

# Part c: Stirling's formula to approximate f(0.43)
x_center = x[len(x) // 2]
u = (0.43 - x_center) / h
approx_stirling = f[n//2]
factorial = 1

for j in range(1, n//2 + 1):
    factorial *= j
    term = (forward_diff[(n//2) - j, 2*j - 1] + forward_diff[(n//2) - j + 1, 2*j - 1]) / 2
    for k in range(1, j):
        term *= (u**2 - (k - 1)**2)
    term *= u if j % 2 == 1 else 1
    approx_stirling += term / factorial

print(f"Approximation of f(0.43) using Stirling's formula: {approx_stirling}")
