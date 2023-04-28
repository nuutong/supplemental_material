set autoscale fix
set grid
set ylabel "BinaryMUC(ms)"
set xlabel "NaiveMUC(ms)"
set logscale x 
set xtics format '10^{%T}'
set logscale y 
set ytics format '10^{%T}'
set xrange [0.1:1000000]
set yrange [0.1:1000000]
set style fill transparent solid 0.4
set style circle radius graph 0.01
set arrow from 0.1,300000 to 1000000,300000 nohead lc rgb 'red' dt 2 lw 5 
set label "300s timeout" right at 0.1,300000 offset 15, 0.6
set arrow from 300000,0.1 to 300000,1000000 nohead lc rgb 'red' dt 2 lw 5
set label "300s timeout" right at 300000,0.1 offset -0.8, 1 
#set terminal postscript eps color font 'Helvetica,20'
set terminal pngcairo color font 'Helvetica,14'
set output "pic1.png"

plot "data1"  using 2:1 notitle with circles, x notitle 
#with linespoints lw 3 ps 2
#, "bitPat_GF1_LTL4BA.dat"  using 1:2 title "LTL4BA" with linespoints lw 3 ps 2
