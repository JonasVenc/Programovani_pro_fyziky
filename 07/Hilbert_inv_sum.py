import numpy
format='%s%20.15f%20.15f%20.15f'

N = 5

for i in range(N):
    nmax = i+1

    A = numpy.full((nmax,nmax),1.0/nmax)
    numpy.fill_diagonal(A,1.0)
    b = numpy.ones(nmax)

    #print(format%('b= ', b[0], b[1], b[2]))

    x = numpy.linalg.solve(A,b)

    #print(format%('x= ', x[0], x[1], x[2]))
    b = A@x

    #print(format%('b= ', b[0], b[1], b[2]))

    A_inv = numpy.linalg.solve(A, numpy.eye(nmax))

    print(A_inv, '\n')

    #zkouška
    result = A @ A_inv
    print(result)

    sum_A_inv = numpy.sum(A_inv)
    print("Suma všch prvků inverzní matice:", sum_A_inv)