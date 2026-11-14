# Example 3 (TCH 201 Module 2, slide 15): two-unit process, steady state, no reaction.
# All balances are written on component flows (kg/h of A and B).

# Known streams: (total flow in kg/h, mass fraction of A)
feed1 = (100, 0.50);  #feed to Unit 1
feed2 = (30, 0.30);  #feed to the mixing point
prod1 = (40, 0.90);  #product leaving Unit 1
prod2 = (30, 0.60); #product leaving Unit 2

def components(flow, x_A):
    """Return the kg/h of A and of B in a stream."""
    A = flow * x_A
    B = flow - A
    return A, B

feed1_A, feed1_B = components(*feed1)
feed2_A, feed2_B = components(*feed2)
prod1_A, prod1_B = components(*prod1)
prod2_A, prod2_B = components(*prod2)


# Overall balance (the box around everything): in = out
m3_A = feed1_A + feed2_A - prod1_A - prod2_A
m3_B = feed1_B + feed2_B - prod1_B - prod2_B

m3 = m3_A + m3_B
x3_A = m3_A / m3
x3_B = 1 - x3_A
print(f"Stream 3: {m3:.2f} kg/h, x_A = {x3_A:.4f} and x_B = {x3_B:.4f}");


# Unit 1 balance: in = out, so stream 1 = feed - product
m1_A = feed1_A - prod1_A;
m1_B = feed1_B - prod1_B;

m1 = m1_A + m1_B;
x1_A = m1_A / m1;
x1_B = 1 - x1_A;
print(f"Stream 1: {m1:.2f} kg/h, x_A = {x1_A:.4f} and x_B = {x1_B:.4f}")


#Unit 2 balance: in = out, so stream 2 = prod2 + m3
m2_A = prod2_A + m3_A;
m2_B = prod2_B + m3_B;

m2 = m2_A + m2_B;
x2_A = m2_A / m2;
x2_B = m2_B / m2;
print(f"Stream 2: {m2:.2f} kg/h, x_A = {x2_A:.4f} and x_B = {x2_B:.4f}");

#Total Material Balance
F = (feed1_A+feed1_B) + (feed2_A+feed2_B) 
P = (prod1_A+prod1_B) + (prod2_A+prod2_B) + m3
if (F==P): 
    print("The Process is Balanced")
else:
    print("The Process is not Balanced")