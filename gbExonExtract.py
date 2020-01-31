#!/usr/bin/env python
"""extracts the exons from a genbank file and writes them to a fasta.

    Usage: gbExonExtract.py inFile.gb -o outFile.fasta

    Dependencies: Biopython

"""

from Bio import SeqIO
import argparse

TYPE_LIST = ("CDS", "tRNA", "rRNA")


def parseInput():
    '''Parses the line arguments and returns it as a tuple'''

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Annotated genbank file")
    # TODO figure out how to allow one default to follow another
    # TODO maybe have default direct somewhere to set the output
    parser.add_argument("-output", default=str(
        "_Extracted.fasta"),
        help="Name of output file. Defaults to <gbfile>_Extracted.fasta")

    args = parser.parse_args()

    if args.output == "_Extracted.fasta":
        output = (args.input).split('.')[0] + args.output
    else:
        output = args.output

    return (args.input, output)


def extractExons(gb_file, w_File):
    '''currently set up to extract exons from gb_file, open a new file, and write to it'''
    # TODO change the extract method so that it simply returns them as a list

    # TODO make sure that it doesn't add replicates
    includedGenes = []  # will be a record of all the genes included to prevent replicates
    for seq_record in SeqIO.parse(gb_file, "genbank"):
        for feature in seq_record.features:
            geneName = feature.qualifiers.get('gene', None)
            if (feature.type in TYPE_LIST) and (geneName is not None) and (geneName not in includedGenes):
                includedGenes.append(geneName)

                with open(w_File, "a+") as outFile:
                    outFile.write(
                        ">" + geneName[0] + "\n" + str(feature.extract(seq_record.seq)) + "\n")


def main():

    genFile, writeFile = parseInput()
    print(str("-"*20) + " EXTRACTING EXONS " + str("-"*20))
    extractExons(genFile, writeFile)
    print(str("-"*20) + "Done!" + str("-"*20))


if __name__ == "__main__":
    main()
