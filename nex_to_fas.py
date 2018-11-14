"""converts nexus alignments to fasta format"""



import sys, os
from Bio import AlignIO

try:
    inDir = sys.argv[1]
except IndexError:
    print("Formatting files in current working directory")
    inDir = os.getcwd()


# checks files in the chosen directory
count = 0

for file in os.listdir(inDir):
    fileStrip = file.replace("._", "")
    name, ext = os.path.splitext(fileStrip)
    if ext == '.nex': # if it's a nexus file
        alignment = AlignIO.read(fileStrip, "nexus")
        with open(os.path.join(os.getcwd(), name+".fasta"), 'w') as outFile:
            outFile.write(alignment.format("fasta"))
            if count%10==0:
                print("Reading file #{}".format(count))
    count += 1

print("Done!")
