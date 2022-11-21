#!/usr/bin/env python

import sys
from copy import deepcopy

inputfile = sys.argv[1]

with open(inputfile,"r") as raw:
    alphabet, n = raw.readlines()

alphabet = alphabet.rstrip().split()
n = int(n)

strings = []
for i in range(len(alphabet)):
    menu = deepcopy(alphabet)
    while len(menu) > 0:
        current = alphabet[i]
        while len(current) < n:
            current += menu[0]
            menu.pop(0)
        strings.append(current)    
print(*strings, sep = "\n")
