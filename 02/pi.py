from math import *
import matplotlib.pyplot as plt
import numpy as np

format="%25s%20.15f"
print(format % ("pi (math.pi)= ", pi))

pi_zaklad = 4 * atan(1)
print(format % ("zakladni formule pi= ", pi_zaklad))

pi_machin = 4 * (4 * atan(1/5) - atan(1/239))
print(format % ("Machinova formule pi= ", pi_machin))

nmax = 100
pi_leibniz = 0
pi_Euler = 0
pi_wallis = 1
z = 1
xdata=np.arange(nmax+1)
ydata1=np.zeros(nmax+1)
ydata2=np.zeros(nmax+1)
ydata3=np.zeros(nmax+1)
ydata4=np.zeros(nmax+1)

for n in range(1, nmax+1):
    pi_leibniz = pi_leibniz + z / (2*n - 1)
    pi_Euler = pi_Euler + 1 / (n*n)
    pi_wallis = pi_wallis * (4*n*n)/(4*n*n-1)
    z = -z
    ydata1[n]=pi_leibniz*4
    ydata2[n]=sqrt(pi_Euler*6)
    ydata4[n]=pi_wallis*2
pi_leibniz = 4 * pi_leibniz
pi_Euler = sqrt(6 * pi_Euler)
pi_wallis = pi_wallis * 2
print(format % ("Leibnizova formule pi= ", pi_leibniz))
print(format % ("Eulerova formule pi= ", pi_Euler))
print(format % ("Wallisova formule pi= ", pi_wallis))

nmax=50
piViete=1
a=0
for n in range(1,nmax+1):
    a=sqrt(0.5+0.5*a)
    piViete=piViete*a
    ydata3[n]=2/piViete
piViete=2/piViete
print(format % ("Vieteova formule pi= ", piViete))

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(xdata,ydata1,color="tab:blue")
ax.plot(xdata,ydata2,color="tab:red")
ax.plot(xdata,ydata3,color="tab:green")
ax.plot(xdata,ydata4,color="tab:orange")
ax.set_xlim([0,nmax])
ax.set_ylim([3.0,3.3])
ax.set_title("Pi podle Leibnize, Eulerovy, Vieteovy a Wallisovy formule")
ax.set_xlabel('n')
ax.set_ylabel('pi')
plt.show()