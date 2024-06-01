import math

def solve_quadratic_4s(a, b, c):
    delta = b ** 2 - 4 * a * c
    sqrt_delta = round(math.sqrt(delta), 4)  # 4 significant figures
    x1 = round((-b + sqrt_delta) / (2 * a), 4)
    x2 = round((-b - sqrt_delta) / (2 * a), 4)
    return x1, x2

def solve_quadratic_2s(a, b, c):
    delta = b ** 2 - 4 * a * c
    sqrt_delta = round(math.sqrt(delta), 2)  # 2 significant figures
    x1 = round((-b + sqrt_delta) / (2 * a), 2)
    x2 = round((-b - sqrt_delta) / (2 * a), 2)
    return x1, x2

# Solve the quadratic equation x^2 - 30x + 1 = 0
a = 1
b = -30
c = 1

x1_4s, x2_4s = solve_quadratic_4s(a, b, c)
x1_2s, x2_2s = solve_quadratic_2s(a, b, c)

print((x1_4s, x2_4s), (x1_2s, x2_2s))
