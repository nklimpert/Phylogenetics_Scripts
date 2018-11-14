from Bio import SeqIO
from sys import argv

taxonFile = argv[1]
taxonName = "Dioscorea_elephantipes"


for seq in SeqIO.parse(taxonFile, 'fasta'):
    gene = seq.id
    seq.id = taxonName
    seq.description = ''
    
    with open('{}_{}.fasta'.format(taxonName, gene), 'w') as outFile:
        outFile.write(seq.format('fasta'))
        
print('Done!')
