#!/usr/bin/env python

import requests
import re
import sys


inputfile = sys.argv[1]

# get fasta files

# sample url:
# https://rest.uniprot.org/uniprotkb/P20840?query=yeast&format=fasta

url_pre = 'https://rest.uniprot.org/uniprotkb/'
url_mid = "?query="
url_suf = 'format=fasta'

seq_dict = {}
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line.find("_") > 0:
            for found in re.finditer(r"(\w+)_\w+_(\w+)",line):
                uniprot_id = found.group(1)
                species = found.group(2)
            url = url_pre + uniprot_id + url_mid + species + "&" + url_suf
        else:
            uniprot_id = line
            url = url_pre + uniprot_id + "?" + url_suf

        seq_dict[line] = ""
        fasta = requests.get(url).text # get entry from uniprot
        fasta = fasta.split("\n")[1:]
        seq_dict[line] += "".join(fasta)

# find motif

def find_motif(seq):
    matches = []
    # need to use (?=(regex)) to find overlapping matches
    for found in re.finditer(r"(?=(N[^P][ST][^P]))",seq):
        matches.append(found.start(1)+1)
    return(matches)

for seq in seq_dict:
    matches = find_motif(seq_dict[seq])
    if len(matches) > 0:
        print(seq)
        out = ""
        for match in matches:
            out += str(match) + " "
        print(out)
