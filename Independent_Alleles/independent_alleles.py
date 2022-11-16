#!/usr/bin/env python

from random import randrange

k = 5 # number of generations
N = 8 # find prob of N or more AaBb in population after k generations

def model(k):
    parent2 = ["A","a","B","b"]
    pop_genk = ["AaBb"]
    for i in range(k):
        parents = pop_genk
        pop_genk = []
        for j in parents:
            parent1 = list(j)
            child1 = parent1[randrange(2)] + parent2[randrange(2)] + parent1[randrange(2,4)] + parent2[randrange(2,4)]
            child2 = parent1[randrange(2)] + parent2[randrange(2)] + parent1[randrange(2,4)] + parent2[randrange(2,4)]
            pop_genk.append(child1)
            pop_genk.append(child2)
    return(pop_genk)

Aa_prop = []
for i in range(999999):
    pop = model(k)
    Aa = pop.count("AaBb") + pop.count("aABb") + pop.count("AabB") + pop.count("aAbB")
    if Aa >= N:
        Aa_prop.append(1)
    else:
        Aa_prop.append(0)
print(round(sum(Aa_prop)/len(Aa_prop),3))
