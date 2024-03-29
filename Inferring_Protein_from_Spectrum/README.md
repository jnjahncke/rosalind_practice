# Introduction to Mass Spectrometry

In “Calculating Protein Mass”, we briefly mentioned an analytic chemical method called mass spectrometry, which aims to measure the mass-to-charge ratio of a particle or a molecule. In a mass spectrometer, a sample is vaporized (turned into gas), and then particles from the sample are ionized. The resulting ions are placed into an electromagnetic field, which separates them based on their charge and mass. The output of the mass spectrometer is a mass spectrum, or a plot of ions' possible mass-to-charge ratio values with the intensity (actual observed frequency) of ions having these mass-to-charge values.

For the moment, we will ignore charge and consider a list of the ions' monoisotopic masses as a simplified spectrum. Researchers do not possess cheap technology to go in and examine a protein one amino acid at a time (molecules are too submicroscopic). Instead, to determine a protein's structure, we will split several copies of the protein into smaller pieces, then weigh the resulting fragments. To do this, we assume that each cut (breakage point) occurs between two amino acids and that we can measure the mass of the resulting pieces for all possible cuts.

For example, the (unknown) protein "PRTEIN" can be cut in five possible ways: "P" and "RTEIN"; "PR" and "TEIN"; "PRT" and "EIN"; "PRTE" and "IN"; "PRTEI" and "N". We then can measure the masses of all fragments, including the entire string. The "left" end of a protein is called its N-terminus, and the ions corresponding to the protein string's prefixes (P, PR, PRT, PRTE, PRTEI) are called b-ions. The "right" end of the protein is called its C-terminus, and the ions corresponding to the string's suffixes (N, IN, EIN, TEIN, RTEIN) are called y-ions. The difference in the masses of two adjacent b-ions (or y-ions) gives the mass of one amino acid residue; for example, the difference between the masses of "PRT" and "PR" must be the mass of "T." By extension, knowing the masses of every b-ion of a protein allows us to deduce the protein's identity.

# Problem

The prefix spectrum of a weighted string is the collection of all its prefix weights.

**Given**: A list L of n (n≤100) positive real numbers.

**Return**: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.

## Sample Dataset

```
3524.8542
3710.9335
3841.974
3970.0326
4057.0646
```

## Sample Output

```
WMQS
```
