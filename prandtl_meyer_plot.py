import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

gamma = 1.4

def prendtl_meyer(M):
    k1 = (gamma + 1) / (gamma - 1)
    k2 = (gamma - 1) / (gamma + 1)
    deflection_angle = np.sqrt(k1) * np.arctan(np.sqrt(k2 * ((M**2) - 1))) - np.arctan(np.sqrt(M**2 - 1))  
    return np.degrees(deflection_angle)  # Convert to degrees

M = np.linspace(1, 10, 1000)  # Typically, M should start from 1 since Prandtl-Meyer function is defined for supersonic flows
deflections = [prendtl_meyer(m) for m in M]

# Create the interpolation function
interpolation_func = interp1d(M, deflections, kind='cubic')

# Example: Find the angle of deflection at a specific Mach number
specific_mach_number = 1.5
specific_deflection_angle = interpolation_func(specific_mach_number)

print(f"The angle of deflection at Mach {specific_mach_number} is {specific_deflection_angle:.6f} degrees.")

# Generate new Mach numbers for interpolation
M_new = np.linspace(1, 10, 5000)
deflections_new = interpolation_func(M_new)

# Plotting the original and interpolated data
plt.plot(M, deflections, 'o', label='Original data')
plt.plot(M_new, deflections_new, '-', label='Interpolated data')
plt.plot(specific_mach_number, specific_deflection_angle, 'rx', label=f'Mach {specific_mach_number}')
plt.xlabel('Mach Number (M)')
plt.ylabel('Deflection Angle (degrees)')
plt.title('Prandtl-Meyer Expansion Angle vs Mach Number')
plt.legend()
plt.grid(True)
plt.show()
