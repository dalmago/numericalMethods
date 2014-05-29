

x = float(input ("intervalo: "))
y = float(input())

def funcao(valor):
	resposta = (valor**2) - 5
	return resposta

val=[]

for i in range (1, 4):
	val.append((((y-x)*i)/4) + x)

res=[]

for i in range (3):
	res.append(funcao(val[i]))


for i in range (3):
	print ("\nx = %f" % val[i])
	print ("f(x) = %f" % res[i])

#print (val)
#print (res)
