"""takes the genes from a single taxon and sorts them to individual gene files.

    USAGE: geneDistributor.py taxonFile.fasta

    ASSUMES: - That your current directory contains the individual gene files that you want to;
               sort your taxon specific files into
             - That the single-taxon input file to be sorted is in a species-specific directory;
               i.e., that Arth.fasta is in \SomeDirectory\Arabidopsis_thaliana\
"""

import sys
import os
from Bio import SeqIO


geneDir = os.getcwd()
taxonFile = sys.argv[1]

#! CHANGING THIS TO MAKE SURE IT CORRECTLY SORTS THEM IN MY CURRENT USE CASE
taxonName = os.path.basename(os.path.split(taxonFile)[-2])

#taxonName = taxonFile.split('_')[0]

for seq in SeqIO.parse(taxonFile, "fasta"):
    gene = seq.id
    seq.id = taxonName
    seq.description = ''  # for whatever reason the fasta format write includes this

    for file in os.listdir(geneDir):
        if os.path.splitext(file)[-1] == ".fasta":
            if('_' in file):
                geneName = file.split("_")[0]
            else:
                geneName = file.split('.')[0]
            if gene == geneName:
                with open(os.path.join(geneDir, file), 'a+') as outFile:
                    outFile.write(seq.format("fasta"))
print("Done!")
