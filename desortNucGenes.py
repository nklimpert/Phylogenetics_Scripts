"""This script takes in a FASTA file of all the nuclear genes assembled for a single taxon and redistributes them to files in the current working directory."""

import sys
from Bio import SeqIO


# Takes in files of genes from command line

taxonFiles = sys.argv[1:]  # this allows for multiple files to be combined

# loop through all the sequences in the taxon file
for taxonFile in taxonFiles:
    for seq in SeqIO.parse(open(taxonFile), 'fasta'):
        name, num = seq.id[:-3], seq.id[-3:]  # the last three characters are the gene number, so everything before that is the name
        with open(num+".FNA", 'a+') as geneFile:  # append to the gene files
                seq.id = name
                geneFile.write(seq.format("fasta"))
