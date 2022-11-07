#!/usr/bin/python

import argparse
import sys
from Bio import AlignIO






def main():
    parser = argparse.ArgumentParser(description="Removes the third codon position from an alignment\
                                                  and prints it to the stdout")
    parser.add_argument("inFiles", nargs='+', metavar="<inFiles>",
                        help="The alignments to be concatenated")

    args = parser.parse_args()

    alignFiles = args.inFiles
    for file in alignFiles:
        alignment = AlignIO.read(file, 'fasta')
        
        if len(alignment[0]) % 3 != 0:
            print('{} WARNING: ALIGNMENT NOT IN MULTIPLES OF THREE: PLEASE CHECK! {}'.format('-'*10,'-'*10))
            exit()
        
        for seq in alignment:
            seq.seq = seq.seq.tomutable()
            for i in range(2, len(seq.seq), 3):
                seq.seq[i] = '-'
        
    AlignIO.write(alignment, sys.stdout, 'fasta')




if __name__ == "__main__":
    main()