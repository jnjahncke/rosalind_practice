#!/usr/bin/env python

import sys

with open(sys.argv[1],"r") as data:
    n = int(data.readline().strip())
    A_raw = data.readline().strip()
    B_raw = data.readline().strip()

