set autoscale fix
#set ytics rotate by 90
set key inside top left at 50,95
set grid
set xlabel "Number of Formulas"
set ylabel "Size of MUC" off 10,0
set style fill transparent solid 0.1
set style circle radius graph 0.01
#set logscale x
#set logscale y
set xrange [0:1292]
set yrange [0:105]
set ytics ('0'0,'20'20,'40'40,'60'60,'80'80,'timeout(300ms)'100)
set arrow from 0,100 to 1292,100 nohead lc rgb '#90dda0dd' dt 1 lw 30
#set label "300s timeout" right at 1292,100 offset -1,-1 font 'Helvetica,14'
set terminal pngcairo color font 'Helvetica,14'
set output "pic7.png"

#plot "size_of_muc" using 1:4 title "BinaryMUC" lt 5 lc 'gold' , "size_of_muc" using 1:5 title "BinaryMUC+UC" lt 6 lc 'skyblue' ,"size_of_muc" using 1:2 title "NaiveMUC" lt 2 lc 'sea-green', "size_of_muc" using 1:3 title "NaiveMUC+UC" with points lt 1 lc 'dark-violet'

# plot  "size_of_muc" using 1:2 title "NaiveMUC" ,"size_of_muc" using 1:3 title "NaiveMUC+UC" with points 

plot "size_of_muc" using 1:4 title "BinaryMUC" with circles lc rgb 'gold' , "size_of_muc" using 1:5 title "BinaryMUC+UC" with circles lc rgb 'skyblue' ,"size_of_muc" using 1:2 title "NaiveMUC" with circles lc rgb 'sea-green', "size_of_muc" using 1:3 title "NaiveMUC+UC" with circles  lc rgb 'dark-violet'


#with linespoints lw 3 ps 2
#, "bitPat_GF1_LTL4BA.dat"  using 1:2 title "LTL4BA" with linespoints lw 3 ps 2
