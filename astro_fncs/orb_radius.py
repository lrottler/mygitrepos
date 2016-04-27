def orb_radius(period, mass_sum):
	'''period: orbital period in years
	   mass_sum: total mass of binary system

	   This function computes and returns the following
	   using the above inputs.

	   R: orbital radius of secondary around primary in AU
	'''

	radius = ((mass_sum)*period**2)**(1./3)
	return radius

# R = orb_radius(69.0, 3.0)
# print R
# print 2**38
