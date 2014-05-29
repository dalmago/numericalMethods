from numpy import array, log

y = array([30, 10, 9, 6, 5, 4, 4])
z = log(y)
g1 = array([1, 1, 1, 1, 1, 1, 1])
g2 = array([-8, -6, -4, -2, 0, 2, 4])
soma = 0

for i in range (7):
    soma = soma + (z[i]*g1[i])
print soma

