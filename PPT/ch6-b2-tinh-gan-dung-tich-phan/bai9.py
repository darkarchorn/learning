import numpy as np

# Define the functions to integrate
def f1(x):
    return x**4

def f2(x):
    return 2 / (x - 4)

def f3(x):
    return x**2 * np.log(x)

def f4(x):
    return x**2 * np.exp(-x)

def f5(x):
    return 2 * x / (x**2 - 4)

def f6(x):
    return 2 / (x**2 - 4)

def f7(x):
    return x * np.sin(x)

def f8(x):
    return np.exp(x**3) * np.sin(2*x)

# Midpoint Rule implementation
def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    total = 0.0
    for i in range(n):
        mid_point = a + (i + 0.5) * h
        total += f(mid_point)
    return total * h

# Integration limits and number of subintervals
intervals = [
    (0.5, 1),      # for integral a
    (0, 0.5),      # for integral b
    (1, 1.5),      # for integral c
    (0, 1),        # for integral d
    (1, 1.6),      # for integral e
    (0, 0.35),     # for integral f
    (0, np.pi/4),  # for integral g
    (0, np.pi/4)   # for integral h
]
functions = [f1, f2, f3, f4, f5, f6, f7, f8]
n = 1000  # Number of subintervals

# Approximate the integrals using the Midpoint Rule
results = [midpoint_rule(func, a, b, n) for func, (a, b) in zip(functions, intervals)]

# Display the results
integrals = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for integral, result in zip(integrals, results):
    print(f"Approximation of integral {integral} using the Midpoint Rule: {result:.6f}")
