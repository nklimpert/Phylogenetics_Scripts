#fileSorter.py

import os
import sys
import shutil

#will want to switch back to this
maindir = os.getcwd()

for file in os.listdir():
    #grab the extension
    extension = (os.path.splitext(file)[-1]).replace('.', '')
    folderName = extension.title() + '_Files'
    if not os.path.isdir(os.path.join(maindir, folderName)):
        os.mkdir(os.path.join(maindir, folderName))
    shutil.move(file, os.path.join(maindir, folderName))
