"""
Mestringstest 2a:
Lennard-Jones potensialet
"""
from math import *
import matplotlib.pyplot as plt
import numpy as np

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

# Getting the values for minimum point
x_min = r_a[np.argmin(lj_p(r_a))]
y_min = min(lj_p(r_a))

print("MINIMUM POINT OF FUNCTION lj_p")
print("-----------------------------------------------------")
print("x-min:", round(x_min, 3),"|", "y-min:", round(y_min,4))

# Physical variables
m = 1           # mass
v = 0           # velocity
v0 =  1         # start velocity
a = b = 1   

r = (3*a)/2     # position 

# t ∈ [0,10]
t = 0
tmax = 10
dt = 0.001

# position and time, empty list
position_list = []  
time_list = []

while t < tmax:
    
    # Force 
    F = 6*(2-r**6)/r**13
    
    # Euler-Cromers metode
    acc = F/m
    v = v + acc*dt
    r = r + v*dt
    
    position_list.append(r)
    time_list.append(t)
    
    t = t + dt

plt.plot(r_a,lj_p(r_a), color="red")
plt.axhline(y=0, color="black", linestyle='--')
plt.title("Plot v/v0 against r/a, (2a.1)")
plt.xlabel("r/a")
plt.ylabel(r'$v/v_0$')
plt.ylim((-0.3,0.1))
plt.show()

plt.plot(time_list, position_list, color = "red")
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("r(t), (2a.5)")
plt.show()
