! Fortran: příprava bodů pro kreslení Mandelbrotovy množiny
! Modul mTicToc pro měření času v matlabovském stylu tic-toc

include 'mTicToc.f90'           ! vložení obsahu souboru s modulem mTicToc

program Mandelbrot
use mTicToc
implicit none
real :: xmin=-2,xmax=0.6,ymin=-1.2,ymax=1.2 ! obdélník v komplexní rovině
integer :: nmax=100             ! max. počet kroků testovací posloupnosti
real :: MaxTime=10              ! doba výpočtu [sec]
integer:: output=1              ! 0: jen statistika, 1: data na obrazovku
real :: x,y
integer :: nstop,cnt1,cnt2

cnt1=0; cnt2=0                  ! čítače bodů
call tic()                      ! uložení startovacího času
do while (toc()<MaxTime)        ! dokud je doba výpočtu menší než MaxTime
  call random_number(x)         ! náhodné číslo v <0,1)
  call random_number(y)
  x=xmin+(xmax-xmin)*x          ! přepočet do <xmin,xmax)
  y=ymin+(ymax-ymin)*y
  nstop=testMandelbrot(x,y)     ! únikový index
  if (output>0) print '(f8.5,f9.5,i5)',x,y,nstop
  if (nstop==nmax+1) cnt1=cnt1+1 ! čítač bodů v Mandelbrotově množině
  cnt2=cnt2+1                   ! čítač všech prověřených bodů
enddo
write (0,'(a,i0,a,i0,a,f5.1,a)') 'Mandelbrot: ',cnt1,' / ',cnt2,' = ',100.*cnt1/cnt2,' %'
                                ! výpis statistiky na stderr
contains

! Výpočet únikového indexu pro bod (x,y)
integer function testMandelbrot(x,y) result (nstop)
real x,y
complex c,z
integer n
c=cmplx(x,y)
z=(0.,0.)
nstop=0
do n=1,nmax
  z=z*z+c
  if (abs(z)>2) then 
  ! if (z%Re**2+z%Im**2>4) then
    nstop=n
    exit                        ! únikový index nalezen
  endif
enddo
if (nstop==0) nstop=nmax+1      ! únikový index nenalezen, vrátí se nmax+1
end function

end program
