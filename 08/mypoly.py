# modul pro interpolaci
import numpy
from numba import njit

@njit
def polyval(p, x):
    """
    Evaluate a polynomial at given points.

    Parameters:
    p (numpy.ndarray): Coefficients of the polynomial in descending order.
    x (numpy.ndarray): Points at which to evaluate the polynomial.

    Returns:
    numpy.ndarray: Values of the polynomial evaluated at the given points.
    """
    result = numpy.empty(x.size)
    for i in range(x.size):
        result[i] = p[0]
        for j in range(1, p.size):
            result[i] = result[i] * x[i] + p[j]
    return result

@njit
def polyfit2(x, y):
    """
    Fit a polynomial to given data points.

    Parameters:
    x (numpy.ndarray): x-coordinates of the data points.
    y (numpy.ndarray): y-coordinates of the data points.

    Returns:
    numpy.ndarray: Coefficients of the fitted polynomial in descending order.
    """
    n = x.size - 1
    V = numpy.empty((n + 1, n + 1))
    for i in range(n + 1):
        V[i,0] = 1
        for j in range(1, n + 1):
            V[i,j] = V[i,j - 1] * x[i]
    c = numpy.linalg.solve(V, y)
    return c[-1::-1]

@njit
def polyfit(x, y, deg):
    m = deg
    n = x.size - 1
    if m==n:
        return polyfit2(x, y)
    xx = numpy.ones(n+1)
    sumx = numpy.ones(2*m+1)
    sumy = numpy.empty(m+1)
    for i in range(2*m+1):
        sumx[i] = sum(xx)
        if i<=m:
            sumy[i] = sum(xx*y)
        xx *= x
        
    G = numpy.empty((m+1, m+1))
    for i in range(m+1):
        for j in range(m+1):
            G[i,j] = sumx[i+j]
    c = numpy.linalg.solve(G, sumy)
    return c[-1::-1]