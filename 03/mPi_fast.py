#modul pro vypocet cisla Pi
#demonstrace proceduralniho stylu

from math import pi, atan, sqrt
from numba import njit

@njit
def piMachin():
    return 4*(4*atan(1/5)-atan(1/239))

@njit
def piLeibniz(nmax):
    pi_leibniz = 0
    z = 1
    for n in range(1, nmax+1):
        pi_leibniz += z / (2*n - 1)
        z = -z
    return 4 * pi_leibniz

@njit
def piEuler(nmax):
    pi_Euler = 0
    for n in range(nmax, 0, -1):
        pi_Euler += + 1 / (n*n)
    return sqrt(6 * pi_Euler)

@njit
def piViete(nmax):
    a=0
    piViete=1
    for n in range (1, nmax+1):
        a=sqrt(0.5+0.5*a)
        piViete=piViete*a
    return 2/piViete

@njit
def piRamanujan(nmax):
    a=1
    piRamanujan=a*1103
    for n in range(1,nmax+1):
        a=a*(4*n-3)*(4*n-2)*(4*n-1)*(4*n)/(396*2)**4
        piRamanujan += a*(1103+26390*n)
    return 1/(piRamanujan*sqrt(8)/9801)