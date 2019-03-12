'''ASSUMPTIONS: That the current working directory has FNA files that have been aligned via MAFFT using the --adjustdirection setting,
    which MAFFT displays by adding _R_ at the beginning of FASTA names'''

import os

nameCount = {}

for filename in os.listdir():
    if filename.endswith(".FNA"):
        with open(filename, 'r') as file:
            for line in file:
                if '>_R_' in line:
                    if line in nameCount:
                        nameCount[line] += 1
                    else:
                        nameCount[line] = 1

for name in nameCount:
    print(name, nameCount[name])
else:
    print("None")