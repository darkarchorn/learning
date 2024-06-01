import numpy as np

def heuns_method(f, y0, t0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]
        
        k1 = f(t, y)
        y_predict = y + h * k1
        k2 = f(t + h, y_predict)
        
        y_values[i] = y + (h / 2) * (k1 + k2)
    
    return t_values, y_values

# Define the differential equations and exact solutions
def f_a(t, y):
    return t * np.exp(t) - 2 * y

def y_exact_a(t):
    return (1/5) * (t**2 * np.exp(t)) - (1/25) * (np.exp(t)) + (1/25) * np.exp(2 * t)

def f_b(t, y):
    return 1 + (t - y)**2

def y_exact_b(t):
    return t + 1/(t - 1)

def f_c(t, y):
    return 1 + y / t

def y_exact_c(t):
    return np.log(t) + 2 * t

def f_d(t, y):
    return np.cos(2 * t) + np.sin(3 * t)

def y_exact_d(t):
    return (1/2) * np.sin(2 * t) - (1/3) * np.cos(3 * t) + (1/2) * np.cos(2 * t) + (1/3) * np.cos(3 * t) + 4/3

# Problem a
t0_a, y0_a, t_end_a, h_a = 0, 0, 1, 0.5
t_values_a, y_values_a = heuns_method(f_a, y0_a, t0_a, t_end_a, h_a)

# Problem b
t0_b, y0_b, t_end_b, h_b = 2, 1, 3, 0.5
t_values_b, y_values_b = heuns_method(f_b, y0_b, t0_b, t_end_b, h_b)

# Problem c
t0_c, y0_c, t_end_c, h_c = 1, 2, 2, 0.25
t_values_c, y_values_c = heuns_method(f_c, y0_c, t0_c, t_end_c, h_c)

# Problem d
t0_d, y0_d, t_end_d, h_d = 0, 1, 1, 0.25
t_values_d, y_values_d = heuns_method(f_d, y0_d, t0_d, t_end_d, h_d)

# Exact solutions
exact_values_a = [y_exact_a(t) for t in t_values_a]
exact_values_b = [y_exact_b(t) for t in t_values_b]
exact_values_c = [y_exact_c(t) for t in t_values_c]
exact_values_d = [y_exact_d(t) for t in t_values_d]

# Display results
print("Problem a: Heun's method")
for t, y_num, y_ex in zip(t_values_a, y_values_a, exact_values_a):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")

print("\nProblem b: Heun's method")
for t, y_num, y_ex in zip(t_values_b, y_values_b, exact_values_b):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")

print("\nProblem c: Heun's method")
for t, y_num, y_ex in zip(t_values_c, y_values_c, exact_values_c):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")

print("\nProblem d: Heun's method")
for t, y_num, y_ex in zip(t_values_d, y_values_d, exact_values_d):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")
