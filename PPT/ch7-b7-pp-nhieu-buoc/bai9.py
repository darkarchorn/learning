import numpy as np
import matplotlib.pyplot as plt

# Given values
h = 0.01
t_values = np.arange(0, 0.21, h)
n = len(t_values)

# Exact solution with safe computation
def exact_solution(t):
    if np.exp(t) >= 1:
        return float('inf')  # Return infinity if the value exceeds the domain of the log
    return 1 - np.log(1 - np.exp(t))

# Function for g(w)
def g(w, w_i, w_i_minus_1, w_i_minus_2, t):
    return w_i + (h/24) * (9 * np.exp(t) + 19 * np.exp(w) - 5 * np.exp(w_i_minus_1) + np.exp(w_i_minus_2))

# Initial values (exact values)
w = np.zeros(n)
w[0] = exact_solution(t_values[0])
w[1] = exact_solution(t_values[1])
w[2] = exact_solution(t_values[2])

# Functional iteration
for i in range(2, n-1):
    w[i+1] = g(w[i], w[i], w[i-1], w[i-2], t_values[i])

# Plotting results
plt.plot(t_values, [exact_solution(t) for t in t_values], label='Exact Solution')
plt.plot(t_values, w, 'o-', label='Adams-Moulton Method')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title('Adams-Moulton Method for Initial-Value Problem')
plt.grid(True)
plt.show()

# Newton's Method - Part b
def newton_method(w_initial, w_i, w_i_minus_1, w_i_minus_2, t):
    tol = 1e-10
    max_iter = 1000
    w_new = w_initial
    for _ in range(max_iter):
        f_value = w_new - g(w_new, w_i, w_i_minus_1, w_i_minus_2, t)
        f_deriv = 1 - (h/24) * 19 * np.exp(w_new)
        w_next = w_new - f_value / f_deriv
        if abs(w_next - w_new) < tol:
            break
        w_new = w_next
    return w_new

# Applying Newton's method
w_newton = np.zeros(n)
w_newton[0] = exact_solution(t_values[0])
w_newton[1] = exact_solution(t_values[1])
w_newton[2] = exact_solution(t_values[2])

for i in range(2, n-1):
    w_newton[i+1] = newton_method(w[i], w[i], w[i-1], w[i-2], t_values[i])

# Plotting Newton's Method results
plt.plot(t_values, [exact_solution(t) for t in t_values], label='Exact Solution')
plt.plot(t_values, w_newton, 'o-', label="Newton's Method")
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.title("Newton's Method for Initial-Value Problem")
plt.grid(True)
plt.show()
