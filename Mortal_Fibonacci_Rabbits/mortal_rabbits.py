#!/usr/bin/env python

n = int(input("n: ")) # number of months
m = int(input("m: ")) # lifespan of rabbits, in months

# need to keep track of m months
alive_m = [0] * m
offspring_m = [0] * m
died_m = [0] * m

alive_m[-1], alive_m[-2] = 1, 1
offspring_m[-2] = 1

# total alive = (# alive last month) - (# died) + (# new)
for month in range(3,n+1):
    if month <= m:
        died = 0
    else:
        died = offspring_m[0]
    alive_last = alive_m[-1]
    new = alive_m[-2] - died_m[-1] # alive two months ago - died last month
    total = alive_last - died + new
    # update lists
    alive_m, offspring_m, died_m = alive_m[1:], offspring_m[1:], died_m[1:]
    alive_m.append(total)
    offspring_m.append(new)
    died_m.append(died)
print(total)
