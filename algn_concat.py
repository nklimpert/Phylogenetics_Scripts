#!/usr/bin/env python

'''USAGE: algn_concat.py <file1> <file2> <file3> ... > outFile'''

#TODO : implement parseargs to deal with different formats
#TODO : write a partition file based on the lengths of all the alignments

import sys
from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq


def getTaxa(alignment):
    '''alignment is a MultipleSeqAlignment object
       Returns a set of the sequence ids for each alignment'''
    includedTaxa = set()
    for record in alignment:
        includedTaxa.add(record.id)
    return includedTaxa


def main():
    fileHandles = sys.argv[1:]
    inFormat = 'fasta'
    outFormat = 'fasta'

    alignments = [AlignIO.read(file, inFormat) for file in fileHandles]
    
    
    # This block should get all of the taxa across all taxa without any repeats
    matrixTaxa = set()
    for alignment in alignments:
        # adds all the elements of the alignments set to the whole set
        matrixTaxa.update(getTaxa(alignment))

    #next, need to add the missing taxa to each alignment
    for alignment in alignments:
        missingTaxa = matrixTaxa - getTaxa(alignment)
        for taxon in missingTaxa:
            #add a dummy alignment
            dummy = SeqRecord(Seq(alignment.get_alignment_length()*'-', generic_dna), id=taxon,
                              name=taxon)
            alignment.append(dummy)
    # need to sort all of the alignments after adding dummy sequences
    map(lambda x: x.sort(), alignments)
    combinedMatrix = alignments[0]
    for alignment in alignments[1:]:
        combinedMatrix = combinedMatrix + alignment
    #TODO : find better way to silence the record descriptions
    for record in combinedMatrix:
        record.description = ''
    print(combinedMatrix.format(outFormat))


if __name__ == "__main__":
    main()
    