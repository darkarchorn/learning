import numpy as np

# Define the data for table a
x_a = np.array([2.1, 2.2, 2.3, 2.4, 2.5, 2.6])
f_a = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.7470223, -0.6015966])
h_a = x_a[1] - x_a[0]

# Compute derivatives using central difference for interior points and forward/backward for boundaries
f_prime_a = np.zeros_like(f_a)

# Forward difference for the first point
f_prime_a[0] = (f_a[1] - f_a[0]) / h_a

# Backward difference for the last point
f_prime_a[-1] = (f_a[-1] - f_a[-2]) / h_a

# Central difference for the interior points
for i in range(1, len(x_a) - 1):
    f_prime_a[i] = (f_a[i + 1] - f_a[i - 1]) / (2 * h_a)

# Define the data for table b
x_b = np.array([-3.0, -2.8, -2.6, -2.4, -2.2, -2.0])
f_b = np.array([9.367879, 8.233241, 7.180350, 6.209329, 5.320305, 4.513417])
h_b = x_b[1] - x_b[0]

# Compute derivatives using central difference for interior points and forward/backward for boundaries
f_prime_b = np.zeros_like(f_b)

# Forward difference for the first point
f_prime_b[0] = (f_b[1] - f_b[0]) / h_b

# Backward difference for the last point
f_prime_b[-1] = (f_b[-1] - f_b[-2]) / h_b

# Central difference for the interior points
for i in range(1, len(x_b) - 1):
    f_prime_b[i] = (f_b[i + 1] - f_b[i - 1]) / (2 * h_b)

# Display the results
print("Table a:")
for i in range(len(x_a)):
    print(f"x: {x_a[i]:.1f}, f(x): {f_a[i]:.6f}, f'(x): {f_prime_a[i]:.6f}")

print("\nTable b:")
for i in range(len(x_b)):
    print(f"x: {x_b[i]:.1f}, f(x): {f_b[i]:.6f}, f'(x): {f_prime_b[i]:.6f}")
