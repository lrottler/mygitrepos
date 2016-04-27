def par_angle(d):
	''' This function takes distance in parsecs as input
	    1 pc = 3.26 light years
	    Computes and returns parallactic angle in arc seconds
	'''

	parallax = 1.0/d
	return parallax

# PA = par_angle(1000.)
# print str(PA * 1000) + " milliarcseconds"
