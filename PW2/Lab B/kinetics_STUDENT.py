"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.
t, C=np.loadtxt("kinetics.csv", delimiter=",",skiprows=1, unpack=True)
C0=C[0]


# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.
def total_error(k):
    return np.sum((C-C0**np.exp(-k*t))**2)



# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
minimized=minimize(total_error,method="SLSQP",bounds=[(0,5)],x0=0.5)
print("fitted k:",minimized.x[0])

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
C_fit=C0**np.exp(-minimized.x[0]*t)
plt.scatter(t,C,label="measured data")
plt.plot(t,C_fit,label="fitted curve")

plt.xlabel("time")
plt.ylabel("concentration")
plt.legend()
plt.tight_layout()
plt.savefig("kinetics.png")

