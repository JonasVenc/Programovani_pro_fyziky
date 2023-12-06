import numpy
import scipy
format='%s%20.15f%20.15f%20.15f'

N = 20

for i in range(N):
    nmax = i+1

    A = scipy.linalg.hilbert(nmax)
    
    #b = numpy.ones(nmax)

    #print(format%('b= ', b[0], b[1], b[2]))

    #x = numpy.linalg.solve(A,b)

    #print(format%('x= ', x[0], x[1], x[2]))
    #b = A@x

    #print(format%('b= ', b[0], b[1], b[2]))

    A_inv = numpy.linalg.solve(A, numpy.eye(nmax))

    #print(A_inv, '\n')

    #zkouška
    result = A @ A_inv
    print(result)

    sum_A_inv = numpy.sum(A_inv)
    print("Suma všech prvků inverzní matice:", sum_A_inv)