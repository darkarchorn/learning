import numpy as np

# Given values
L = 10
r = 1
V = 12.4

# Define the volume function
def volume(h):
    term1 = 0.5 * np.pi * r**2
    term2 = r**2 * np.arcsin(h / r)
    term3 = h * np.sqrt(r**2 - h**2)
    return L * (term1 - term2 - term3)

# Define the function for bisection method
def f(h):
    return volume(h) - V

# Bisection method implementation
def bisection_method(a, b, tol=0.01, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1, max_iter + 1):
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        if np.abs(f_m_n) < tol:
            return m_n
        elif f(a_n) * f_m_n < 0:
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n) / 2

# Finding the depth
a = 0
b = 1
depth = bisection_method(a, b)
print(depth)
