import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the function
x = sp.symbols('x')
f = 3**(x+1) - 7 * 5**(2*x)

# Solve symbolically
symbolic_solution = sp.solve(f, x)
print(f'Symbolic Solutions: {symbolic_solution}')

# Convert to numpy function for plotting
f_lambdified = sp.lambdify(x, f, 'numpy')

# Define the range for x
x_vals = np.linspace(-3, 3, 400)
y_vals = f_lambdified(x_vals)

# Plot the function
plt.plot(x_vals, y_vals)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title('Plot of f(x) = $3^{x+1} - 7 \cdot 5^{2x}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

# Define the derivative of the function
f_prime = sp.diff(f, x)
f_prime_lambdified = sp.lambdify(x, f_prime, 'numpy')

# Newton's Method Implementation
def newton_method(f, f_prime, x0, tol=1e-16, max_iter=100):
    for _ in range(max_iter):
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

# Initial guess from the plot
initial_guesses = [-2, 0, 2]

# Applying Newton's Method
newton_solutions = [newton_method(f_lambdified, f_prime_lambdified, x0) for x0 in initial_guesses]
print(f'Newton\'s Method Solutions: {newton_solutions}')

# Exact Solutions using sympy
exact_solutions = sp.solve(f, x)
print(f'Exact Solutions: {exact_solutions}')
