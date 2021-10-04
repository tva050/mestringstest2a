"""
Lennard-Jones potensialet
"""

import matplotlib.pyplot as plt
import numpy as np



# fysiske parametre
b = a = 1
v0 = 1


# Lennard-Jones funksjon
def ljp(r):
    func = v0*((a/r)**(12)-(b/r)**(6))
    return func

r = np.arange(0.5, 3, 0.1)

plt.plot(r,ljp(r))
plt.show
    
    

    
    

