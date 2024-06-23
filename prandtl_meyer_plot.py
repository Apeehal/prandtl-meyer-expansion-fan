import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def prandtl_meyer_function(M, gamma):
    """Calculate the Prandtl-Meyer function nu for a given Mach number M and specific heat ratio gamma."""
    return math.sqrt((gamma + 1) / (gamma - 1)) * math.atan(math.sqrt((gamma - 1) * (M**2 - 1) / (gamma + 1))) - math.atan(math.sqrt(M**2 - 1))

def mach_from_prandtl_meyer(nu, gamma):
    """Calculate the Mach number M for a given Prandtl-Meyer function nu and specific heat ratio gamma."""
    def equation(M):
        return prandtl_meyer_function(M, gamma) - nu

    # Use a root-finding method to solve for M
    M_initial_guess = 1
    M_solution = fsolve(equation, M_initial_guess)
    return M_solution[0]

# Define the specific heat ratio (gamma) for air, typically 1.4
gamma = 1.4

# Define the initial Mach number
M1 = 1

# Define the initial static temperature (in Kelvin)
T1 = 300  # Example initial temperature

# Define the specific gas constant for air (in J/(kg*K))
R = 287  # J/(kg*K)

# Compute the Prandtl-Meyer function (nu) for the given Mach number
nu1 = prandtl_meyer_function(M1, gamma)

# Define the range of deflection angles (in degrees)
theta_range = np.linspace(0, 45, 100)  # From 0 to 45 degrees

# Arrays to store results
M2_values = []
T2_values = []
V2_values = []

for theta in theta_range:
    # Convert deflection angle from degrees to radians for the calculation
    theta_rad = math.radians(theta)

    # Compute the final Prandtl-Meyer function (nu2) after deflection
    nu2 = nu1 + theta_rad

    # Compute the final Mach number after expansion
    M2 = mach_from_prandtl_meyer(nu2, gamma)
    M2_values.append(M2)

    # Compute the final static temperature using the isentropic relation
    T2 = T1 * (1 + ((gamma - 1) / 2) * M1**2) / (1 + ((gamma - 1) / 2) * M2**2)
    T2_values.append(T2)

    # Compute the final velocity
    a2 = (gamma * R * T2)**0.5  # Speed of sound at final temperature
    V2 = M2 * a2
    V2_values.append(V2)

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(theta_range, V2_values, label='Final Velocity $V_2$')
plt.xlabel('Deflection Angle $\\theta$ (degrees)')
plt.ylabel('Final Velocity $V_2$ (m/s)')
plt.title('Final Velocity after Prandtl-Meyer Expansion vs. Deflection Angle')
plt.legend()
plt.grid(True)
plt.show()
