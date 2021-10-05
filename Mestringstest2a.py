"""
Mestringstest 2a:
Lennard-Jones potensialet
"""

import matplotlib.pyplot as plt
import numpy as np
#from scipy.optimize import fmin


# r=r/a=r/b
r_a = np.arange(0.5, 3, 0.001)


# Lennard-Jones potential
def lj_p(r_a):
    """
    Redefining the Lennard-Jones potential (v = v0 ((a/r)**12 - (b/r)**6)) to, 
    write the function for v/v0 against r/a.
    """
    
    func = ((r_a)**(-12)-(r_a)**(-6))
    
    return func

#min_y_index = np.argmin(lj_p)

#x = (r[min_y_index])
#y = (lj_p[min_y_index])
#print(x,y)


m = a = b = v0 =  1
r = (3*a)/2
v = 0 


#t = np.arange(0, 10, 0.001)
t = 0
dt = 0.1
tmax = 10

# position and time, empty list
position_list = []  
time_list = []

while t < tmax:
    
    # Force 
    F = 6*(2-r**6)/r**13
    
    # Euler-Cromers metode
    a = F/m
    v = v + a*dt
    r = r + v*dt
    
    position_list.append(r)
    time_list.append(t)
    
    
    t = t + dt

plt.plot(r_a,lj_p(r_a), color="red")
plt.axhline(y=0, color="black", linestyle='--')
plt.title("Plot v/v0 against r/a, (2a.1)")
plt.xlabel("r/a")
plt.ylabel(r'$v/v_0$')
plt.ylim((-0.25,0.1))
plt.show()

plt.plot(time_list, position_list, color = "red")
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("r(t), (2a.5)")
plt.show()


