#!/usr/bin/env python

import sys

def motif(seq, subseq):
    result = seq.find(subseq)
    if result == 0:
        return True
    else:
        return False

def memoize(func):
    cache = {}
    def decorated_function(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return decorated_function

motif = memoize(motif)

# import sequence
seq = ""
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] != ">":
            seq += line

# build failure array
array = [0]
for i in range(1,len(seq)):
    longest = 0
    for j in range(i+1):
        newseq = seq[:i]
        subseq = seq[i-j:i+1]
        if subseq[0] == seq[0]:
            find = motif(newseq, subseq)
            if find == True:
                length = len(subseq) 
                if length > longest:
                    longest = length
    array.append(longest)
print(*array, sep = " ")
