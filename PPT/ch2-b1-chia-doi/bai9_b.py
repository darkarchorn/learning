import numpy as np

# Define the function for which we need to find the root
def f(x):
    return np.exp(x) - 2 - np.cos(np.exp(x) - 2)

# Bisection method implementation
def bisection_method(a, b, tol=1e-5, max_iter=100):
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

# Finding the root
a = 0.5
b = 1.5
root = bisection_method(a, b)
print(root)
