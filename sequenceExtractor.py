import sys

importantTaxa = ['Apteria_aphylla', 'Burmannia_bicolor', 'Gymnosiphon_longistylus']

inFile = sys.argv[1]



with open(inFile, 'r') as i:
    for line in i:
        if line.split(' ')[0] in importantTaxa:
            with open(line.split(' ')[0]+'.fasta', 'w') as o:
                o.write(line)
