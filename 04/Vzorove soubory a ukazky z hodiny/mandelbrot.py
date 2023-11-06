# Python: příprava bodů pro kreslení Mandelbrotovy množiny
# Balíčky Numba pro zrychlení, time pro měření času a sys pro stderr

from numba import njit
xmin=-2; xmax=0.6; ymin=-1.2; ymax=1.2  # obdélník v komplexní rovině
nmax=100                    # max. počet kroků testovací posloupnosti
MaxTime=10                  # doba výpočtu [sec]
output=1                    # 0: jen statistika, 1: data na obrazovku

@njit
def testMandelbrot(x,y):    # výpočet únikového indexu pro bod (x,y)
  c=complex(x,y)
  z=0+0j
  nstop=0
  for n in range(nmax):
    z=z*z+c
    if abs(z)>2:
    # if z.real**2+z.imag**2>4:
      nstop=n+1
      break                 # únikový index nalezen, jinak nmax+1
  return nstop if nstop>0 else nmax+1

import random               # pro náhodná čísla
import time                 # pro měření času
import sys                  # pro výpis na stderr
cnt1=0; cnt2=0              # čítače bodů
tic=time.time()             # startovací čas
while time.time()-tic<MaxTime:        # dokud je doba výpočtu menší než MaxTime
  x=xmin+(xmax-xmin)*random.random()  # náhodné číslo v <xmin,xmax)
  y=ymin+(ymax-ymin)*random.random()  # náhodné číslo v <ymin,ymax)
  nstop=testMandelbrot(x,y)           # únikový index
  if output>0: print('%8.5f%9.5f%5d'%(x,y,nstop))
  # print('{:8.5f} {:8.5f} {:4d}'.format(x,y,nstop))
  # print(f'{x:8.5f} {y:8.5f} {nstop:4d}')
  if nstop==nmax+1: cnt1+=1 # čítač bodů v Mandelbrotově množině 
  cnt2+=1                   # čítač všech prověřených bodů
sys.stderr.write('Mandelbrot: '+str(cnt1)+' / '+str(cnt2)+' = '+f'{100*cnt1/cnt2:5.1f}'+' %\n')
                            # výpis na stderr pomocí write(string), včetně \n pro odřádkování
