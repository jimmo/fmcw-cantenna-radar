#!/bin/sh
for file in main.py micropython-fourier/{dft,dftclass,window,polar,algorithms}.py; do
  echo $file
  cp $file /media/PYBFLASH
done
sync
