import numpy
from numba import njit

@njit
def fchobotnice(x,y):
  return numpy.sin(x)*numpy.sin(y)

@njit
def dblquad(f,xmin,xmax,ymin,ymax,nmaxx,nmaxy):
  result=0
  hx=(xmax-xmin)/nmaxx
  hy=(ymax-ymin)/nmaxy
  t=0.5*(f(xmin,ymin)+f(xmax,ymin))
  for x in numpy.linspace(xmin+hx,xmax-hx,nmaxx-1): t+=f(x,ymin)
  result+=0.5*t
  for y in numpy.linspace(ymin+hy,ymax-hy,nmaxy-1):
    t=0.5*(f(xmin,y)+f(xmax,y))
    for x in numpy.linspace(xmin+hx,xmax-hx,nmaxx-1): t+=f(x,y)
    result+=t
  t=0.5*(f(xmin,ymax)+f(xmax,ymax))
  for x in numpy.linspace(xmin+hx,xmax-hx,nmaxx-1): t+=f(x,ymax)
  result+=0.5*t
  return result*hx*hy

nmaxx=1_000
nmaxy=1_000

print(dblquad(fchobotnice,0,numpy.pi,0,numpy.pi,nmaxx,nmaxy))