#!/usr/bin/env python

import sys
from itertools import product 

# import alphabet and max length n
with open(sys.argv[1],"r") as data:
    alph, n = data.readlines()
alph = alph.split()
n = int(n)

# generate all words, unordered
lexicon = []
for i in range(1,n+1):
    for x in ["".join(x) for x in product(alph,repeat=i)]:
        lexicon.append(x)

# sort by alphabet and print to std out
lexicon = sorted(lexicon, key = lambda word: [alph.index(x) for x in word])
print(*lexicon, sep = "\n")
