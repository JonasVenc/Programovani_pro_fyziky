# gnuplot: multiplot and plot with boxes
fpol(x)=x**2; fgon(x)=sin(x); fpi(x)=(16*x-16)/(((x-2)*x*x+4)*x-4)
set terminal pngcairo enhanced crop font 'Sans,10' size 1024,800
set output 'integral3.png'
set samples 1000
set style fill solid
set multiplot
set size .35,.35
set origin 0,0
set xtics 0,.5; set ytics 0,1
set key left top
set title 'plocha zeleně: 1/3'
plot [0:1] fpol(x) with boxes linecolor 'green' title 'x^2'
set origin .33,0
set xtics 0,1; set ytics 0,1
set key right top
set title 'plocha zeleně: 2'
plot [0:pi] fgon(x) with boxes linecolor 'green' title 'sin x'
set origin .66,0
set xtics 0,.5; set ytics 0,4
set key right top
set title 'plocha zeleně: {/Symbol p}'
plot [0:1] fpi(x) with boxes linecolor 'green' title 'fpi(x)'
unset multiplot
set output
unset terminal