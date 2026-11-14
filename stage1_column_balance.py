import numpy as np

# Testing...

A = np.array([[1, 1],
              [ 2, 3]]);

b = np.array([10, 28]);

answer = np.linalg.solve(A, b);
# print(answer);

# 1. A distillation column receives 1000 kg/h of a feed that is 50 wt% benzene and 50 wt% toluene.
# The distillate (D) is 95% benzene and the bottoms (B) is 4% benzene. Find D and B.
procees_coeff = np.array([[1, 1],
                          [0.95, 0.04]]);

constants = np.array([1000, 1000*0.5]);
answer = np.linalg.solve(procees_coeff, constants);

# print(answer);

# 2. A distillation column is fed 2000 kg/h of a mixture that is 40 wt% methanol and 60 wt% water.
# The distillate is 90 wt% methanol and the bottoms is 5 wt% methanol. Find D and B.

D_m, B_m, F, F_m = 0.9, 0.05, 2000, 0.4;
coeffs = np.array([[1, 1],
                          [D_m, B_m]]);

constant = np.array([F, F_m*F]);
answer = np.linalg.solve(coeffs, constant);

print(answer);

methanol_in = F * F_m;
print(methanol_in);
methanol_out = (answer[0] * D_m) + (answer[1] * B_m);
print(methanol_out)

if (methanol_in == methanol_out): 
    print("The process is balanced")
else:
    print("The process is not balanced")