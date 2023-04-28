#!/bin/bash

cd ./statistics
/usr/bin/python3 ./extract.py
/usr/bin/python3 ./getData.py
gnuplot pic1.plot
gnuplot pic2.plot
gnuplot pic3.plot
gnuplot pic4.plot

cd ..
[ -e result ] && rm -r result
mkdir result
mv ./statistics/*eps ./result/
