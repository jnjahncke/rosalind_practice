#!/usr/bin/env python

import sys

with open(sys.argv[1],"r") as i:
    s,t = i.readlines()

hd = 0
for x,y in zip(s,t):
    if x != y:
        hd += 1

print(hd)
