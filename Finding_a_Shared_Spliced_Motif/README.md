# Problem

A string u is a common subsequence of strings s and t if the symbols of u appear in order as a subsequence of both s and t. For example, "ACTG" is a common subsequence of "AACCTTGG" and "ACACTGTGA".

Analogously to the definition of longest common substring, u is a longest common subsequence of s and t if there does not exist a longer common subsequence of the two strings. Continuing our above example, "ACCTTG" is a longest common subsequence of "AACCTTGG" and "ACACTGTGA", as is "AACTGG".

**Given**: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.

**Return**: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)

## Sample Dataset

```
>Rosalind_23
AACCTTGG
>Rosalind_64
ACACTGTGA
```

## Sample Output

```
AACTGG
```
