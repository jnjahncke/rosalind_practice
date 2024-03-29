# Ions Galore

In “Inferring Protein from Spectrum”, we inferred a protein string from a list of b-ions. In practice, biologists have no way of distinguishing between b-ions and y-ions in the simplified spectrum of a peptide. However, we will often possess a pair of masses in the spectrum corresponding to a single cut. The two corresponding ions complement each other: for example, mass("PR") + mass("TEIN") = mass("PRTEIN"). As a result, we can easily infer the mass of a b-ion from its complementary y-ion and vice versa, as long as we already know the parent mass, i.e., the mass of the entire peptide.

The theoretical simplified spectrum for a protein P of length n is constructed as follows: form all possible cuts, then compute the mass of the b-ion and the y-ion at each cut. Duplicate masses are allowed. You might guess how we could modify “Inferring Protein from Spectrum” to infer a peptide from its theoretical simplified spectrum; here we consider a slightly modified form of this problem in which we attempt to identify the interior region of a peptide given only b-ions and y-ions that are cut within this region. As a result, we will have constant masses at the beginning and end of the peptide that will be present in the mass of every b-ion and y-ion, respectively.

# Problem

Say that we have a string s containing t as an internal substring, so that there exist nonempty substrings s1 and s2 of s such that s can be written as s1ts2. A t-prefix contains all of s1 and none of s2; likewise, a t-suffix contains all of s2 and none of s1.

**Given**: A list L containing 2n+3 positive real numbers (n≤100). The first number in L is the parent mass of a peptide P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

**Return**: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions exist, you may output any one.

## Sample Dataset

```
1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091
```

## Sample Output

```
KEKEP
```
