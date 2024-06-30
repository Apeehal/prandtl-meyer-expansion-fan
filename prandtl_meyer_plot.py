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

# Create the inverse interpolation function
inverse_interpolation_func = interp1d(deflections, M, kind='cubic', fill_value='extrapolate')

# Example: Find the Mach number for a specific deflection angle
specific_deflection_angle = 20.0  # degrees
specific_mach_number = inverse_interpolation_func(specific_deflection_angle)

print(f"The Mach number for a deflection angle of {specific_deflection_angle} degrees is {specific_mach_number:.6f}.")

# Generate new deflection angles for interpolation
deflections_new = np.linspace(min(deflections), max(deflections), 5000)
M_new = inverse_interpolation_func(deflections_new)

# Plotting the original and interpolated data
plt.plot(deflections, M, 'o', label='Original data')
plt.plot(deflections_new, M_new, '-', label='Interpolated data')
plt.plot(specific_deflection_angle, specific_mach_number, 'rx', label=f'Deflection {specific_deflection_angle}°')
plt.xlabel('Deflection Angle (degrees)')
plt.ylabel('Mach Number (M)')
plt.title('Mach Number vs Prandtl-Meyer Expansion Angle')
plt.legend()
plt.grid(True)
plt.show()
