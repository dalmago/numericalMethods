x= input ('Digite o valor a ser lido\n')

def decToBin(valor):
	valor = int(valor)
	resultado = []
	while valor != 0:
		#print (valor)
		if valor % 2 == 1:
			resultado.append(1)
		else:
			resultado.append(0)
		valor = int(valor / 2 )

	resultado = resultado[::-1] #inverte lista
	return (resultado)


def floatToBin(valor):	
	resultado = []
	while valor!=0:
		valor = 2*valor		
		if valor >= 1:
			d=1
			resultado.append(1)
		else:
			d=0
			resultado.append(0)
		valor=valor-d
	return (resultado)

def converteLista(lista):
	y=''
	for i in lista:
		if i != ',' and i != ' ':
			y=y+str(i)
	return y


if type(x) is float:
	y=x-int(x) #parte flutuante
	z=int(x) #parte inteira
	resultint=decToBin(z)
	resultfloat=floatToBin(y)
	print converteLista(resultint) + '.' + converteLista(resultfloat)

elif type (x) is int:
	result=decToBin(x)
	print converteLista(result)
