#! /usr/bin/env python

import os
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
import argparse
import re
import sys

taxa = []


parser = argparse.ArgumentParser(description="removes the taxa in the provided .txt file from the\
                                 alignments in the current directory. Depends on BioPython.")
parser.add_argument("inFiles", nargs='+', metavar="<inFiles>",
                    help="The alignments to be stripped")
parser.add_argument("--infmt", choices=['fasta', 'nexus', 'phylip'],
                    default='fasta', help="The file format of the input alignments -\
                                Defaults to fasta")
parser.add_argument("-t", "--taxa", nargs='+', metavar="<taxon>",
                    required=True,
                    help="The taxa to be removed. Supports regular expressions.\
                          E.x., -t 'Homo.*' will remove both Homo_sapiens and\
                          Homo_neandertalis.")
parser.add_argument("-o", "--out", default=sys.stdout,
                    help="Where the output should be saved. Defaults to stdout.")
args = parser.parse_args()

taxa = args.taxa

taxa_regex = [re.compile(taxon) for taxon in taxa]

files = args.inFiles

for file in files:
    geneAlignment = AlignIO.read(file, args.infmt)

    strippedAlignment = MultipleSeqAlignment([sequence for sequence in geneAlignment
                                             if not any(regex.match(sequence.name)
                                              for regex in taxa_regex)])

    AlignIO.write(strippedAlignment, args.out, 'fasta')
