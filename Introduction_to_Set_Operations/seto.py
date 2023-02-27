#!/usr/bin/env python

import sys
from re import finditer

def extract_set(line):

    set_out = []
    for match in finditer(r"(\d*)[,|}]", line):
        set_out.append(int(match.group(1)))

    return set(set_out)

with open(sys.argv[1],"r") as data:
    n = int(data.readline().strip())
    A_raw = data.readline().strip()
    B_raw = data.readline().strip()

A = extract_set(A_raw)
B = extract_set(B_raw)
C = set([x for x in range(1,n+1)])

# A union B
print(A|B)

# intersection of A and B
print(A&B)

# A - B
print(A-B)

# B - A
print(B-A)

# A complement
print(C-A)

# B complement
print(C-B)
