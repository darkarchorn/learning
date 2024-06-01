import numpy as np

# Function definition
def f(x):
    return x**3 - 2*x**2 - 5  # Example function

# Secant Method Implementation
def secant_method(f, p0, p1, tol=1e-4, max_iter=100):
    for _ in range(max_iter):
        if abs(f(p1) - f(p0)) < tol:
            return p1
        p2 = (f(p1) * p0 - f(p0) * p1) / (f(p1) - f(p0))
        if abs(p2 - p1) < tol:
            return p2
        p0, p1 = p1, p2
    return p1

# Newton's Method Implementation for comparison
def newton_method(f, f_prime, x0, tol=1e-4, max_iter=100):
    for _ in range(max_iter):
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

# Derivative of the function for Newton's Method
def f_prime(x):
    return 3*x**2 - 4*x

# Initial guesses
p0, p1 = 1, 4
x0 = (p0 + p1) / 2

# Solve using Secant Method
secant_solution = secant_method(f, p0, p1)
print(f'Secant Method Solution: {secant_solution}')

# Solve using Newton's Method
newton_solution = newton_method(f, f_prime, x0)
print(f'Newton\'s Method Solution: {newton_solution}')

# The Secant Method can be less accurate than Newton's Method because it uses an approximation of the derivative
# (difference between function values at two points) instead of the exact derivative. This approximation can lead 
# to larger errors, especially if the function is highly nonlinear or if the initial guesses are not close to the 
# actual root. Newton's Method, on the other hand, uses the exact derivative, providing a more accurate and often faster convergence to the root.