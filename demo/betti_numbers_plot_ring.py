import matplotlib.pyplot as plt
import pylab
import numpy as np
from ripser import ripser
import demo.examples as eg

# 1. Compute the entire persistence diagram instantly using ripser
# (ripser only does Vietoris-Rips, so this replaces the VR loop)
result = ripser(eg.ring)
diagrams = result['dgms']

# Betti 0 information is always stored in the first diagram index [0]
betti0_intervals = diagrams[0]

# 2. Define the epsilon steps you want to plot
epsilons = np.linspace(0, 2, 101)

# 3. Calculate Betti 0 for each epsilon
# A feature is alive at 'ep' if it was born <= ep AND dies > ep
vr_betti0s = []
for ep in epsilons:
    alive_features = np.sum((betti0_intervals[:, 0] <= ep) & (betti0_intervals[:, 1] > ep))
    vr_betti0s.append(alive_features)

# 4. Plot the results
plt.plot(epsilons, vr_betti0s, label='Vietoris-Rips Complex (Ripser)')
plt.xlabel('Epsilon')
plt.ylabel('Betti 0')
plt.title('Betti 0 Plot using Ripser')
plt.legend()

pylab.show()

# plt.scatter(eg.ring[:,0], eg.ring[:,1])
# pylab.show()
# C:\Users\fst16\anaconda3\python.exe -m demo.betti_numbers_plot_ring