from math import pi, sin

import matplotlib.pyplot as plt
import numpy as np

nmax = 1000 # pocet kroku
ax = 1 # amplituda x
ay = 2 # amplituda y
az = 1 # amplituda z
fx = 5 # frekvence x
fy = 3 # frekvence y
fz = 2 # frekvence z
phx = 0 # faze x
phy = 0 # faze y
phz = 0 # faze z
tmin = 0 # startovaci cas
tmax = 2*pi # koncovy cas
#filename = 'Lissajous.dat'
xdata=np.zeros(nmax+1)
ydata=np.zeros(nmax+1)
zdata=np.zeros(nmax+1)

#f = open(filename,'w')
for n in range(0,nmax+1):
    t = tmin + n*(tmax-tmin)/nmax
    x = ax*sin(fx*t+phx)
    y = ay*sin(fy*t+phy)
    z = az*sin(fz*t)+phz
    xdata[n]=x
    ydata[n]=y
    zdata[n]=z
    #print(f'{x:8.4f} {y:8.4f} {z:8.4f}', file=f)
ax = plt.figure().add_subplot(projection='3d')
ax.plot(xdata,ydata,zdata,label='Lissajous')
ax.legend()
plt.show()
#f.close()