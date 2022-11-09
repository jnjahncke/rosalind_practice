#!/usr/bin/env python

k = 27 # number homozygous dominant
m = 27 # number heterozygous
n = 17 # number homozygous recessive
total = k + m + n
total1 = total - 1

# Calculate the probability that two randomly selected matings will produce an individual with a dominant allele

kk = (k/total) * ((k-1)/total1) * 1
km = (k/total) * (m/total1) * 1
kn = (k/total) * (n/total1) * 1
mk = (m/total) * (k/total1) * 1
mm = (m/total) * ((m-1)/total1) * 0.75
mn = (m/total) * (n/total1) * 0.5
nk = (n/total) * (k/total1) * 1
nm = (n/total) * (m/total1) * 0.5
nn = (n/total) * ((n-1)/total1) * 0

prob = kk + km + kn + mk + mm + mn + nk + nm + nn

print(prob)
