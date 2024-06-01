import math
def sqrt2_convergence_c(x0, tol=1e-4, max_iter=1000):
    def g(x):
        return 0.5 * (x + 2/x)
    
    x_prev = x0
    for i in range(max_iter):
        x_next = g(x_prev)
        if abs(x_next - math.sqrt(2)) < tol:
            return x_next, i+1
        x_prev = x_next
    return x_next, max_iter

# Part (c)
sqrt2_approx_c, sqrt2_iters_c = sqrt2_convergence_c(0.5)
print(sqrt2_approx_c, sqrt2_iters_c)