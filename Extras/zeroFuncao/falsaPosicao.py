
x1 = float(input("Intervalo: "))
x2 = float(input())
z = int(input("Numero de iteracoes:\n"))

import math

def funcao(val):
    return math.sin(val)

for i in range (z):
    _x = (x1*(funcao(x2)) - x2*(funcao(x1)))/(funcao(x2)-funcao(x1))
    if (funcao(_x))*(funcao(x1)) < 0:
        x2 = _x
    else:
        aux = x1
        x1=_x
        x2=aux
    print (_x)

#print (_x)
