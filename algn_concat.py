#!/usr/bin/env python3.7

import sys
import os
import re
from Bio import AlignIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import collections
import argparse


def makePartitions(partitions, file):
    partition_file = """## ALIGNMENT FILE ##
alignment = infile.phy;

## BRANCHLENGTHS: linked | unlinked ##
branchlengths = unlinked;

## MODELS OF EVOLUTION for PartitionFinder: all | mrbayes | beast | <list> ##
models = all;

## MODEL SELECTION: AIC | AICc | BIC ##
model_selection = AICc;

## DATA BLOCKS ##
[data_blocks]
{}


## SCHEMES, search: all | greedy | rcluster | hcluster | user ##
[schemes]
search = rcluster;

    """

    with open(file, 'w+') as outFile:
        outString = ""
        for line in partitions.split(';'):
            line = line.strip()
            regex = re.compile('(\w+) \= (\d+)\-(\d+)', re.IGNORECASE)
            matched = regex.match(line)
            if matched:
                gene = matched.group(1)
                start = int(matched.group(2))
                end = int(matched.group(3))
                for position in range(1,4):
                    outString += '\t{}_pos{} = {}-{}\\3;\n'.format(gene, str(position), str(start-1+position), str(end))
        outFile.write(partition_file.format(outString))



def getTaxa(alignment):
    '''alignment is a MultipleSeqAlignment object
       Returns a set of the sequence ids for each alignment'''
    includedTaxa = set()
    for record in alignment:
        includedTaxa.add(record.id)
    return includedTaxa


def main():
    parser = argparse.ArgumentParser(description="Concatenate a set of multiple sequence alignments\
                                                  and prints the output (unless -o is specified).\
                                                  Can also be used to quickly convert from one \
                                                  format to another. Requires BioPython.")
    parser.add_argument("inFiles", nargs='+', metavar="<inFiles>",
                        help="The alignments to be concatenated")
    parser.add_argument("--infmt", choices=['fasta', 'nexus', 'phylip'],
                        default='fasta', help="The file format of the input alignments -\
                                 Defaults to fasta")
    parser.add_argument("--outfmt", choices=['fasta', 'nexus', 'phylip','stockholm'],
                        default='fasta', help="The file format of the output alignment -\
                                 Defaults to fasta")
    parser.add_argument("-o", "--out", nargs='?', metavar="<outFile>",
                        default=sys.stdout,
                        help="Writes the concatenated matrix to the output file, if specified.\
                              Otherwise, writes to stdout.")
    parser.add_argument("-p", "--partitions", metavar="<PartitionFile>",
                        help="Use this option to save a partition file to the specified handle.")
    args = parser.parse_args()

    fileHandles = args.inFiles
    inFormat = args.infmt
    outFormat = args.outfmt
    if outFormat == 'phylip':
        outFormat = 'phylip-relaxed'
    partitionFile = args.partitions

    # Storing all of the alignments in a dictionary as filehandle: alignment
    alignments = collections.OrderedDict()
    try:
        for file in fileHandles:
            alignments[file] = AlignIO.read(file, inFormat)
    except:
        print("There was something wrong with " + file)

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
            dummy = SeqRecord(Seq(alignment.get_alignment_length()*'-'), id=taxon,
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
            records1 = set(record.id for record in combinedMatrix)
            records2 = set(record.id for record in alignment)
            combinedMatrix = combinedMatrix + alignment
        endPos = combinedMatrix.get_alignment_length()
        part_name = os.path.splitext(os.path.basename(filename))[0]
        partitions[part_name] = (startPos, endPos)
        startPos = endPos+1

    # TODO : find better way to silence the record descriptions
    for record in combinedMatrix:
        record.description = ''
    AlignIO.write(combinedMatrix, args.out, outFormat)
    if(partitionFile):
        parts = ''
        for part_name, values in partitions.items():
                parts += "{} = {}-{};\n".format(part_name, values[0], values[1])
        makePartitions(parts, partitionFile)


if __name__ == "__main__":
    main()
