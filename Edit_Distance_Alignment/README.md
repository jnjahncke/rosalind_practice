# Reconstructing Edit Distance

In “Counting Point Mutations”, the calculation of Hamming distance gave us a clear way to model the sequence of point mutations transforming one genetic string into another. By simply writing one string directly over the other, we could count each mismatched symbol as a substitution.

However, in the calculation of edit distance (see “Edit Distance”), the two strings can have different lengths; thus, simply superimposing one string over the other does us no good when it comes to visualizing a sequence of edit operations transforming one string into the other. To remedy this, we will introduce a new symbol to serve as a placeholder representing an inserted or deleted symbol; furthermore, this placeholder will allow us to align two strings of differing lengths.

# Problem

An alignment of two strings s and t is defined by two strings s′ and t′ satisfying the following three conditions: 1. s′ and t′ must be formed from adding gap symbols "-" to each of s and t, respectively; as a result, s and t will form subsequences of s′ and t′. 2. s′ and t′ must have the same length. 3. Two gap symbols may not be aligned; that is, if s′[j] is a gap symbol, then t′[j] cannot be a gap symbol, and vice-versa.

We say that s′ and t′ augment s and t. Writing s′ directly over t′ so that symbols are aligned provides us with a scenario for transforming s into t. Mismatched symbols from s and t correspond to symbol substitutions; a gap symbol s′[j] aligned with a non-gap symbol t′[j] implies the insertion of this symbol into t; a gap symbol t′[j] aligned with a non-gap symbol s′[j] implies the deletion of this symbol from s.

Thus, an alignment represents a transformation of s into t via edit operations. We define the corresponding edit alignment score of s′ and t′ as dH(s′,t′) (Hamming distance is used because the gap symbol has been introduced for insertions and deletions). It follows that dE(s,t)=mins′,t′dH(s′,t′), where the minimum is taken over all alignments of s and t. We call such a minimum score alignment an optimal alignment (with respect to edit distance).

**Given**: Two protein strings s and t in FASTA format (with each string having length at most 1000 aa).

**Return**: The edit distance dE(s,t) followed by two augmented strings s′ and t′ representing an optimal alignment of s and t.

## Sample Dataset

```
>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN
```

## Sample Output

```
4
PRETTY--
PR-TTEIN
```
