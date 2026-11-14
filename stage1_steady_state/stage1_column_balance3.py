import matplotlib.pyplot as plt
import numpy as np


# Testing...
x = [1, 2, 3, 4];
y = [10, 20, 5, 30];

# plt.plot(x, y);
# plt.xlabel("x values");
# plt.ylabel("y values");
# plt.show();


def column_balance(F, F_m, D_m, B_m): 
    coeffs = np.array([[1, 1],
                       [D_m, B_m]]);
    constants = np.array([F, F_m*F]);
    D, B = np.linalg.solve(coeffs, constants);
    return D, B;

F, F_m, B_m = 2000, 0.40, 0.05;
purities = np.linspace(0.60, 0.98, 20);
D_values = [];

for D_m in purities:
    D, B = column_balance(F, F_m, D_m, B_m);
    D_values.append(D);

D_formula = F * (F_m - B_m) / (purities - B_m)
print(np.allclose(D_formula, D_values))
# print(purities);
# print(D_values);

plt.plot(purities, D_values);
plt.xlabel("Distillate Purity, D_m (mass fraction methanol)");
plt.ylabel("Distillate Flow Rate, D (kg/h)");
plt.title("Effect of distillate purity on distillate flow");
plt.show();

