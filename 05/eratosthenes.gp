# gnuplot: počet prvočísel (primes) a prvočíselných dvojčat (twin prime pairs) menších než N
xsize=800             # rozlišení obrázku ve směru x
ysize=800             # rozlišení obrázku ve směru y
xmax=1e9              # horní limit x-osy
ymax=xmax/20          # horní limit y-osy
binary=0              # typ vstupních souborů: 0 text, 1 binary
set title " p(N): počet prvočísel menších než N \n d(N): počet prvočíselných dvojčat menších než N "
set xlabel 'N'
set xtics xmax/5 format "%.0t.10^%1T"
set mxtics 4          # minor xtics
set ytics ymax/5 format "%.0t.10^%1T"
set mytics 4          # minor ytics
set key left top      # legenda vlevo nahoře
set size square       # čtvercový formát obrázku
set terminal pngcairo enhanced size xsize,ysize
set output 'eratosthenes.png'
if (!binary) {
plot [0:xmax][0:ymax] 'primes.dat' using 1:0 with lines title 'p(N)', \
                      'twins.dat' using 1:0 with lines title 'd(N)'
} else {
plot [0:xmax][0:ymax] 'primes.bin' binary format='%i' using 1:0 with lines title 'p(N)', \
                      'twins.bin' binary format='%i' using 1:0 with lines title 'd(N)'
}
set output