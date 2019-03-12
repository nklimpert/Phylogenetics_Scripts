#fasta only combine w25 sequences (Burmannia_bicolor)
import os

## TODO: change this path
appendPath = r"C:\Users\klimpert\Documents\BIOL525B\Dioscorea_RawFASTA"


dataPath = r"C:\Users\klimpert\Documents\BIOL525B\MH_Included\Mycohets_Copy"

dataDict = {}


#for each file in both directories
for i in range(len(os.listdir(appendPath))):

    appendTo = os.listdir(appendPath)[i]
    data = os.listdir(dataPath)[i]
    os.chdir(appendPath)
    with open(appendTo, 'a') as A:
        print("Opening file: " + appendTo)
        os.chdir(dataPath)
        with open(data, 'r') as D:
            print("Reading... \n" + data)
            #code snippet that separates out only W25
            data = D.read()
            d = data.split('>')[1:]
            j = ''
            for l in d:
                if 'W25' in l:
                    j = '>'+l #j is now just the W25 segments
            A.write(j)


print("Done!")
