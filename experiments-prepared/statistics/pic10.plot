set autoscale fix
#set ytics rotate by 90
set key inside top left at 50,95
set grid
set xlabel "Number of Formulas"
set ylabel "Jaccard index between NaiveMUC+UC and BinaryMUC+UC" font 'Helvetica,12'
set style fill transparent solid 0.1
set style circle radius graph 0.01
#set logscale x
#set logscale y
set xrange [0:1292]
set yrange [-0.02:1.02]
# set ytics ('0'0,'20'20,'40'40,'60'60,'80'80,'timeout(300ms)'100)
# set arrow from 0,100 to 1292,100 nohead lc rgb '#90dda0dd' dt 1 lw 30

set terminal pngcairo color font 'Helvetica,14'
set output "pic10.png"


plot "overlap_naiveucmuc_binaryucmuc" using 1:2 with circles  lc rgb 'dark-violet'


#with linespoints lw 3 ps 2
#, "bitPat_GF1_LTL4BA.dat"  using 1:2 title "LTL4BA" with linespoints lw 3 ps 2
