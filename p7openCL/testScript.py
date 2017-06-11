#Testing Script for CS475 Project 7b
#Jesse Thoren
#Description: Compiles and runs project7.cpp (RABBIT ONLY)

import os
cmd = "g++ -o project7 project7.cpp ./libOpenCL.so -lm -fopenmp"
os.system(cmd)
cmd = "./project7"
os.system(cmd)
cmd = "rm -f project7"
os.system(cmd)
