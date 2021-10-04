"""
Mestringstest 2a:
Lennard-Jones potensialet
"""

import matplotlib.pyplot as plt
import numpy as np


# r=r/a=r/b
r = np.arange(0.5, 3, 0.001)


# Lennard-Jones potential
def lj_p(r):
    
    
    func = ((r)**(-12)-(r)**(-6))
    
    return func


plt.plot(r,lj_p(r))
plt.xlabel("r/a")
plt.ylabel("v/v0")
plt.ylim((-0.25,0.1))
plt.show

