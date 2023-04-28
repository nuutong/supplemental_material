set autoscale fix
#set ytics rotate by 90
set key inside top left
set grid
set xlabel "Number of Formulas"
set ylabel "Time(ms)"
#set logscale y
set xrange [0:1292]
set yrange [0:66500970]
set terminal postscript eps color font 'Helvetica,20'
set output "pic5.pdf"

plot "data5" using 1:2 title "NaiveMUC", "data5" using 1:3 title "NaiveMUC+UC" , "data5" using 1:4 title "BinaryMUC" , "data5" using 1:5 title "BinaryMUC+UC" , "data5" using 1:6 title "virtual best" with linespoints

#epstool --copy --bbox pic6.eps --output bpic6.eps
#epstopdf --hires --outfile=pic4.pdf bpic4.eps
