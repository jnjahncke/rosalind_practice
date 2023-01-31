#!/usr/bin/env python

import sys

with open(sys.argv[1],"r") as data:
    n = int(data.readline().strip())

print(2**n % 1000000)
