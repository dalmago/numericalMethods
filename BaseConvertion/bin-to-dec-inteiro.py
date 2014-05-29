
x=input('Digite o numero binario a ser convertido:')

valorstr = str(x) #quebra o valor x em um vetor de caracteres

def binToDec(valor):
	tamanho = len(valor) #ingora o caractere de final de linha '\n'
	resultado = 0
	expoente = 0
	for i in range (tamanho):
		indice = tamanho-i-1
		resultado = resultado + (int(valor[indice])*(2**expoente))
		expoente = expoente + 1
	return resultado

i = '.'
if i in valorstr:
	valorfloat=float(valorstr)
	
	valorint=int(valorfloat)
	valorfloat=valorfloat-valorint
	
	resultint=binToDec(str(valorint))
	
	
	
else:
	print binToDec(valorstr)


#print binToDec(valor)
