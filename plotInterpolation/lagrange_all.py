#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

xmin = -1 
xmax = 6
ymin = -1 
ymax = 8
x = np.arange (xmin, xmax, 0.025)

"""Lagrange"""
l0 = ((x-2)*(x-3)*(x-4)*(x-5))/24

l1 = ((x-1)*(x-3)*(x-4)*(x-5))/(-6)

l2 = ((x-1)*(x-2)*(x-4)*(x-5))/4

l3 = ((x-1)*(x-2)*(x-3)*(x-5))/(-6) 

l4 = ((x-1)*(x-2)*(x-3)*(x-4))/24

plt.plot (x, l0, color='b', label='L0', linewidth=1.5)
plt.plot (x, l1, color='g', label='L1', linewidth=1.5)
plt.plot (x, l2, color='y', label='L2', linewidth=1.5)
plt.plot (x, l3, color='k', label='L3', linewidth=1.5)
plt.plot (x, l4, color='m', label='L4', linewidth=1.5)

lagra = 2.1*l0 + 3.1*l1 + 4.15*l2 + 5.09*l3 + 6.18*l4
plt.plot (x, lagra, color='c', label='Lagrange') #plota polinomio


plt.axhline(linewidth=2, color='black') #desenha eixo x
plt.axvline(linewidth=2, color='black') #desenha eixo y

plt.axhline(y = 1, linewidth=2, color='black') #desenha linha y=1

"""plota pontos da tabela"""
#x = np.arange (1, 6)
#y = 1.73 - 0.243*x + 0.7975*(x**2) - 0.2016*(x**3) + 0.0175*(x**4)
xk = [1,2,3,4,5]
yk = [2.1, 3.1, 4.15, 5.09, 6.18]
for i in range (len(xk)):
	plt.plot(xk[i], yk[i], color='r', marker='.',  markersize=12)


plt.legend()
plt.axis ([xmin, xmax, ymin, ymax])
plt.show()

