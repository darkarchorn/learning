import numpy as np

def heun_method(f, y0, t0, t_end, h):
    t_values = np.arange(t0, t_end + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        y = y_values[i-1]
        k1 = f(t, y)
        k2 = f(t + h, y + h * k1)
        y_values[i] = y + (h / 2) * (k1 + k2)
    
    return t_values, y_values

# Các hàm f(t, y) cho các bài toán
def f_a(t, y):
    return np.exp(3*t) - 2*y

def f_b(t, y):
    return 1 + (t - y)**2

def f_c(t, y):
    return 1 + y/t

def f_d(t, y):
    return np.cos(2*t) + np.sin(3*t)

# Điều kiện ban đầu và bước nhảy h
y0_a, t0_a, t_end_a, h_a = 0, 0, 1, 0.5
y0_b, t0_b, t_end_b, h_b = 1, 2, 3, 0.5
y0_c, t0_c, t_end_c, h_c = 2, 1, 2, 0.25
y0_d, t0_d, t_end_d, h_d = 1, 0, 1, 0.25

# Giải phương trình sử dụng phương pháp Heun
t_values_a, y_values_a = heun_method(f_a, y0_a, t0_a, t_end_a, h_a)
t_values_b, y_values_b = heun_method(f_b, y0_b, t0_b, t_end_b, h_b)
t_values_c, y_values_c = heun_method(f_c, y0_c, t0_c, t_end_c, h_c)
t_values_d, y_values_d = heun_method(f_d, y0_d, t0_d, t_end_d, h_d)

# In kết quả
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

# Bài toán a
plt.subplot(2, 2, 1)
plt.plot(t_values_a, y_values_a, 'o-', label="Heun")
plt.plot(t_values_a, 1/5 * np.exp(3*t_values_a) - 1/25 * np.exp(-2*t_values_a), label="Actual")
plt.title('Problem a')
plt.legend()

# Bài toán b
plt.subplot(2, 2, 2)
plt.plot(t_values_b, y_values_b, 'o-', label="Heun")
plt.plot(t_values_b, t_values_b + 1/(1-t_values_b), label="Actual")
plt.title('Problem b')
plt.legend()

# Bài toán c
plt.subplot(2, 2, 3)
plt.plot(t_values_c, y_values_c, 'o-', label="Heun")
plt.plot(t_values_c, np.log(t_values_c) + 2*t_values_c, label="Actual")
plt.title('Problem c')
plt.legend()

# Bài toán d
plt.subplot(2, 2, 4)
plt.plot(t_values_d, y_values_d, 'o-', label="Heun")
plt.plot(t_values_d, 0.5*np.sin(2*t_values_d) - (1/3)*np.cos(3*t_values_d) + 4/3, label="Actual")
plt.title('Problem d')
plt.legend()

plt.tight_layout()
plt.show()
