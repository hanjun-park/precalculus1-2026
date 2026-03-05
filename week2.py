import matplotlib.pyplot as plt
import numpy as np
import math

# We want to create three plots to verify whether the series "\sum e^n n! / n^n" converges or diverges.

# 1) Plot the graph of b_n = (1+1/n)^n to see if it really converges to exp.
#    x-axis: n, y-axis: (1+1/n)^n
# 2) Plot the ratio r_n = a_{n+1}/a_n per n.
#    x-axis: n, y-axis: a_{n+1}/a_n
# 3) Plot a_n = e^n n! / n^n
#    x-axis: n, y-axis: a_n
# 4) Plot the graph of d_n = n^{1/n}
#    x-axis: n, y-axis: n^{1/n}

##############################  YOU SHOULD FILL [FILL HERE]  ########################################

# 1. Create a range of integers for visualization (x-axis).
n_values = np.arange(1,101) # Hint: np.arange(a, b) creates the integer list from a to b-1. a, b should be integer

# 2. Define the sequence that approaches e
b_n = ( 1+ 1/n_values ) ** n_values # Hint: a**b is equal to operation a^b.

# 3. Define the ratio
r_n = np.e / b_n # Hint: np.e is equal to exponential

# 4. Define d_n = n^{1/n}
d_n = n_values ** (1/n_values)

#####################################################################################################

# Calculate terms a_n iteratively
a_n = np.zeros(len(n_values))
current_a = (math.e * math.factorial(1)) / (1**1)
for i in range(len(n_values)):
    a_n[i] = current_a
    if i < len(n_values) - 1:
        current_a = current_a * r_n[i]


# Plot three plots using matplotlib
fig, axes = plt.subplots(1, 4, figsize=(18, 5))

# (1+1/n)^n -> e
axes[0].plot(n_values, b_n, 'o-', label=r'$(1+\frac{1}{n})^n$')
axes[0].axhline(y=np.e, color='r', linestyle='--', label=r'$y=e$')
axes[0].set_title(r'Sequence $(1+\frac{1}{n})^n \to e$')
axes[0].set_xlabel('n')
axes[0].set_ylabel('Value')
axes[0].legend()
axes[0].grid(True)

# Ratio a_{n+1}/a_n -> 1 from above
axes[1].plot(n_values, r_n, 'g*-', label=r'Ratio $\frac{a_{n+1}}{a_n}$')
axes[1].axhline(y=1, color='k', linestyle='--', label='Ratio = 1')
axes[1].set_title(r'Ratio Test: $\frac{a_{n+1}}{a_n} > 1$')
axes[1].set_xlabel('n')
axes[1].set_ylabel('Ratio')
axes[1].legend()
axes[1].grid(True)

# Terms a_n diverging
axes[2].plot(n_values, a_n, 'm^-', label=r'$a_n = \frac{e^n n!}{n^n}$')
axes[2].set_title(r'Terms $a_n$ (Divergence)')
axes[2].set_xlabel('n')
axes[2].set_ylabel('Term Value')
axes[2].legend()
axes[2].grid(True)

# d_n plot
axes[3].plot(n_values, d_n, 'y^-', label=r'$d_n = n^\frac{1}{n}$')
axes[3].set_title(r'$n^\frac{1}{n}$')
axes[3].set_xlabel('n')
axes[3].set_ylabel('Value')
axes[3].legend()
axes[3].grid(True)

plt.tight_layout()
plt.show()
