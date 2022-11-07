#!/usr/bin/env python3
"""strips out files anything besides the species in the provided .txt file"""



from Bio import SeqIO
import os, sys

TAXA = []

file = sys.argv[1]

with open(file, 'r') as inFile:
    for line in inFile:
        TAXA.append(line.strip())

FASFORMAT = {".fasta", ".fas", ".FNA", ".fa"}

name = os.path.basename(file.split('.')[0])

for file in os.listdir():
    if os.path.splitext(file)[-1] in FASFORMAT:
        with open("filtered_" + file, 'w') as outFile:
            for seq in SeqIO.parse(file, "fasta"):
                if seq.id in TAXA:
                    outFile.write(seq.format("fasta"))

print("Done!")