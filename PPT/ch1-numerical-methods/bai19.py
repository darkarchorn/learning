import math

def maclaurin_expx(x, terms):
    """Calculate e^x using Maclaurin series up to the specified number of terms."""
    result = sum((x**n) / math.factorial(n) for n in range(terms))
    return result

def maclaurin_expx_negative(x, terms):
    """Calculate e^-x using Maclaurin series up to the specified number of terms."""
    result = sum(((-x)**n) / math.factorial(n) for n in range(terms))
    return result

x = 1
num_terms = list(range(5, 11))

# Calculate e^x and e^-x for 5 to 10 terms
results_expx = [maclaurin_expx(x, n) for n in num_terms]
results_expx_negative = [maclaurin_expx_negative(x, n) for n in num_terms]

# Calculate 1/e by taking the reciprocal of e^x and using e^-x directly
results_reciprocal_expx = [1 / result for result in results_expx]

results = {
    "Terms": num_terms,
    "e^-x (partial sum)": results_expx_negative,
    "1/(e^x) (partial sum)": results_reciprocal_expx
}

import pandas as pd
df = pd.DataFrame(results)
print(df)

#Phương pháp sử dụng e^(-x) có vẻ chính xác hơn vì không yêu cầu nghịch đảo, tránh được sai số làm tròn bổ sung