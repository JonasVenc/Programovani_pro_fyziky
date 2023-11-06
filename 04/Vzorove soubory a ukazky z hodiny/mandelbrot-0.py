# Python: příprava bodů pro kreslení Mandelbrotovy množiny

import random
xmin=-2; xmax=0.6; ymin=-1.2; ymax=1.2  # obdélník v komplexní rovině
nmax=100                     # max. počet kroků testovací posloupnosti
random.seed()
while True:
  x=random.random()          # náhodné číslo z intervalu <0,1)
  y=random.random()
  x=xmin+(xmax-xmin)*x       # přepočet na <xmin,xmax)
  y=ymin+(ymax-ymin)*y       # přepočet na <ymin,ymax)
  c=complex(x,y)             # náhodný bod v obdélníku
  z=0+0j                     # výchozí z_0
  nstop=0
  for n in range(nmax):
    z=z*z+c
    if abs(z)>2:
      nstop=n+1              # únikový index nalezen
      break
  if nstop==0: nstop=nmax+1  # únikový index nenalezen, volíme nmax+1
  print('%8.5f%9.5f%5d'%(x,y,nstop))
  # print('{:8.5f} {:8.5f} {:4d}'.format(x,y,nstop))
  # print(f'{x:8.5f} {y:8.5f} {nstop:4d}')
