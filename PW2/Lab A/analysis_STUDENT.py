"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
t,y=np.loadtxt("freefall.csv",delimiter=",",skiprows=1,unpack=True)
#delimiter says how columns are seperated, skiprows=1 in order to skip the header, unpack=true says to give columns as seperate two arrays t,y

# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v=np.gradient(y,t)
a=np.gradient(v,t)
print("mean acceleration:",np.mean(a))
print("standard deviation",a.std())


# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
v_integrated=cumulative_trapezoid(a, t, initial=0) + v[0]
y_integrated=cumulative_trapezoid(v_integrated, t, initial=0) + y[0]
difference=np.abs(y-y_integrated)
print("max difference between original and integrated position:",np.max(difference))

# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig,axes=plt.subplots(3,1,sharex=True)

axes[0].plot(t,y)
axes[0].set_ylabel("position(m)")

axes[1].plot(t,v)
axes[1].set_ylabel("velocity(m/s)")

axes[2].plot(t,a)
axes[2].axhline(-9.81,linestyle="--")
axes[2].set_ylabel("acceleration(m/s^2)")
axes[2].set_xlabel("time(s)")

plt.tight_layout()
plt.savefig("motion.png")

