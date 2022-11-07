#! /usr/bin/env python

from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import sys
import re
from Bio.Alphabet.IUPAC import ambiguous_dna as alph

def parse_FASTA(fileHandle):
    '''returns a list of seq features that can be appended to the seq features of the sequence to\
       be annotated'''
    features = [record for record in SeqIO.parse(fileHandle, 'fasta')]
    for seq in features:
        seqID = seq.id
        description = seq.description
        strand = 1
        matches = re.search(r"(c?)(\d+)\-(\d+)", description)
        if matches:
            comp, start, end = matches.groups()
            if comp:
                strand = -1
                start, end = end, start
            feature = SeqFeature(FeatureLocation(int(start), int(end)), type='CDS', id=seqID, strand=strand)
            feature.qualifiers['gene'] = seqID
            yield feature
mainSeqHandle = sys.argv[1]

features = sys.argv[2]

mainSeq = SeqIO.read(mainSeqHandle, "fasta", alphabet=alph)

f = [x for x in parse_FASTA(features)]

mainSeq.features.extend(f)

SeqIO.write(mainSeq, sys.stdout, "genbank")