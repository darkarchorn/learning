import numpy as np
from scipy.interpolate import interp1d

def midpoint_method(f, y0, t0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]
        
        k1 = f(t, y)
        y_mid = y + (h / 2) * k1
        t_mid = t + (h / 2)
        k2 = f(t_mid, y_mid)
        
        y_values[i] = y + h * k2
    
    return t_values, y_values

# Define the differential equations and exact solutions
def f_a(t, y):
    return y/t - (y/t)**2

def y_exact_a(t):
    return t / (1 + np.log(t))

def f_b(t, y):
    return 1 + y/t + (y/t)**2

def y_exact_b(t):
    return t * np.tan(np.log(t))

def f_c(t, y):
    return -y + t * (y + 3)

def y_exact_c(t):
    return -3 + 2 * (1 + np.exp(t**2 - 1))

def f_d(t, y):
    return -5*y + 5*t**2 + 2*t

def y_exact_d(t):
    return t**2 + t - 1/3 * np.exp(-5*t)

# Problem a
t0_a, y0_a, t_end_a, h_a = 1, 1, 2, 0.1
t_values_a, y_values_a = midpoint_method(f_a, y0_a, t0_a, t_end_a, h_a)

# Problem b
t0_b, y0_b, t_end_b, h_b = 1, 0, 3, 0.2
t_values_b, y_values_b = midpoint_method(f_b, y0_b, t0_b, t_end_b, h_b)

# Problem c
t0_c, y0_c, t_end_c, h_c = 0, -2, 2, 0.2
t_values_c, y_values_c = midpoint_method(f_c, y0_c, t0_c, t_end_c, h_c)

# Problem d
t0_d, y0_d, t_end_d, h_d = 0, 1/3, 1, 0.1
t_values_d, y_values_d = midpoint_method(f_d, y0_d, t0_d, t_end_d, h_d)

# Exact solutions
exact_values_a = [y_exact_a(t) for t in t_values_a]
exact_values_b = [y_exact_b(t) for t in t_values_b]
exact_values_c = [y_exact_c(t) for t in t_values_c]
exact_values_d = [y_exact_d(t) for t in t_values_d]

# Display results
print("Problem a: Midpoint method")
for t, y_num, y_ex in zip(t_values_a, y_values_a, exact_values_a):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")

print("\nProblem b: Midpoint method")
for t, y_num, y_ex in zip(t_values_b, y_values_b, exact_values_b):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")

print("\nProblem c: Midpoint method")
for t, y_num, y_ex in zip(t_values_c, y_values_c, exact_values_c):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")

print("\nProblem d: Midpoint method")
for t, y_num, y_ex in zip(t_values_d, y_values_d, exact_values_d):
    print(f"t = {t:.2f}, y_approx = {y_num:.6f}, y_exact = {y_ex:.6f}")

# Interpolation
def interpolate(t_values, y_values, points):
    linear_interp = interp1d(t_values, y_values, kind='linear')
    interp_values = linear_interp(points)
    return interp_values

# Interpolation points for Problem a
interp_points_a = [1.25, 1.93]
interp_values_a = interpolate(t_values_a, y_values_a, interp_points_a)
exact_interp_a = [y_exact_a(t) for t in interp_points_a]

# Interpolation points for Problem b
interp_points_b = [2.1, 2.75]
interp_values_b = interpolate(t_values_b, y_values_b, interp_points_b)
exact_interp_b = [y_exact_b(t) for t in interp_points_b]

# Interpolation points for Problem c
interp_points_c = [1.3, 1.93]
interp_values_c = interpolate(t_values_c, y_values_c, interp_points_c)
exact_interp_c = [y_exact_c(t) for t in interp_points_c]

# Interpolation points for Problem d
interp_points_d = [0.54, 0.94]
interp_values_d = interpolate(t_values_d, y_values_d, interp_points_d)
exact_interp_d = [y_exact_d(t) for t in interp_points_d]

# Display interpolation results
print("\nInterpolation results for Problem a:")
for t, y_interp, y_exact in zip(interp_points_a, interp_values_a, exact_interp_a):
    print(f"t = {t:.2f}, y_approx = {y_interp:.6f}, y_exact = {y_exact:.6f}")

print("\nInterpolation results for Problem b:")
for t, y_interp, y_exact in zip(interp_points_b, interp_values_b, exact_interp_b):
    print(f"t = {t:.2f}, y_approx = {y_interp:.6f}, y_exact = {y_exact:.6f}")

print("\nInterpolation results for Problem c:")
for t, y_interp, y_exact in zip(interp_points_c, interp_values_c, exact_interp_c):
    print(f"t = {t:.2f}, y_approx = {y_interp:.6f}, y_exact = {y_exact:.6f}")

print("\nInterpolation results for Problem d:")
for t, y_interp, y_exact in zip(interp_points_d, interp_values_d, exact_interp_d):
    print(f"t = {t:.2f}, y_approx = {y_interp:.6f}, y_exact = {y_exact:.6f}")
