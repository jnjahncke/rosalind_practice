#!/usr/bin/env python

import sys

# read in array
with open(sys.argv[1],"r") as a:
    a = a.read()
a = [float(f) for f in a.split(" ")]

def find_p(qq):
    # Hardy-Weinberg states: pp + 2pq + qq = 1
    #   where p = p(A) and q = p(a)
    #   qq is given in the dataset, solve for p using quadratic formula
    a = 1
    b = 2 * (qq**0.5)
    c = qq - 1
    p = (-b + ((b**2) - (4*a*c))**0.5) / (2*a)
    return(p)

def find_carrier(qq):
    p = find_p(qq)
    # given p, return 2pq + qq
    return(2*p*(qq**0.5) + qq)

out = [round(find_carrier(x),3) for x in a]
print(*out, sep = " ")
