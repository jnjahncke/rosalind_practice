#!/usr/bin/env python

n = int(input("n: ")) # number of months
k = int(input("k: ")) # number of rabbit pairs born to each pair of rabbits each month

alive1g = 1 # number alive 1 generations ago
alive2g = 1 # number alive 2 generations ago

for months in range(3,n+1):
    offspring = k * alive2g
    total = alive1g + offspring
    alive2g = alive1g
    alive1g = total
print(total)

