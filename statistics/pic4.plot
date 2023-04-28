set autoscale fix
#set ytics rotate by 90
set key inside top left
set grid
set xlabel "Number of Formulas"
set ylabel "Time"
#set logscale y
set xrange [0:700]
set yrange [0:800000]
set terminal postscript eps color font 'Helvetica,20'
set output "pic4.eps"

plot "data4" using 1:2 title "Binary", "data4" using 1:3 title "BinaryUC" , "data4" using 1:4 title "Global" with linespoints

#epstool --copy --bbox pic6.eps --output bpic6.eps
#epstopdf --hires --outfile=pic4.pdf bpic4.eps

