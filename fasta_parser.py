#!/usr/env/python

def fasta_parser(filename):
    seq_dict = {}
    with open(filename,"r") as fasta:
        for line in fasta:
            line = line.rstrip()
            if line[0] == ">":
                seq = line[1:]
                seq_dict[seq] = ""
            else:
                seq_dict[seq] += line
    return(seq_dict)
