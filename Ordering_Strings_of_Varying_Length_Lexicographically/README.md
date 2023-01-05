# Problem

Say that we have strings s=s<sub>1</sub>s<sub>2</sub>⋯s<sub>m</sub> and t=t<sub>1</sub>t<sub>2</sub>⋯t<sub>n</sub> with m<n. Consider the substring t′=t[1:m]. We have two cases:

If s=t′, then we set s<<sub>Lex</sub> t because s is shorter than t (e.g., APPLE<APPLET).
Otherwise, s≠t′. We define s<<sub>Lex</sub> t if s<<sub>Lex</sub> t′ and define s><sub>Lex</sub> t if s><sub>Lex</sub> t′ (e.g., APPLET<<sub>Lex</sub> ARTS because APPL<<sub>Lex</sub> ARTS).

**Given**: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).

**Return**: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)

## Sample Dataset

```
D N A
3
```

## Sample Output

```
D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA
```
