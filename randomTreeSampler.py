#Take random subsamples of trees from a file and create trees based on them
import sys
import random
trees = []
f = sys.argv[1]

#can change the number of bins to put them in
BIN_NUMBER = 20


with open(f, 'r') as openFile:
    for line in openFile:
        trees.append(line)

perBin = len(trees)//BIN_NUMBER

#write a file of the trees?
for i in range(BIN_NUMBER):
    with open(str('bin'+str(i)+'.txt'), 'w') as binFile:
        for j in range(perBin):
            random.shuffle(trees)
            binFile.write(trees.pop())
print('Done!')
