"""
Mestringstest 2a:
Lennard-Jones potensialet
"""

import matplotlib.pyplot as plt
import numpy as np


# fysiske parametre
v0 = 0.01
b = a = 3.3

# r_a=r/a=r/b
r_a = np.arange(0.5, 3, 0.001)


# Lennard-Jones potensialet funksjon
def lj_p(r_a):
    func = v0*((a/r_a)**(12)-(b/r_a)**(6))
    return func


plt.plot(r_a,lj_p(r_a))
plt.xlabel("r/a ")
plt.ylabel("ljp")
plt.show
    
    

