#IQTree on all alignments using the given MODELS

import sys
import os
import subprocess

#should be the full path to the models file
iFile = sys.argv[1]

workingDirectory = os.getcwd()

#extract the path and the filename from the input
modelsPATH, modelsFile = os.path.split(iFile)

#change directory to modelsFile
os.chdir(modelsPATH)

#Build a dictionary where the keys are filenames and values are models
models = {}
with open(modelsFile, 'r') as mFile:
    for line in mFile:
        keyVal = line.split('\t')
        models[keyVal[0][:-4]] = keyVal[1].replace('\n', '')

#change back to the directory with all of the alignments
os.chdir(workingDirectory)


#this will run command (which should be formatted as a list of args)

for file in os.listdir():
    #check if file extension is .FNA
    if os.path.splitext(file)[-1] == '.FNA':
        #make the command
        command = [r"C:\Users\klimpert\PhylogeneticsPrograms\iqtree-1.6.5-Windows\bin\iqtree.exe", "-s", file, "-m", models[file], '-bb', '1000', '-nt', 'AUTO']
        subprocess.run(command, shell=True)
