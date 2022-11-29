#!/usr/bin/env python

import sys
from math import log

inputfile = sys.argv[1]

with open(inputfile,"r") as inputfile:
    seq = inputfile.readline().rstrip()
    A = [float(x) for x in inputfile.readline().split()]

# given a GC content, calculate the probability of a given sequence
def prob_seq(seq, GC):
    probGC = GC/2
    probAT = (1-GC)/2
    
    prob = 1
    for NT in seq:
        if NT == "G" or NT == "C":
            prob *= probGC
        elif NT == "A" or NT == "T":
            prob *= probAT
    
    return(round(log(prob,10),3)) # log base 10, round to 3 digits

# iterate through A, calculate probs for each given GC in A
B = [prob_seq(seq, x) for x in A]
print(*B, sep = " ")
