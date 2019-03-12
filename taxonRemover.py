'''removes the taxa in the provided .txt file from the alignments in the current directory

    USAGE: taxonRemover.py taxa.txt
'''


import os
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
import sys

taxonFile = sys.argv[1]
taxa = []


with open(taxonFile, 'r') as taxFile:
    taxa = taxFile.read().split('\n')

for file in os.listdir():
    geneAlignment = AlignIO.read(file, 'fasta')

    strippedAlignment = MultipleSeqAlignment([taxon for taxon in geneAlignment if taxon.name not in taxa])

    AlignIO.write(strippedAlignment, '1'+file, 'fasta')
