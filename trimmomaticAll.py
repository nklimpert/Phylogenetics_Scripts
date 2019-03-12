#! python
import os
import subprocess

inputdirectory = "C:\\Users\\klimpert\\PhylogeneticsPrograms\\NOVOPlasty\\Pogoniopsis\\"
processed = "C:\\Users\\klimpert\\PhylogeneticsPrograms\\NOVOPlasty\\Pogoniopsis\\trimmed\\"
log = "C:\\Users\\klimpert\\PhylogeneticsPrograms\\NOVOPlasty\\Pogoniopsis\\log\\"
trimmomaticdirectory = "C:\\Users\\klimpert\\PhylogeneticsPrograms\\Trimmomatic-0.38\\trimmomatic-0.38.jar"


for fileF in os.listdir():
        dividing = fileF.split(".")
        if ("F" in fileF):
            fileR = fileF.replace('F', 'R')
            if os.path.isfile(os.path.join(os.getcwd(),fileR)):
                dividing1 = fileR.split(".")
                log1 = dividing[0]
                output1 = dividing[0]
                output2 = dividing1[0]
                subprocess.call(["java", "-jar", trimmomaticdirectory, "PE", "-phred33", "trimlog", log+log1, fileF, fileR, output1, "unpaired"+output1, output2, "unpaired"+output2, "ILLUMINACLIP:TruSeq2-PE.fa:2:30:10", ], shell=True)