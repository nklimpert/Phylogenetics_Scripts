import Bio
from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

import os


fullTaxonSet = {"DALT", "SRR3938623", "P09", "P32", "SRR3938611", "P26", "P27", "DISO1_3", "P25", "DIPE1_3", "P29", "P28", "SRR3938635", "P30", "P05", "P04", "P31", "DVIT", "DISY1_3", "P03", "DICO1_3", "P06", "P18", "P02", "P23", "P24", "P21", "P22", "DCOT", "P20", "SRR1218151", "P10", "SRR5457049", "P01", "P08", "P07", "TACT", "P17"}

#main directory where all the files are
maindir = os.getcwd()

#loops over each
for root, dirs, files in os.walk(maindir):
    #files are only those with the nexus extension in the cwd
    for file in filter(lambda x: x.endswith('.nex'), files):
        alignment = AlignIO.read(os.path.join(root,file), "nexus")

        #makes a set of all the names of taxa in the alignment
        taxa = set(record.id for record in alignment)

        #how long each sequence is in the alignment
        seqLength = alignment.get_alignment_length()

        #the sequences that are missing from the alignment
        missingSeqs = fullTaxonSet - taxa

        #only do this if there are missing sequences
        for taxon in missingSeqs:
            #make a dummy sequence of the right length
            dummy = SeqRecord(Seq(seqLength*'N', generic_dna), id=taxon, name=taxon)
            alignment.append(dummy)

        #at this point, alignment should be filled, so it can be rewritten
        with open(os.path.join(root,file), 'w') as outFile:
            outFile.write(alignment.format("nexus"))
