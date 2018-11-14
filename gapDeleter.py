'''deletes all the sequences that only have gaps'''

from Bio import SeqIO
import os

# outdir = os.path.join(os.getcwd(), "cleaned")
outdir = os.getcwd()
logFile = "gapDeleter_log.txt"
log = {}

for file in os.listdir():
    for current_seq in SeqIO.parse(file, "fasta"):
        
        ungapped = current_seq.seq.ungap(gap="-")

        # checks whether the sequence has an bases in it or is just blank
        if not str(ungapped) == "NNN":

            # todo add it to a file in the cleaned directory
            with open(os.path.join(outdir, file), 'a+') as geneFile:
                geneFile.write(ungapped.format("fasta"))

            break
        else:
            if file not in log.keys():
                log[file] = [current_seq.id]
            else:
                log[file].append(current_seq.id)


# writes the logfile
with open(logFile, 'w') as outFile:
    for key in log.keys():
        outFile.write(key)
        for i in log[key]:
            outFile.write(i)