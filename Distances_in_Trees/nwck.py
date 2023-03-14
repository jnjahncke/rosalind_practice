#!/usr/bin/env python

import sys
from Bio import Phylo
from io import StringIO

# import trees
with open(sys.argv[1],"r") as r:
    items = [x.split("\n") for x in r.read().strip().split("\n\n")]

# parse data
trees = {}
for i in items:
    tree, pair = i[0], i[1].split()
    trees[tree] = {"x":pair[0], "y":pair[1]}

# calculate distances
distances = []
for tree in trees:
    x,y = trees[tree]["x"], trees[tree]["y"]
    tree_read = Phylo.read(StringIO(tree), "newick")
    clades = tree_read.find_clades()
    for clade in clades:
        clade.branch_length = 1
    distances.append(tree_read.distance(x,y))

print(*distances, sep = " ")
