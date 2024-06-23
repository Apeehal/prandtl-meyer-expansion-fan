# prandtl_meyer_example.py
import gasdynamics as gd

# Define the specific heat ratio (gamma) for air, typically 1.4
gamma = 1.4

# Define the initial Mach number
M1 = 2.0

# Compute the Prandtl-Meyer function (nu) for the given Mach number
nu1 = gd.prandtl_meyer.nu(M1, gamma)

# Define the deflection angle (in degrees)
theta = 20

# Compute the final Prandtl-Meyer function (nu2) after deflection
nu2 = nu1 + theta

# Compute the final Mach number after expansion
M2 = gd.prandtl_meyer.mach(nu2, gamma)

print(f"Initial Mach number: {M1}")
print(f"Deflection angle: {theta} degrees")
print(f"Final Mach number: {M2}")
