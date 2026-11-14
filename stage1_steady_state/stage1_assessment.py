import numpy as np;
import matplotlib.pyplot as plt;

# Question:
# A column is fed 5000 kg/h of a mixture that is 30 wt% ethanol and 70 wt%
# water. The distillate is 85 wt% ethanol, and the bottoms is 2 wt% ethanol.

def column_balance(F, F_e, D_e, B_e):
    coeffs = np.array([[1, 1],
                       [D_e, B_e]]);
    constants = np.array([F, F*F_e]);
    D, B = np.linalg.solve(coeffs, constants);
    return D, B;

D, B = column_balance(5000, 0.30, 0.85, 0.02);
print("D =", D, " B =", B);
print(np.isclose(0.30 * 5000, 0.85 * D + 0.02 * B));

F, D_e, B_e = 5000, 0.85, 0.02        # fixed: feed flow, distillate fraction, bottoms fraction
feed_fractions = np.linspace(0.20, 0.45, 20)
B_values = []

for F_e in feed_fractions:
    D, B = column_balance(F, F_e, D_e, B_e)
    B_values.append(B)

plt.plot(feed_fractions, B_values);
plt.xlabel("Feed composition, F_e (mass fraction ethanol)")
plt.ylabel("Bottoms flow rate, B (kg/h)")
plt.title("Effect of feed composition on bottoms flow rate")
plt.show();