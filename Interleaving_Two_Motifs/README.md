# Problem

A string s is a supersequence of another string t if s contains t as a subsequence.

A common supersequence of strings s and t is a string that serves as a supersequence of both s and t. For example, "GACCTAGGAACTC" serves as a common supersequence of "ACGTC" and "ATAT". A shortest common supersequence of s and t is a supersequence for which there does not exist a shorter common supersequence. Continuing our example, "ACGTACT" is a shortest common supersequence of "ACGTC" and "ATAT".

**Given**: Two DNA strings s and t.

**Return**: A shortest common supersequence of s and t. If multiple solutions exist, you may output any one.

## Sample Dataset

```
ATCTGAT
TGCATA
```

## Sample Output

```
ATGCATGAT
```
