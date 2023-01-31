#!/usr/bin/env python

import sys
from random import choice, shuffle 

def generate_seq(x, s):
    length = len(s)
    num_gc = int(length * x)
    num_at = length - num_gc
    seq = []
    for n in range(num_gc):
        seq.append(choice("GC"))
    for n in range(num_at):
        seq.append(choice("AT"))
    shuffle(seq)
    return("".join(seq))

def generate_N(N,x,s):
    genome = []
    for n in range(N):
        genome.append(generate_seq(x,s))
    return(genome)

with open(sys.argv[1],"r") as data:
    N,x = data.readline().rstrip().split()
    N,x = int(N), float(x)
    s = data.readline().rstrip()

is_in = 0
for i in range(int(sys.argv[2])):
    genome = generate_N(N,x,s)
    if s in genome:
        is_in += 1
print(is_in/1000)
