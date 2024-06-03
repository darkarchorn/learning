import numpy as np
import matplotlib.pyplot as plt

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

def interpolate(t_values, y_values, t):
    for i in range(len(t_values) - 1):
        if t_values[i] <= t <= t_values[i + 1]:
            t0, y0 = t_values[i], y_values[i]
            t1, y1 = t_values[i + 1], y_values[i + 1]
            return y0 + (y1 - y0) * (t - t0) / (t1 - t0)
    return None

# Các hàm f(t, y) cho các bài toán trong Bài tập 7
def f_a(t, y):
    return y/t - (y/t)**2

def f_b(t, y):
    return 1 + y/t + (y/t)**2

def f_c(t, y):
    return -(y + 1)*(y + 3)

def f_d(t, y):
    return -5*y + 5*t**2 + 2*t

# Điều kiện ban đầu và bước nhảy h
y0_a, t0_a, t_end_a, h_a = 1, 1, 2, 0.1
y0_b, t0_b, t_end_b, h_b = 0, 1, 3, 0.2
y0_c, t0_c, t_end_c, h_c = -2, 0, 2, 0.2
y0_d, t0_d, t_end_d, h_d = 1/3, 0, 1, 0.1

# Giải phương trình sử dụng phương pháp Heun
t_values_a, y_values_a = heun_method(f_a, y0_a, t0_a, t_end_a, h_a)
t_values_b, y_values_b = heun_method(f_b, y0_b, t0_b, t_end_b, h_b)
t_values_c, y_values_c = heun_method(f_c, y0_c, t0_c, t_end_c, h_c)
t_values_d, y_values_d = heun_method(f_d, y0_d, t0_d, t_end_d, h_d)

# Ước lượng giá trị y(t) tại các điểm cụ thể bằng nội suy tuyến tính
t_estimates = [1.25, 1.93]
y_estimates_a = [interpolate(t_values_a, y_values_a, t) for t in t_estimates]
y_estimates_b = [interpolate(t_values_b, y_values_b, t) for t in t_estimates]

# In kết quả
print("Problem a:")
for t, y in zip(t_estimates, y_estimates_a):
    print(f"y({t}) ≈ {y}")

print("\nProblem b:")
for t, y in zip(t_estimates, y_estimates_b):
    print(f"y({t}) ≈ {y}")

# Vẽ biểu đồ kết quả
plt.figure(figsize=(10, 8))

# Bài toán a
plt.subplot(2, 1, 1)
plt.plot(t_values_a, y_values_a, 'o-', label="Heun")
plt.title('Problem a')
plt.legend()

# Bài toán b
plt.subplot(2, 1, 2)
plt.plot(t_values_b, y_values_b, 'o-', label="Heun")
plt.title('Problem b')
plt.legend()

plt.tight_layout()
plt.show()
