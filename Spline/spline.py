#!/usr/bin/python
# -*- coding: utf-8 -*-

from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

xmin = -6
xmax = 6
ymin = -1
ymax = 2

"""Plotar função f(x)"""
x = np.arange (xmin, xmax, 0.00025)
y = 1.0/(1+25*x**2)
plt.plot (x, y, linewidth=2, color='b', label='f(x)')

"""Pontos tabela"""
xi = np.arange (-5, 6, 1)
fi = 1.0/(1+25*xi**2)
#for i in range (len(xi)):
	#plt.plot (xi[i], fi[i], color='r', marker='.', markersize=12)

print ("\nPontos da tabela para f(x) = 1/(1+25x²):\n\nxi: " + str(xi) + "\n\n   yi:" + str(fi)+"\n")


"""Calcula diferenças divididas e polinômio de Newton de grau 2"""
xi = np.arange (-5, 5+1, 5)
fi = 1.0/(1+25*xi**2)
tamanho = len(xi)

ordem1=[]
for i in range (tamanho-1):
	ordem1.append (fi[i+1] - fi[i])
	ordem1[i] = ordem1[i] / 5.0

ordem2 = []
for i in range (tamanho-2):
	ordem2.append (ordem1[i+1] - ordem1[i])
	ordem2[i] = ordem2[i] / 10.0
newton = fi[0] + ordem1[0]*(x-xi[0]) + ordem2[0]*(x-xi[0])*(x-xi[1])

plt.plot (x, newton, color='y', label='Newton grau 2')


"""Calcula diferenças divididas e polinômio de Newton de grau 4"""
xi = np.arange (-4, 4+1, 2)
fi = 1.0/(1+25*xi**2)
tamanho = len(xi)

ordem1=[]
for i in range (tamanho-1):
	ordem1.append (fi[i+1] - fi[i])
	ordem1[i] = ordem1[i] / 2.0

ordem2 = []
for i in range (tamanho-2):
	ordem2.append (ordem1[i+1] - ordem1[i])
	ordem2[i] = ordem2[i] / 4.0

ordem3 = []
for i in range (tamanho-3):
	ordem3.append (ordem2[i+1] - ordem2[i])
	ordem3[i] = ordem3[i] / 6.0

ordem4 = []
for i in range (tamanho-4):
	ordem4.append (ordem3[i+1] - ordem3[i])
	ordem4[i] = ordem4[i] / 8.0

newton = fi[0] + ordem1[0]*(x-xi[0]) + ordem2[0]*(x-xi[0])*(x-xi[1]) + ordem3[0]*(x-xi[0])*(x-xi[1])*(x-xi[2]) + ordem4[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3]) 

plt.plot (x, newton, color='cyan', label='Newton grau 4')

"""Calcula diferenças divididas e polinômio de Newton de grau 10"""
xi = np.arange (-5, 5+1)
fi = 1.0/(1+25*xi**2)
tamanho = len(xi)

ordem1=[]
for i in range (tamanho-1):
	ordem1.append (fi[i+1] - fi[i])
	ordem1[i] = ordem1[i] / 1.0

ordem2 = []
for i in range (tamanho-2):
	ordem2.append (ordem1[i+1] - ordem1[i])
	ordem2[i] = ordem2[i] / 2.0

ordem3 = []
for i in range (tamanho-3):
	ordem3.append (ordem2[i+1] - ordem2[i])
	ordem3[i] = ordem3[i] / 3.0

ordem4 = []
for i in range (tamanho-4):
	ordem4.append (ordem3[i+1] - ordem3[i])
	ordem4[i] = ordem4[i] / 4.0

ordem5 = []
for i in range (tamanho-5):
	ordem5.append (ordem4[i+1] - ordem4[i])
	ordem5[i] = ordem5[i] / 5.0

ordem6 = []
for i in range (tamanho-6):
	ordem6.append (ordem5[i+1] - ordem5[i])
	ordem6[i] = ordem6[i] / 6.0

ordem7 = []
for i in range (tamanho-7):
	ordem7.append (ordem6[i+1] - ordem6[i])
	ordem7[i] = ordem7[i] / 7.0

ordem8 = []
for i in range (tamanho-8):
	ordem8.append (ordem7[i+1] - ordem7[i])
	ordem8[i] = ordem8[i] / 8.0

ordem9 = []
for i in range (tamanho-9):
	ordem9.append (ordem8[i+1] - ordem8[i])
	ordem9[i] = ordem9[i] / 9.0

ordem10 = []
for i in range (tamanho-10):
	ordem10.append (ordem9[i+1] - ordem9[i])
	ordem10[i] = ordem10[i] / 10.0

newton = fi[0] + ordem1[0]*(x-xi[0]) + ordem2[0]*(x-xi[0])*(x-xi[1]) + ordem3[0]*(x-xi[0])*(x-xi[1])*(x-xi[2]) + ordem4[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3]) + ordem5[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3])*(x-xi[4])+ ordem6[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3])*(x-xi[4])*(x-xi[5])+ ordem7[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3])*(x-xi[4])*(x-xi[5])*(x-xi[6])+ ordem8[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3])*(x-xi[4])*(x-xi[5])*(x-xi[6])*(x-xi[7])+ ordem9[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3])*(x-xi[4])*(x-xi[5])*(x-xi[6])*(x-xi[7])*(x-xi[8])+ ordem10[0]*(x-xi[0])*(x-xi[1])*(x-xi[2])*(x-xi[3])*(x-xi[4])*(x-xi[5])*(x-xi[6])*(x-xi[7])*(x-xi[8])*(x-xi[9])


plt.plot (x, newton, color='y',linewidth=2, label='Newton grau 10')

"""Calcula e plota spline linear"""
xi = np.arange (-5, -3)
fi = 1.0/(1+25*xi**2)

color='r'
linewidth =1

s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color, label='Spline linear')

xi = np.arange (-4, -2)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (-3, -1)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (-2, 0)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (-1, 1)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (0, 2)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (1, 3)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (2, 4)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (3, 5)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

xi = np.arange (4, 6)
fi = 1.0/(1+25*xi**2)
s = fi[0]*((xi-xi[1])/(xi[0]-xi[1])) + fi[1]*((xi-xi[0])/(xi[1]-xi[0]))
plt.plot (xi, s, linewidth=linewidth, color=color)

"""Calcula e plota spline cubica"""

cor = "k"
tamanho=2.5

xs = linspace (-5, -2, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-5, -4, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho, label='Spline Cubica')

xs = linspace (-5, -2, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-4, -3, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (-4, -1, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-3, -2, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (-3, 0, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-2, -1, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (-2, 1, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-1, 0, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (-1, 2, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (0, 1, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (0, 3, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (1, 2, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (1, 4, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (2, 3, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (2, 5, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (3, 4, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)

xs = linspace (2, 5, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (4, 5, 1000)
yi = s(xs)
plt.plot (xs, yi, color=cor, linewidth=tamanho)


"""Plota eixos e mostra grafico"""
plt.axhline (linewidth=1, color='k')
plt.axvline (linewidth=1, color='k')

plt.legend()
plt.axis ([xmin, xmax, ymin, ymax])
plt.show()
