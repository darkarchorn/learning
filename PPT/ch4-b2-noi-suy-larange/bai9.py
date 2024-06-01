import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the data points
x0, y0 = 0, 0
x1, y1 = 0.5, sp.Symbol('y')
x2, y2 = 1, 3
x3, y3 = 2, 2

# Define the Lagrange basis polynomials
def lagrange_basis(x, xi, xj):
    return sp.prod([(x - xj_k)/(xi - xj_k) for xj_k in xj])

# Lagrange basis polynomials
x_points = [x0, x1, x2, x3]
l0 = lagrange_basis(x, x0, [x1, x2, x3])
l1 = lagrange_basis(x, x1, [x0, x2, x3])
l2 = lagrange_basis(x, x2, [x0, x1, x3])
l3 = lagrange_basis(x, x3, [x0, x1, x2])

# Construct the interpolating polynomial
P3 = y0*l0 + y1*l1 + y2*l2 + y3*l3

# Extract the coefficient of x^3
coeff_x3 = sp.expand(P3).coeff(x**3)
print(f"Coefficient of x^3: {coeff_x3}")

# Solve for y such that the coefficient of x^3 is 6
solution = sp.solve(coeff_x3 - 6, y1)
print(f"Value of y: {solution}")
