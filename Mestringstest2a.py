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
    """
    Redefining the Lennard-Jones potential (v = v0 ((a/r)**12 - (b/r)**6)) to, 
    write the function for v/v0 against r/a.
    """
    
    func = ((r)**(-12)-(r)**(-6))
    
    return func


plt.plot(r,lj_p(r))
plt.axhline(y=0, color='r', linestyle='--')
plt.title("Plot v/v0 against r/a")
plt.xlabel("r/a")
plt.ylabel(r'$v/v_0$')
plt.ylim((-0.25,0.1))
plt.show()


