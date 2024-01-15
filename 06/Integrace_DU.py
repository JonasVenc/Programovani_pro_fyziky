import numpy as np
from numba import njit

r = 1
nmax = 10000

@njit
def pulkruh(x):
    return np.sqrt(r**2 -  x**2)

@njit
def quad_for(f, a, b, nmax):
    result = (f(a) + f(b))*0.5
    h = (b - a)/nmax
    x = a
    for n in range(1, nmax):
        x += h
        result += f(x)
    return result*h

@njit
def polokoule(x, y):
    vysledek = r**2 - x**2 - y**2
    return np.sqrt(vysledek) if vysledek >= 0 else 0

@njit
def quad_triple (f, a, b, c, d, nmax):
    result = 0
    h = (b - a)/nmax
    j = (d - c)/nmax
    x = a
    for i in range(1, nmax):
        x += h
        y = c
        for k in range(1, nmax):
            y += j
            result += f(x, y)
    return result*h*j

print(2*quad_for(pulkruh, -1, 1, nmax))
print(3/2*quad_triple(polokoule, -1, 1, -1, 1, nmax))