#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

xmin = -1
xmax = 7
ymin = 0
ymax = 300


x = np.array([0,1,2,3,4,5,6])
y = np.array([32, 47, 65, 92, 132, 190, 275])
xs = np.arange (xmin, xmax, 0.025)
phi1 = 32.13*(1.42)**xs
phi2 = 38.86*(xs)**0.96

plt.plot (xs, phi1, color='b', label='y(x) = a(b)^x')
plt.plot (xs, phi2, color='g', label='y(x) = a(x)^b')

for i in range (len(x)):
    plt.plot(x[i], y[i], color='r', marker='.',  markersize=12)

plt.axhline(linewidth=2, color='black') #desenha eixo x
plt.axvline(linewidth=2, color='black') #desenha eixo y

plt.legend()
plt.axis ([xmin, xmax, ymin, ymax])
plt.show()
