set autoscale fix
#set ytics rotate by 90
set key inside top left
set grid
set xlabel "NaiveMUC"
set ylabel "NaiveMUC + UC"
set logscale x
set logscale y
set xrange [-0.1:300000]
set yrange [-0.1:300000]
set terminal postscript eps color font 'Helvetica,20'
set output "pic2.eps"

plot "data2"  using 1:2 notitle, x notitle#, x= , y=

#with linespoints lw 3 ps 2
#, "bitPat_GF1_LTL4BA.dat"  using 1:2 title "LTL4BA" with linespoints lw 3 ps 2
