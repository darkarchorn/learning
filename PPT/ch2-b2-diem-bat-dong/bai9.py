def fixed_point_iteration(g, x0, tol=1e-4, max_iter=1000):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, i+1
        x = x_new
    raise ValueError("Did not converge")

# Hàm lặp cố định g(x) = (x + 3/x)/2
g = lambda x: (x + 3/x) / 2

# Giá trị ban đầu
x0 = 1.5

# Gọi hàm để tìm giá trị gần đúng
approx_root, iterations = fixed_point_iteration(g, x0)

print(approx_root, iterations)
