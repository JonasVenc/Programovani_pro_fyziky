import numpy
import mypoly
import matplotlib.pyplot as plt

f_in = 'C:\\Users\\jonas\\OneDrive\\Dokumenty\\GitHub\\Programovani_pro_fyziky\\08\\data.txt'
f_out = 'C:\\Users\\jonas\\OneDrive\\Dokumenty\\GitHub\\Programovani_pro_fyziky\\08\\fit.txt'

with open(f_in, 'r') as f:
    n = 0
    for line in f:
        n += 1
n -= 1

x = numpy.empty(n+1)
y = numpy.empty(n+1)

with open(f_in, 'r') as f:
    nn = 0
    for line in f:
        (x[nn], y[nn]) = line.split()
        nn += 1

p = mypoly.polyfit2(x, y)
p_0 = mypoly.polyfit(x, y, 0)
p_1 = mypoly.polyfit(x, y, 1)
p_2 = mypoly.polyfit(x, y, 2)
p_3 = mypoly.polyfit(x, y, 3)

#print(x)
#print(y)
#p = mypoly.polyfit2(x, y)
#print(p)

nmax = 100*n
xmin = x[0] - 1
xmax = x[n] + 1

xi = numpy.linspace(xmin, xmax, nmax+1)
yi = mypoly.polyval(p, xi)
yi_0 = mypoly.polyval(p_0, xi)
yi_1 = mypoly.polyval(p_1, xi)
yi_2 = mypoly.polyval(p_2, xi)
yi_3 = mypoly.polyval(p_3, xi)

#print do souboru pouze první funkce
with open(f_out, 'w') as f:
    for nn in range(nmax+1):
        print(f'{xi[nn]:10.6f} {yi[nn]:10.6f}', file=f )

plt.plot(x, y, 'o', label='data')
plt.plot(xi, yi, label='fit_přesný')
plt.plot(xi, yi_0, label='fit_0')
plt.plot(xi, yi_1, label='fit_1')
plt.plot(xi, yi_2, label='fit_2')
plt.plot(xi, yi_3, label='fit_3')

max_y = numpy.max(y)
min_y = numpy.min(y)

plt.ylim(min_y-2, max_y+0.1*max_y)
plt.title("Fit pomocí funkcí s různou degenerací")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()