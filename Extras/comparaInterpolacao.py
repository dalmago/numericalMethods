def vander (x):
	return (1.73 - (0.243*x) + (0.7975*(x**2)) - (0.2016*(x**3)) + (0.0175*(x**4)))

def lagrange (x):
	l0 = ((x-2)*(x-3)*(x-4)*(x-5))/24
	l1 = ((x-1)*(x-3)*(x-4)*(x-5))/(-6)
	l2 = ((x-1)*(x-2)*(x-4)*(x-5))/4
	l3 = ((x-1)*(x-2)*(x-3)*(x-5))/(-6)
	l4 = ((x-1)*(x-2)*(x-3)*(x-4))/24
	return 2.1*l0 + 3.1*l1 + 4.15*l2 + 5.09*l3 + 6.18*l4
	
def newton(x):
	return 2.1 + (x-1) + 0.025*(x-1)*(x-2) - 0.0266*(x-1)*(x-2)*(x-3) + 0.0175*(x-1)*(x-2)*(x-3)*(x-4)

varia = float(input ('valor:'))
print ("vandermond")
print (vander(varia))
print ("lagrange")
print (lagrange(varia))
print ("newton")
print (newton(varia))
