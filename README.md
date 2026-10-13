# PW1 Lab A

Computer Science for Physics and Chemistry.

RESULTS:
Pure-Python loop: 2.477426 seconds
NumPy version:    0.000195 seconds
NumPy is 12710.75 times faster

CONCLUSION:
In this lab I learned how to test the radioactive decay simulation and compare two different versions of the code. Numpy version was faster. The test also showed that the simulation works correctly.

# PW2 Lab A
The mean acceleration measured from the free-fall data was about -8,58 m/s^2. The acceleration was very noisy because the position data had some small noise, and taking derivative made the noise bigger. WE took the derivative twice to get acceleration so the noise became even bigger. After integrating acceleration back we got about 0.78 m difference in position. This showed that we can get a close result even with noisy acceleration.

 
#PW2 Lab B
Part 2 optimization methods
Gradient descent newtons method and SLSQP found the minimum of simple function near x=3. Newtons method and SLSQP were faster. Gradient dascent could become unstable for the more difficukt function.
Part 3 Chemical reaction rate 
We used optimization to find the rate constant by minimizing the difference between measured and predicted concentrations. The fitted rate constant was approximately 15.6
Part 4 Chemical equilibrium
Newtons method and SLSQP gave similar results, with x=0.66 mol. The equilibrium amounts were approximately 0.34 mol H2, 0.34 mol I2, and 1.33 mol HI





