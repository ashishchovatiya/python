from pylab import *
x = linspace(-3, 3, 30)
y = x**2
plot(y, -sin(y),'b-')
plot(x, cos(x), 'r-')
plot(x, -sin(x), 'g--')
show()