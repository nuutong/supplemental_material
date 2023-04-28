#!/bin/bash

cd ./statistics
/usr/bin/python3 ./extract.py
/usr/bin/python3 ./getData.py
/usr/bin/python3 ./mucSize.py
gnuplot pic1.plot
gnuplot pic2.plot
gnuplot pic3.plot
gnuplot pic4.plot
gnuplot pic5.plot
gnuplot pic6.plot
gnuplot pic7.plot
gnuplot pic8.plot
gnuplot pic8_2.plot

cd ..
[ -e result ] && rm -r result
mkdir result
mv ./statistics/*eps ./result/
mv ./statistics/*png ./result/
