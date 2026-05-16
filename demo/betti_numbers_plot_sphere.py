__author__ = 'stephenhky'

import matplotlib.pyplot as plt
import pylab
import numpy as np
from ripser import ripser
import demo.examples as eg

# 1. Downsample the sphere dataset!
# eg.sphere has 2601 points. Taking every 15th point reduces it to ~174 points.
# This keeps the sphere shape intact while making it computationally feasible.
small_sphere = eg.sphere[::15]

# 2. Compute the persistence diagram using ripser
# We set maxdim=2 because spheres have a Betti 2 feature (a 2D void/cavity)
result = ripser(small_sphere, maxdim=2)
diagrams = result['dgms']

# Betti 0 information is always stored in the first diagram index [0]
betti0_intervals = diagrams[0]

# 2. Define the epsilon steps you want to plot
epsilons = np.linspace(0, 2, 101)

# 4. Calculate Betti 0, Betti 1, and Betti 2 for each epsilon
betti0_series = []
betti1_series = []
betti2_series = []
for ep in epsilons:
    # Betti 0 (Connected components)
    b0 = np.sum((diagrams[0][:, 0] <= ep) & (diagrams[0][:, 1] > ep))
    betti0_series.append(b0)
    
    # Betti 1 (Tunnels/Loops) - Spheres shouldn't really have these, mostly noise
    b1 = np.sum((diagrams[1][:, 0] <= ep) & (diagrams[1][:, 1] > ep))
    betti1_series.append(b1)
    
    # Betti 2 (Voids/Cavities) - This represents the hollow inside of the sphere
    b2 = np.sum((diagrams[2][:, 0] <= ep) & (diagrams[2][:, 1] > ep))
    betti2_series.append(b2)

# 5. Plot the results
plt.figure(figsize=(10, 6))
plt.plot(epsilons, betti0_series, label='Betti 0 (Components)', color='blue')
plt.plot(epsilons, betti1_series, label='Betti 1 (Loops/Tunnels)', color='orange', linestyle='--')
plt.plot(epsilons, betti2_series, label='Betti 2 (Cavities/Voids)', color='green', linewidth=2)

plt.xlabel('Epsilon Threshold')
plt.ylabel('Betti Number Count')
plt.title('Betti Numbers vs. Epsilon for a 3D Sphere')
plt.legend()
plt.grid(True)

pylab.show()

# plt.scatter(eg.ring[:,0], eg.ring[:,1])
# pylab.show()
# C:\Users\fst16\anaconda3\python.exe -m demo.betti_numbers_plot_sphere