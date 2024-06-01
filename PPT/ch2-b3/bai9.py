import sympy as sp
import numpy as np
import pandas as pd

# Defining the functions and their derivatives for Newton's Method
x = sp.symbols('x')
functions = [
    x**3 - 2*x**2 - 5,   # for part a
    x**3 + 3*x**2 - 1,   # for part b
    x - sp.cos(x),       # for part c
    x - 0.8 - 0.2*sp.sin(x)  # for part d
]

# Derivatives of the functions
derivatives = [sp.diff(f, x) for f in functions]

# Converting sympy functions to numpy functions
f_lambdas = [sp.lambdify(x, f, 'numpy') for f in functions]
f_prime_lambdas = [sp.lambdify(x, df, 'numpy') for df in derivatives]

# Defining the intervals for each part
intervals = [
    (1, 4),        # for part a
    (-3, -2),      # for part b
    (0, np.pi/2),  # for part c
    (0, np.pi/2)   # for part d
]

# Newton's Method Implementation
def newton_method(f, f_prime, x0, tol=1e-4, max_iter=100):
    for _ in range(max_iter):
        x1 = x0 - f(x0) / f_prime(x0)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

# False Position Method Implementation
def false_position_method(f, a, b, tol=1e-4, max_iter=100):
    for _ in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        if abs(f(c)) < tol:
            return c
    return c

# Applying Newton's Method
newton_solutions = [newton_method(f_lambdas[i], f_prime_lambdas[i], sum(interval)/2) for i, interval in enumerate(intervals)]

# Applying False Position Method
false_position_solutions = [false_position_method(f_lambdas[i], *interval) for i, interval in enumerate(intervals)]

# Combining the results
results = {
    'Method': ['Newton', 'False Position'],
    'a': [newton_solutions[0], false_position_solutions[0]],
    'b': [newton_solutions[1], false_position_solutions[1]],
    'c': [newton_solutions[2], false_position_solutions[2]],
    'd': [newton_solutions[3], false_position_solutions[3]]
}

df_results = pd.DataFrame(results)
print(df_results)
