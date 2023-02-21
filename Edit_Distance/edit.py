#!/usr/bin/env python

import sys


seq_dict = {}
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] == ">":
            seq = line[1:]
            seq_dict[seq] = ""
        else:
            seq_dict[seq] += line

s,t = seq_dict.values()
M = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

for i in range(1,len(s) + 1):
    M[i][0] = i
for i in range(1, len(t) + 1):
    M[0][i] = i
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i-1] == t[j-1]:
            cost = 0
        else:
            cost = 1
        M[i][j] = min(M[i-1][j] + 1, M[i][j-1] + 1, M[i-1][j-1] + cost)
print(*M, sep = "\n")
print()
print(M[len(s)][len(t)])
