#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

xmin = -1 
xmax = 6
ymin = -1 
ymax = 8
x = np.arange (xmin, xmax, 0.025)

"""Newton"""
new = 2.1 + (x-1) + 0.025*(x-1)*(x-2) - 0.0266*(x-1)*(x-2)*(x-3) + 0.0175*(x-1)*(x-2)*(x-3)*(x-4)

plt.plot (x, new, color='b', label='Newton') #plota polinomio


plt.axhline(linewidth=2, color='black') #desenha eixo x
plt.axvline(linewidth=2, color='black') #desenha eixo y


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

