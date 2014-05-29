from numpy import linspace
from numpy.random import randn
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

xmin = -6
xmax = 6
ymin = -1
ymax = 2
x = linspace (-5, 5, 400)
y = (1.0/(1+25*x**2))
#plt.plot (x, y, linewidth=2, color='b', label='f(x)')

xs = linspace (-5, -2, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-5, -4, 1000)
yi = s(xs)
plt.plot (xs, yi, color="green", linewidth=2, label='spline')

xs = linspace (-5, -2, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-4, -3, 1000)
#xs = [-4, -3]
yi = s(xs)
plt.plot (xs, yi, color="b", linewidth=2)

xs = linspace (-4, -1, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-3, -2, 1000)
#xs = [-3, -2]
yi = s(xs)
plt.plot (xs, yi, color="r", linewidth=2)

xs = linspace (-3, 0, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-2, -1, 1000)
#xs = [-2, -1]
yi = s(xs)
plt.plot (xs, yi, color="cyan", linewidth=2)

xs = linspace (-2, 1, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (-1, 0, 1000)
#xs = [-2, -1]
yi = s(xs)
plt.plot (xs, yi, color="b", linewidth=2)


xs = linspace (-1, 2, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (0, 1, 1000)
yi = s(xs)
plt.plot (xs, yi, color="green", linewidth=2)


xs = linspace (0, 3, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (1, 2, 1000)
yi = s(xs)
plt.plot (xs, yi, color="magenta", linewidth=2)

xs = linspace (1, 4, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (2, 3, 1000)
yi = s(xs)
plt.plot (xs, yi, color="yellow", linewidth=2)


xs = linspace (2, 5, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (3, 4, 1000)
yi = s(xs)
plt.plot (xs, yi, color="b", linewidth=2)

xs = linspace (2, 5, 4)
ys = (1.0/(1+25*xs**2))
s = UnivariateSpline(xs, ys, k=3)
xs = linspace (4, 5, 1000)
yi = s(xs)
plt.plot (xs, yi, color="r", linewidth=2)

#plt.axhline (linewidth=2, color='k')
#plt.axvline (linewidth=2, color='k')
plt.legend()
plt.axis ([xmin, xmax, ymin, ymax])
plt.show()
