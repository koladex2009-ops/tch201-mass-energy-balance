import numpy as np;

def column_balance(F, F_m, D_m, B_m): 
    coeffs = np.array([[1, 1],
                       [D_m, B_m]])
    constants = np.array([F, F_m*F]);
    D, B = np.linalg.solve(coeffs, constants);
    return D, B;

D, B = column_balance(2000, 0.40, 0.90, 0.05)
print("D =", D, " B =", B)
print(np.isclose(0.40 * 2000, 0.90 * D + 0.05 * B))