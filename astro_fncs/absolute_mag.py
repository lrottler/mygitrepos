def abs_magnitude(m,d):
	'''This function takes the visual magnitude of a star,
	   m and the distance in parsecs from the sun as input.
	   Computes and returns the absolute magnitude of the
	   star.
	'''

	import numpy as np

	AbsMag = m - 5 * np.log10(d) + 5
	return AbsMag

# M = abs_magnitude(-1.44, 2.637)
# print M
