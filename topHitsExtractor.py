"""Expects the input to be a blast-xml file, will pull out all the top hits and put it in a fasta file."""

import sys
from Bio import SearchIO

#TODO make this a try/except clause
if len(sys.argv)>2:
    inFile = sys.argv[1]
    outFile = sys.argv[2]
else:
    inFile = r"C:\Users\klimpert\Documents\MHResearch\Gentianaceae\Voyriella_parvifloraExaff2VopaCPGenes.xml"
    outFile = "testResults.fasta"
data = [qresult for qresult in SearchIO.parse(inFile, "blast-xml")
for result in data:
    if len(result) != 0:  # only check it if there's only one result
        #TODO pull out the query id, the hit seq

        #TODO format the query id+hitseq as fasta

#TODO write to the outfile
