import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

gamma = 1.4

def prendtl_meyer(M):
    k1 = (gamma+1)/(gamma-1)
    k2 = (gamma-1)/(gamma+1)
    deflection_angle = np.sqrt(k1)*np.arctan(np.sqrt(k2*((M**2)-1))) - np.arctan(np.sqrt(M**2-1))  
    return deflection_angle

M = np.linspace(1,10,1000)
deflections = []

for i in range(len(M)):
    angle_deflection = prendtl_meyer(M[i])
    angle_deflections_degrees = angle_deflection * (180/np.pi)
    deflections.append(angle_deflections_degrees)


# Plotting the results
plt.plot(M, deflections)
plt.xlabel('Mach Number (M)')
plt.ylabel('Deflection Angle (degrees)')
plt.title('Prandtl-Meyer Expansion Angle vs Mach Number')
plt.grid(True)
plt.show()