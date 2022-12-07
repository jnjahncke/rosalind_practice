#!/usr/bin/env python

import sys

# import data
i = 0
adjacency = []
with open(sys.argv[1],"r") as data:
    for line in data:
        i += 1
        line = line.rstrip()
        if i == 1:
            n = int(line)
        else:
            a,b = line.split()
            adjacency.append([int(a),int(b)])

print(n-1-len(adjacency))
