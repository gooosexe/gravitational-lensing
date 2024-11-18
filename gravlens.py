import numpy as np
import matplotlib.pyplot as plt

# GLOBAL CONSTANTS AND PARAMS
# the position of the observer is always (0, 0, 0)
# positions in meters
source_position = np.array([0, 4.962e+17, 1.786559e26])
# Lens parameters
M = 1.989e30  # Lens mass (solar masses)
D_l = 5.324482e11          # Distance to lens (m)
D_s = source_position[2]      # Distance to source (m)
D_ls = D_s - D_l     # Lens-source distance (m)
c = 299792458  # Speed of light (m/s)
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)

# TODO: consider for strong refraction and weak refraction

def create_circle(radius, num_points=500, center=(0, 0)):
	""" Function to create a circle as a series of points.
	"""
	theta = np.linspace(0, 2 * np.pi, num_points)
	x = radius * np.cos(theta) + center[0]
	y = radius * np.sin(theta) + center[1]
	return x, y

def calculate_image(source_position, M, D_l, D_s, D_ls):
	""" Calculate the image of the source due to gravitational lensing.
	"""
	xi = np.sqrt(source_position[0]**2 + source_position[1]**2)  # Impact parameter
	pass

def get_deflect_angle(M, xi):
	""" Calculate the angle of deflection.
	"""
	def_alpha = 4 * G * M / (c**2 * xi)  # Angle of deflection
	return def_alpha

def get_source_position(source_position):
	""" Get the position of the source.
	"""
	beta = np.rad2deg(np.arctan2(source_position[1], D_s)) # declination of the source in degrees
	phi = np.rad2deg(np.arctan2(source_position[0], D_s)) # right ascension of the source in degrees
	return phi, beta

def get_image_pos_strong(phi, beta, M, D_l, D_s, D_ls):
	""" Get the position of the image.
	"""
	theta_1 = 1/2 * (beta + np.sqrt(beta**2 + 4*(4*G*M*D_ls)/( c**2 * D_l * D_s )))
	theta_2 = 1/2 * (beta - np.sqrt(beta**2 + 4*(4*G*M*D_ls)/( c**2 * D_l * D_s )))
	# dont worry about this one
	#phi = phi + def_alpha / D_s # right ascension of the image
	return theta_1, theta_2

def get_image_pos_weak(phi, beta, M, D_s, D_ls):
	""" Get the position of the image.
	"""
	alpha = get_deflect_angle(M, xi)*(D_ls/D_s)  # deflection angle
	theta = beta + alpha
	# dont worry about this one
	#phi = phi + def_alpha / D_s # right ascension of the image
	return 0, theta
	

if __name__ == "__main__":
	phi, beta = get_source_position(source_position)
	#xi = np.sqrt(source_position[0]**2 + source_position[1]**2) # impact parameter
	#alpha_hat = get_deflect_angle(M, xi)  # deflection angle
	theta_1, theta_2 = get_image_pos_strong(phi, beta, M, D_l, D_s, D_ls)

	theta1_arcsec = theta_1 * 3600
	theta2_arcsec = theta_2 * 3600
	beta_arcsec = beta * 3600
	phi_arcsec = phi * 3600

	theta_e = np.sqrt(4*G*M*D_ls/(c**2*D_l*D_s))  # Einstein radius

	lens_x, lens_y = create_circle(theta_e, center=(0, 0))

	print("Einstein radius: ", theta_e)
	print("Source position: ", source_position)
	print("Lens mass: ", M)
	print("Deflection angle: ", theta_1, theta_2)

	# Plot
	plt.figure(figsize=(8, 8))
	plt.plot(0, 0, 'ko', label="Lens Center")
	plt.plot(lens_x, lens_y, label="Lens", linestyle="--", color="black")
	plt.plot(phi_arcsec, beta_arcsec, 'bo', label="Source center")
	plt.plot(phi_arcsec, theta1_arcsec, 'go', label="Image")
	plt.plot(phi_arcsec, theta2_arcsec, 'go', label="Image")
	plt.title("Gravitational Lensing Simulation")
	plt.xlabel("X (arcsec)")
	plt.ylabel("Y (arcsec)")
	plt.show()

