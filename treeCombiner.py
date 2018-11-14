import os


for file in os.listdir():
    if os.path.splitext(file)[-1] == ".tre":
        with open(file, 'r') as inFile:
            with open(os.path.split(os.getcwd())[-1].split('_')[-1]+"_FastTrees.tre", 'a+') as outFile:
                outFile.write(inFile.read())