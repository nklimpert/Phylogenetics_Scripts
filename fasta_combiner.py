"""Combines files in current working directory with those given in the path.
    Appends the data from the given directory to the working directory files

    ASSUMPTIONS: that there are an equal number of fasta files in each.
"""
import os

appendPath = r"C:\Users\klimpert\Documents\BIOL525B\MH_aligned"
dataPath = r"C:\Users\klimpert\Documents\BIOL525B\Outgroups_Copy"

#for each file in both directories
for i in range(len(os.listdir(appendPath))):

    appendTo = os.listdir(appendPath)[i]
    data = os.listdir(dataPath)[i]
    os.chdir(appendPath)
    with open(appendTo, 'a') as A:
        print("Opening file: " + appendTo)
        os.chdir(dataPath)
        with open(data, 'r') as D:
            print("Reading..." + data)
            A.write(D.read())

print("Done!")
