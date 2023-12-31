import numpy
import scipy
from numba import njit
import matplotlib.pyplot as plt


#konstanty pro prepinani
class cEquation: EXP = 1; GON = 2; GUN = 3
class cSolver: EUL = 1; RK4 = 2; SCI = 3

#parametry dela
g = 9.81 #m/s^2
r = 16*0.0254 #m
S = numpy.pi*r**2 #m^2
rho = 1.2 #kg/m^3
Cd = 0.06
M = 929 #kg
K = 0.5*rho*S*Cd
KM = K/M
V0 = 788 #m/s
alpha0 = 32*numpy.pi/180 #rad elevace dela 
vzdalenost = 10000 #m
presnost = 100 #m

#prave strany
@njit
def fexp(t, y):
    return -y

@njit
def fgon(t, Y):
    (y1, y2) = Y
    return numpy.array((y2, -y1))

@njit
def fgun(t, Y):
    (x,z,vx,vz) = Y
    v = numpy.sqrt(vx**2 + vz**2)
    return numpy.array((vx, vz, -KM*v*vx, -KM*v*vz - g))

#Eulerova metoda
@njit
def Euler(func, y0, t):
    y = numpy.empty((len(t), len(y0)))
    y[0,:] = y0
    for n in range(len(t)-1):
        h = t[n+1] - t[n]
        y[n+1,:] = y[n,:] + h*func(t[n], y[n,:])
    return y

#Runge-Kuttova metoda 4. radu
@njit
def RungeKutta4(func, y0, t):
    y = numpy.empty((len(t), len(y0)))
    y[0,:] = y0
    for n in range(len(t)-1):
        h = t[n+1] - t[n]
        h2 = h*0.5
        k1 = func(t[n], y[n,:])
        k2 = func(t[n] + h2, y[n,:] + h2*k1)
        k3 = func(t[n] + h2, y[n,:] + h2*k2)
        k4 = func(t[n] + h, y[n,:] + h*k3)
        y[n+1,:] = y[n,:] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return y

#kresleni
def savefig(t, y, file):
    match Equation:
        case cEquation.EXP:
            fanal = lambda t: numpy.exp(-t) 
            plt.plot(t, fanal(t), t, y[:,0], 'o')
        case cEquation.GON:
            fanal1 = lambda t: numpy.sin(t)
            fanal2 = lambda t: numpy.cos(t)
            plt.plot(t, fanal1(t), t, y[:,0], 'o', t, fanal2(t), t, y[:,1], 'x')
        case cEquation.GUN:
            plt.plot(y[:,0], y[:,1])
    plt.savefig(file)
    plt.show()

#vyber ulohy

beta = 0
gama = alpha0
odch = (gama-beta)/8
alpha = beta
#print (alpha0*180/numpy.pi, odch*180/numpy.pi)
zasah = 0
alpha1 = 0
poc = 0

while (zasah == 0):

    pred = 0
    poc += 1

    for i in range(0,9,1):

        Equation = cEquation.GUN
        Solver = cSolver.SCI

        match Equation:
            case cEquation.EXP:
                func = fexp
                tmin = 0
                tmax = 2
                y0 = numpy.array([1])
                nmax = 20 if Solver == cSolver.EUL else 5
            case cEquation.GON:
                func = fgon
                tmin = 0
                tmax = 2*numpy.pi
                y0 = numpy.array([0,1])
                nmax = 100 if Solver == cSolver.EUL else 25
            case cEquation.GUN:
                func = fgun
                tmin = 0
                tmax = 75
                y0 = numpy.array([0,0,V0*numpy.cos(alpha),V0*numpy.sin(alpha)])
                nmax = 1000 if Solver == cSolver.EUL else 250

        #vytvoreni casove osy
        t = numpy.linspace(tmin, tmax, nmax+1)

        #reseni
        match Solver:
            case cSolver.EUL:
                y = Euler(func, y0, t)
            case cSolver.RK4:
                y = RungeKutta4(func, y0, t)
            case cSolver.SCI:
                y = scipy.integrate.odeint(func, y0, t, tfirst=True)

        n = 1
        while (y[n,1] >= 0):
            n += 1

        n -= 1

        #print(y[n,0]) #, y[n,1], t[n]) #vzdalenost, vyska, cas

        #print(alpha*180/numpy.pi) #uhel vystrelu

        if (y[n,0] >= vzdalenost - presnost and y[n,0] <= vzdalenost + presnost):
            print("-------------------------")
            print("Zasah nastal v: ", y[n,0], "m.")
            print("Uhel zasahu: ", alpha*180/numpy.pi, "°\n")
            zasah = y[n,0]
            break

        if (y[n,0] < vzdalenost - presnost):
            pred += 1
            #print("Pred: ", y[n,0], "m.", pred)

        alpha += odch

    print("Po ", poc,". vystrelech pocet gejziru pred lodi: ", pred, ".\n")
    alpha = (pred - 1) * odch + beta + alpha1
    alpha1 = alpha
    odch = odch/8

plt.plot(y[:n, 0], y[:n, 1])
plt.xlabel('Distance')
plt.ylabel('Height')
plt.title('Projectile motion that hits the target')
plt.grid(True)
plt.show()