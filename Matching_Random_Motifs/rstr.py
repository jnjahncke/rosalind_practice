#!/usr/bin/env python

import sys

with open(sys.argv[1],"r") as data:
    N,x = data.readline().rstrip().split()
    N,x = int(N), float(x)
    s = data.readline().rstrip()

length = len(s)
num_gc = length * x
prob_gc = num_gc/length
prob_at = 1 - prob_gc

prob1 = 1
for NT in s:
    if NT == "A" or NT == "T":
        prob1 *= prob_at/2
    elif NT == "G" or NT == "C":
        prob1 *= prob_gc/2

# probability of it never happening 
# is the complement of it happening once
probC = 1-prob 

# probability of it happening one or more times
# is the complement of it never happening
print(f'{1-(probC**N):.3}')
