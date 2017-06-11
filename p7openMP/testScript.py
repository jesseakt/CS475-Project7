#Testing Script for CS475 Project 7b
#Jesse Thoren
#Description: Compiles and runs project7.cpp

import os
for NUMT in [1, 16]:
    cmd = "g++ -o project7 project7.cpp -lm -fopenmp -DNUMT=%d" % NUMT
    os.system(cmd)
    cmd = "./project7"
    os.system(cmd)
cmd = "rm -f project7"
os.system(cmd)
