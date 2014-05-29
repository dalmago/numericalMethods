from numpy import *
 
coef=([1, 0, -1, -1]) #coeficiente

v2=0 
v1=0
x1=1 #intervalo (x1, x2)
x2=2
g0=poly1d(coef)
g1=g0.deriv()
div=polydiv(g0, g1)
resto=div[1]
while resto.o != 0:  
 div=polydiv(g0, g1)
 resto=div[1]
 if(g0(x1)*g1(x1)<0):
    v1=v1+1


 g0=g1
 g1=resto



g0=poly1d(coef)
g1=g0.deriv()
div=polydiv(g0, g1)
resto=div[1]
while resto.o != 0:  
 div=polydiv(g0, g1)
 resto=div[1]
 if(g0(x2)*g1(x2)<0):
    v2=v2+1


 g0=g1
 g1=resto
raizesnoin=abs(v1-v2)
print (raizesnoin)
