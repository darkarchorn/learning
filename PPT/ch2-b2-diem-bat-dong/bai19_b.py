import math

def sqrt2_convergence_b(x0, tol=1e-4, max_iter=1000):
    def g(x):
        return 0.5 * (x + 2/x)
    
    x_prev = x0
    for i in range(max_iter):
        x_next = g(x_prev)
        if 0 < x_next - math.sqrt(2)**2 < tol:
            return x_next, i+1
        x_prev = x_next
    return x_next, max_iter

# Part (b)
sqrt2_approx_b, sqrt2_iters_b = sqrt2_convergence_b(1)
print(sqrt2_approx_b, sqrt2_iters_b)