import os
from Bio import SeqIO

for file in os.listdir():
    seqs= SeqIO.parse(open(file), 'fasta')
    for seq in seqs:
        with open(seq.id + '.fasta', 'a+') as outFile:
            seq.id = seq.id + file.split('.')[0]
            outFile.write(seq.format('fasta'))