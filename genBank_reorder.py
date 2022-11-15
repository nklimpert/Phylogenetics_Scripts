#!/usr/bin/env python3

from Bio import SeqIO
import argparse

def parseInput():
    '''Parses the line arguments and returns it as a tuple'''

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Annotated genbank file")
    parser.add_argument("-shift", default=0, help="The new starting point of the genbank file")
    parser.add_argument("-output", default=str(
        "_shifted.fasta"),
        help="Name of output file. Defaults to <gbfile>_shifted.fasta")

    args = parser.parse_args()

    if args.output == "_shifted.fasta":
        output = (args.input).split('.')[0] + args.output
    else:
        output = args.output
    shift = int(args.shift)
    return (args.input, shift, output)

def reorder(gbFile, n):
    record = SeqIO.read(gbFile, "genbank")
    left = record[0:n]
    right = record[n:]

    record = right + left

    return (record)

def main():

    genFile, shift, writeFile = parseInput()
    ## displayGB(genFile)
    SeqIO.write(reorder(genFile, shift), writeFile, "genbank")

if __name__ == "__main__":
    main()