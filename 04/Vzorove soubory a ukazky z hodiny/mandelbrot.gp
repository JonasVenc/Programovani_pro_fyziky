# gnuplot: vykreslení Mandelbrotovy množiny
set palette defined \
  (0 'dark-blue',6 'dark-blue',30 'white',70 'gold',100 'brown',100.001 'black',101 'black')
set cbrange [0:101]
set terminal pngcairo size 1024,768
# set term pngcairo size 2048,1536
set output 'mandelbrot.png'
unset key
# unset xtics; unset ytics
plot [-2.:.6][-1.2:1.2] 'mn.dat' using 1:2:3 with dots palette
# plot 'mn.dat' using 1:2:3 with dots palette
set output
