set autoscale fix
#set ytics rotate by 90
set key inside top left
set grid
set xlabel "Number of Formulas"
set ylabel "Time(ms)"
#set logscale y
set xrange [0:1292]
set yrange [0:25523205]
set terminal postscript eps color font 'Helvetica,20'
set output "pic8_2.eps"

plot "data7_2" using 1:2 title "AALTAF-UC", "data7_2" using 1:3 title "BinaryMUC+UC" with linespoints

#epstool --copy --bbox pic6.eps --output bpic6.eps
#epstopdf --hires --outfile=pic4.pdf bpic4.eps
