import numpy
format='%s%20.15f%20.15f%20.15f'

nmax = 10_000

A = numpy.full((nmax,nmax),1.0/nmax)
numpy.fill_diagonal(A,1.0)
b = numpy.ones(nmax)

print(format%('b= ', b[0], b[1], b[2]))

x = numpy.linalg.solve(A,b)

print(format%('x= ', x[0], x[1], x[2]))
b = A@x

print(format%('b= ', b[0], b[1], b[2]))

print(format%('chyby= ', sum(abs(b-1.0)), numpy.sqrt(sum((b-1.0)**2)), max(abs(b-1.0))))
