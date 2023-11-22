import numpy
from numba import njit
import time
import math

@njit
def fpol(x):
    return x*x

@njit
def fgon(x):
    return numpy.sin(x)

@njit
def frat(x):
    return (16*x-16)/(((x-2)*x*x+4)*x-4)

@njit
def quad_for (f, a, b, nmax):
    result = 0.5*(f(a)+f(b))
    h = (b-a)/nmax
    x = a
#    for n in range(1, nmax):
#        x += h
#        x = a+n*h
#        result += f(x)
#    for x in numpy.arange(a+h, b, h):
#        result += f(x)
    for x in numpy.linspace(a+h, b-h, nmax-1):
        result += f(x)
    return result*h

#@njit
def quad_fsum (f, a, b, nmax):
    h = (b-a)/nmax
    x = numpy.linspace(a, b, nmax+1)
#    result = 0.5*(f(a)+f(b)) + math.fsum(f(x[1:nmax]))
    result = 0.5*(f(a)+f(b)) + sum(f(x[1:nmax]))
    return result*h

#@njit
def quad_eps (f, a, b, namx, eps):
    n = 1
    Lnew = quad_fsum(f, a, b, n)
    while True:
        Lond = Lnew
        n *= 2
        if n > nmax:
            break
        Lnew = quad_fsum(f, a, b, n)
        if abs(Lnew-Lond) < eps*abs(Lnew):
            break
        return Lnew

nmax = 100_000_000
eps = 1.0E-14
tic = time.time()
print(quad_eps(fpol, 0, 1, nmax, eps))
print(quad_eps(fgon, 0, numpy.pi, nmax, eps))
print(quad_eps(frat, 0, 1, nmax, eps))
tac = time.time()
print('Doba behu: ', f'{tac-tic:0.2f} s')