import sympy

def testSympy():
    x = sympy.Symbol('x')
    fpol = x*x
    fgon = sympy.sin(x)
    frat = (16*x-16)/(x**4-2*x**3+4*x-4)
    print(sympy.integrate(fpol, x), '...', sympy.integrate(fpol, (x, 0, 1)))
    print(sympy.integrate(fgon, x), '...', sympy.integrate(fgon, (x, 0, sympy.pi)))
    print(sympy.integrate(frat, x), '...', sympy.integrate(frat, (x, 0, 1)))
    return None

testSympy()