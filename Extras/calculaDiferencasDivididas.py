xk = [1,2,3,4,5,6]
fk = [2.1, 3.1, 4.15, 5.09, 6.18, 7.1]

ordem1 = []
ordem2 = []
ordem3 = []
ordem4 = []
ordem5 = []
for k in range (5):
	ordem1.append (float(fk[k+1]-fk[k]))

for k in range (4):
	ordem2.append (float(ordem1[k+1]-ordem1[k])/2)

for k in range (3):
	ordem3.append (float(ordem2[k+1]-ordem2[k])/3)

for k in range (2):
	ordem4.append (float(ordem3[k+1]-ordem3[k])/4)

for k in range (1):
	ordem5.append (float(ordem4[k+1]-ordem4[k])/5)

print ("ordem1:")
print ordem1

print ("ordem2:")
print ordem2

print ("ordem3:")
print ordem3

print ("ordem4:")
print ordem4

print ("ordem5:")
print ordem5
