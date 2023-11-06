#nahodne C

from numba import jit
import random
import time
import sys

xmin = -2
xmax = +0.6
ymin = -1.2
ymax = +1.2
nmax = 100
MaxTime = 10
output = 0 # 0 jen statistika, 1 na obrazovku

@jit
def testMandelbrot(x, y):
    c = complex(x, y)
    z = 0.0 + 0.0j
    nstop = 0
    for n in range(nmax):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag > 4):
            nstop = n + 1
            break
    if nstop == 0:
        nstop = nmax + 1
    return nstop

random.seed()
cnt1 = 0
cnt2 = 0

ixmax = 3
iymax = 4

tic=time.time()
while time.time()-tic<MaxTime:
    x = xmin + (xmax - xmin) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    nstop = testMandelbrot(x, y)
    if nstop == nmax + 1:
        cnt1 += 1
    else:
        cnt2 += 1
    if output > 0: print('%9.5f %9.5f %5d' % (x, y, nstop))
#        for ix in range (ixmax + 1):
#            for iy in range (iymax + 1):
#                print(ix,iy,f'{abs(complex(ix,iy)):5.3f}',end='/')
#        print('stop')
result = 100 * cnt1 / cnt2
sys.stderr.write(f'Mandelbrot: {cnt1} / {cnt2} = {result:5.1f}%\n')
