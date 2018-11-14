"""create random bins of the nexus alignments in the current working directoryself.
"""

import os
import shutil
import random

maindir = os.getcwd()

#make 13 folders, one for each bin
print("Making bin folders...")
for i in range(13):
    folderName = "Bin" + str(i+1)
    os.mkdir(os.path.join(maindir, folderName))


#list of folders
folderNames = []


fileNames = []
print("Making file lists...")
for file in os.listdir():
    #check if the file is a nexus file
    if os.path.splitext(file)[-1] == '.nex':
        fileNames.append(file)
    #otherwise if it's one of the new folders, add it to the folderNames
    elif os.path.isdir(file):
        folderNames.append(file)

print("Randomly sorting alignments into bins....")
#fill each of the empty lists with 20 random genes alignments
for bin in folderNames:
    for x in range(20):
        #make sure the list of fileNames is not zero
        if len(fileNames) != 0:
            #shuffle the list of names and take the last one off, then add it to the folder
            random.shuffle(fileNames)
            shutil.move(fileNames.pop(), bin)

print("Done!")
