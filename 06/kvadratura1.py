import numpy
import scipy

def fpol(x):
    return x*x

def fgon(x):
    return numpy.sin(x)

def frat(x):
#    return (16*x-16)/(x**4-2*x**3+4*x-4)
    return (16*x-16)/(((x-2)*x*x+4)*x-4)

def quad_scipy (f, a, b):
    return scipy.integrate.quad(f, a, b)

print (quad_scipy(fpol, 0, 1))
print (quad_scipy(fgon, 0, numpy.pi))
print (quad_scipy(frat, 0, 1))