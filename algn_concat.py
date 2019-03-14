#!/usr/bin/env python

import sys
from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq
import collections
import argparse


def getTaxa(alignment):
    '''alignment is a MultipleSeqAlignment object
       Returns a set of the sequence ids for each alignment'''
    includedTaxa = set()
    for record in alignment:
        includedTaxa.add(record.id)
    return includedTaxa


def main():
    parser = argparse.ArgumentParser(description="Concatenate a set of multiple sequence alignments")
    parser.add_argument("inFiles", nargs='+', metavar="<inFiles>",
                        help="The alignments to be concatenated")
    parser.add_argument("--infmt", choices=['fasta', 'nexus', 'phylip'],
                        default='fasta', help="The file format of the input alignments -\
                                 I can't handle multiple alignments with \
                                 different formats, sorry!"
                        )
    parser.add_argument("--outfmt", choices=['fasta', 'nexus', 'phylip'],
                        default='fasta', help="The file format of the output alignment -\
                                 I can't handle multiple alignments with \
                                 different formats, sorry!"
                        )
    parser.add_argument("-o", "--out", nargs='?', default=sys.stdout,
                        help="Writes the concatenated matrix to the output file, if specified.\
                              Otherwise, writes to stdout.")
    parser.add_argument("-p", "--partitions",
                        help="Use this option to save a partition file as partitions.txt")
    args = parser.parse_args()

    fileHandles = args.inFiles
    inFormat = args.infmt
    outFormat = args.outfmt
    partitionFile = args.partitions
    
    # Storing all of the alignments in a dictionary as filehandle: alignment
    alignments = collections.OrderedDict()
    for file in fileHandles:
        alignments[file] = AlignIO.read(file, inFormat)

    # This block should get all of the taxa across all taxa without any repeats
    matrixTaxa = set()
    for alignment in alignments.values():
        # adds all the elements of the alignments set to the whole set
        matrixTaxa.update(getTaxa(alignment))

    # next, need to add the missing taxa to each alignment
    for alignment in alignments.values():
        missingTaxa = matrixTaxa - getTaxa(alignment)
        for taxon in missingTaxa:
            # add a dummy alignment
            dummy = SeqRecord(Seq(alignment.get_alignment_length()*'-', generic_dna), id=taxon,
                              name=taxon)
            alignment.append(dummy)
    # need to sort all of the alignments after adding dummy sequences
    map(lambda x: x.sort(), alignments.values())
    combinedMatrix = None
    
    # Writing all of the partition information to a dictionary
    # Keeps track of the file handle, beginning, and end
    partitions = collections.OrderedDict()

    for filename, alignment in alignments.items():
        if not combinedMatrix:
            combinedMatrix = alignment
            startPos = 1
        else:
            combinedMatrix = combinedMatrix + alignment
        endPos = combinedMatrix.get_alignment_length()
        partitions[filename] = (startPos, endPos)
        startPos = endPos+1

    # TODO : find better way to silence the record descriptions
    for record in combinedMatrix:
        record.description = ''
    AlignIO.write(combinedMatrix, args.out, outFormat)
    if(partitionFile):
        with open(partitionFile, 'w') as outFile:
            for filename, values in partitions.items():
                outFile.write("{}: {}-{};\n".format(filename, values[0], values[1]))


if __name__ == "__main__":
    main()
