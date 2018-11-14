import os

for filename in os.listdir():
    if filename.endswith(".FNA"):
        data = []
        with open(filename, 'r') as file:
            for line in file:
                if '>_R_' in line:
                    data += ('>' + line.strip('>_R_'))
                else:
                    data += [line]

        with open(filename, 'w') as outFile:
            for line in data:
                outFile.write(line)
print("Done!")
