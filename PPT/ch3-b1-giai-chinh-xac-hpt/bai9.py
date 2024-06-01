import sympy as sp
import numpy as np

# Define symbols
alpha, x1, x2 = sp.symbols('alpha x1 x2')

# Define the equations
eq1 = 2*x1 - 6*alpha*x2 - 3
eq2 = 3*alpha*x1 - x2 - sp.Rational(3, 2)

# Create the augmented matrix
aug_matrix = sp.Matrix([[2, -6*alpha, 3], [3*alpha, -1, sp.Rational(3, 2)]])

# Part a and b: Solving for alpha where determinant is zero and consistency
A = sp.Matrix([[2, -6*alpha], [3*alpha, -1]])
det_A = A.det()

alpha_values = sp.solve(det_A, alpha)
print(f"Values of alpha where det(A) = 0: {alpha_values}")

# Check consistency for these alpha values
for alpha_val in alpha_values:
    aug_matrix_sub = aug_matrix.subs(alpha, alpha_val)
    rank_A = A.subs(alpha, alpha_val).rank()
    rank_aug = aug_matrix_sub[:, :-1].rank()
    if rank_A == rank_aug:
        print(f"The system has infinite solutions for alpha = {alpha_val}")
    else:
        print(f"The system has no solutions for alpha = {alpha_val}")

# Part c: Assuming unique solution exists for alpha not in {1/3, -1/3}
alpha_val = 1  # Example value where alpha is not +/- 1/3
A_num = np.array([[2, -6*alpha_val], [3*alpha_val, -1]])
b_num = np.array([3, 1.5])

if np.linalg.det(A_num) != 0:
    solution = np.linalg.solve(A_num, b_num)
    print(f'Solution for alpha = {alpha_val}: {solution}')
else:
    print("The system does not have a unique solution for given alpha.")
