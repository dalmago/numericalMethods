
def funcao (valor) :
    result = ((valor**5) -6)
    return (result)

def derivada (valor):
    result = (5*(valor**4))
    return (result)

def novo_valor (valor):
    result = (valor - ((funcao(valor))/(derivada(valor))))
    return (result)

x = float(input("chute inicial: "))
#print (funcao (x))

while abs(funcao(x)) > 0.0000000001:
    print (x)
    #print (funcao (x))
    x= novo_valor(x)


