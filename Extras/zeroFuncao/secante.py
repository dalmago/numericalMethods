import math

def funcao (valor):
    return math.sin(valor)

#def funcao (valor):
    #return ((valor**3) - 9*valor + 3)


x0 = float(input("Chutes: "))
x1 = float(input())

_x = 1 #so pra entrar no loop, cuidar se nao da pau na funcao

while abs(funcao(_x)) > 0.00000000000001:
    _x = ((x0 * funcao(x1)) - (x1 * funcao(x0)))/(funcao(x1) - funcao(x0))
    print (_x)
    if funcao(x0) * funcao(_x) < 0:
        x1 = _x
    else:
        x0 = _x

print("f(x): %.15f" % funcao(_x))
