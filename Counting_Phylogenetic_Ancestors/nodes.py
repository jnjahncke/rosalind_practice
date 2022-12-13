#!/usr/bin/env python

import sys

with open(sys.argv[1],"r") as num:
    n = int(num.readline().strip())

print(n-2)
